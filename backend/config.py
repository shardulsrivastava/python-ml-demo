import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini"))


# this is used to set the environment to run the application
# by default it is set for "dev" - development
ENV = os.getenv("APP_ENV", "dev")