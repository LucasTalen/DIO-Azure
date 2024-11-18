import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv('ENDPOINT')
    KEY = os.getenv('KEY')
    AZURE_S_C_S = os.getenv('AZURE_S_C_S')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')