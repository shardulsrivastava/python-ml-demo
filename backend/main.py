import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from PIL import Image
import h5py
import numpy as np
from tensorflow.keras.models import load_model
from ml4h.models.model_factory import get_custom_objects
from ml4h.tensormap.ukb.survival import mgb_afib_wrt_instance2
from ml4h.tensormap.ukb.demographics import age_2_wide, af_dummy, sex_dummy3

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to ECG Intelligence"}

@app.post("/predict")
# def get_prediction(file: UploadFile = File(...)):
def get_prediction():
    return predict()

ECG_REST_LEADS = {
    'strip_I': 0, 'strip_II': 1, 'strip_III': 2, 'strip_V1': 3, 'strip_V2': 4, 'strip_V3':5,
    'strip_V4': 6, 'strip_V5': 7, 'strip_V6': 8, 'strip_aVF': 9, 'strip_aVL': 10,'strip_aVR': 11}

ECG_SHAPE = (5000, 12)
ECG_HD5_PATH = 'ukb_ecg_rest'
def ecg_as_tensor(ecg_file):
    with h5py.File(ecg_file, 'r') as hd5:
        tensor = np.zeros(ECG_SHAPE, dtype=np.float32)
        for lead in ECG_REST_LEADS:
            data = np.array(hd5[f'{ECG_HD5_PATH}/{lead}/instance_0'])
            tensor[:, ECG_REST_LEADS[lead]] = data
        tensor -= np.mean(tensor)
        tensor /= np.std(tensor) + 1e-6
        # print(tensor.shape)
        return tensor

def predict():
    tensor = ecg_as_tensor('ecg/fake_0.hd5')
    tensor = np.expand_dims(tensor, axis=0)
    output_tensormaps = {tm.output_name(): tm for tm in [mgb_afib_wrt_instance2, age_2_wide, af_dummy, sex_dummy3]}
    custom_dict = get_custom_objects([mgb_afib_wrt_instance2, age_2_wide, af_dummy, sex_dummy3])
    model = load_model('ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5',
                    custom_objects=custom_dict)
    prediction = model(tensor)
    # print(prediction)

    # output_tensormaps = {tm.output_name(): tm for tm in [mgb_afib_wrt_instance2, age_2_wide, af_dummy, sex_dummy3]}
    # custom_dict = get_custom_objects([mgb_afib_wrt_instance2, age_2_wide, af_dummy, sex_dummy3])
    # model = load_model('model_zoo/ECG2AF/ecg_5000_survival_curve_af_quadruple_task_mgh_v2021_05_21.h5', custom_dict)
    # ecg = np.random.random((1, 5000, 12))
    # prediction = model(ecg)
    for name, pred in zip(model.output_names, prediction):
        otm = output_tensormaps[name]
        print(otm)
        if otm.is_survival_curve():
            intervals = otm.shape[-1] // 2
            days_per_bin = 1 + otm.days_window // intervals
            predicted_survivals = np.cumprod(pred[:, :intervals], axis=1)
            # print(pred)
            # print(predicted_survivals)
            print(type(otm))
            print(f'AF Risk {str(otm)} prediction is: {str(1 - predicted_survivals[0, -1])}')
        else:
            print(f'{otm} prediction is {pred}')
    return prediction



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8081)
     