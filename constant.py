
from  dotenv import load_dotenv
load_dotenv()
import os 

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
CLOUD_FRONT_URL = os.getenv("CLOUD_FRONT_URL")