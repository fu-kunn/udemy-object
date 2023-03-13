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

"""
画像説明の取得
"""
# print("===== Describe an image - remote =====")
# description_results = computervision_client.describe_image(remote_image_url )

# print("Description of remote image: ")
# if (len(description_results.captions) == 0):
#     print("No description detected.")
# else:
#     for caption in description_results.captions:
#         print("'{}' with confidence {:.2f}%".format(caption.text, caption.confidence * 100))
# print()
# '''
# END - Describe an Image - remote
# '''
# print("End of Computer Vision quickstart.")


"""
画像カテゴリの取得
"""
# print("===== Categorize an image - remote =====")
# remote_image_features = ["categories"]
# categorize_results_remote = computervision_client.analyze_image(remote_image_url, remote_image_features )

# print("Categorize of remote image: ")
# if (len(categorize_results_remote.categories) == 0):
#     print("No categories detected.")
# else:
#     for category in categorize_results_remote.categories:
#         print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))
# print()
# '''
# END - Categorize an Image - remote
# '''
# print("End of Computer Vision quickstart.")


"""
画像タグの取得
"""
# print("===== Tag an image - remote =====")
# tags_result_remote = computervision_client.tag_image(remote_image_url )

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

"""
物体を検出する
"""
print("===== Detect Object - remote =====")
remote_image_url_objects ="https://learn.microsoft.com/ja-jp/azure/cognitive-services/computer-vision/images/tagging.png"
detect_objects_results_remote = computervision_client.detect_objects(remote_image_url_objects )

print("Detecting object in remote image: ")
if (len(detect_objects_results_remote.objects) == 0):
    print("No objects detected.")
else:
    for object in detect_objects_results_remote.objects:
        print("object at location {}, {}, {}, {}".format( \
        object.rectangle.x, object.rectangle.x + object.rectangle.w, \
        object.rectangle.y, object.rectangle.y + object.rectangle.h))
print()
'''
END - Tag an Image - remote
'''
print("End of Computer Vision quickstart.")