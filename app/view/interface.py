import streamlit as st
from pydantic import StrictStr, EmailStr
# from utils import ecglogger


class ECGInterface:
    """
    WebApp class is used to accomodate any changes into UI functionality.
    Current Functionality
    * Takes Users name and email
    * Display the images

    """
    def __init__(self, config, ENV: StrictStr):
        
        # setup logger
        # ecglogger.ECGLogger(level="INFO")
        st.title("ECG2AF Model Web Application")

        with st.form(key='image_upload_form'):
        
            self.user_name = st.text_input("Enter your name")
            self.user_email = st.text_input("Enter your email")

            self.config = config
            self.ENV = ENV
            cols = st.columns(3)

            # Image upload
            self.uploaded_files = st.file_uploader("Upload ECG images",
                                                   type=config.get(ENV, "IMG_FORMAT"),
                                                   accept_multiple_files=True)
            
            # Submit button
            self.submit_button = st.form_submit_button(label='Submit')
        if self.submit_button:
            self.display_image(self.uploaded_files)

    def display_image(self, uploaded_files, prediction_result: StrictStr = None):
        """Displays the image and its prediction score

        Args:
            image_file (_type_): _description_
            prediction_result (StricStr): _description_
        """
        try:
            for image_file in uploaded_files:
                st.image(image_file, caption=image_file.name)
        # st.image(image_file, caption=f"Uploaded Image", use_column_width=True)
        # st.write(f"Prediction: {prediction_result}")
        except FileNotFoundError:
            st.error(f"Upload the file with reqiored file format {self.config.get(self.ENV, 'IMG_FORMAT')}")
            # ecglogger.logger.error("Invalid File or File Not Found")


