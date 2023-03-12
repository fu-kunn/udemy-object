from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


from dotenv import load_dotenv
# .envファイルの内容を読み込見込む
load_dotenv()


KEY = os.environ['KEY_SUB']
ENDPOINT = os.environ['ENDPOINT']
