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

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"


print("===== Describe an image - remote =====")
description_results = computervision_client.describe_image(remote_image_url )

print("Description of remote image: ")
if (len(description_results.captions) == 0):
    print("No description detected.")
else:
    for caption in description_results.captions:
        print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
print()
'''
END - Describe an Image - remote
'''
print("End of Computer Vision quickstart.")


"""
画像タグの取得
"""
# print("===== Tag an image - remote =====")
# # Call API with remote image
# tags_result_remote = computervision_client.tag_image(remote_image_url )

# # Print results with confidence score
# print("Tags in the remote image: ")
# if (len(tags_result_remote.tags) == 0):
#     print("No tags detected.")
# else:
#     for tag in tags_result_remote.tags:
#         print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
# print()
# '''
# END - Tag an Image - remote
# '''
# print("End of Computer Vision quickstart.")