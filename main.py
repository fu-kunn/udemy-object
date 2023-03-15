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
# remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

read_image_path = 'sample01.jpg'
read_image = open(read_image_path, "rb")

# 画像タグの取得
# read_imageの変数は何回も呼び出さないといけないのか？
def get_tags(filepath):
    read_image = open(filepath, "rb")
    tags_result = computervision_client.tag_image_in_stream(read_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    
    return tags_name

# filepath = 'sample01.jpg'
# print(get_tags(filepath))


def detect_objects(filepath):
    read_image = open(filepath, "rb")
    detect_objects_results = computervision_client.detect_objects_in_stream(read_image)
    objects = detect_objects_results.objects

    return objects
    
# filepath = 'sample01.jpg'
# print(detect_objects(filepath))

import streamlit as st

st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png'])
if uploaded_file is not None:
    # PIL(pythonの画像ライブラリ)でImageクラスを使っている
    img = Image.open(uploaded_file)
    st.image(img)
    # **で囲むことで太文字にできる
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown('> apple, tree, building, green')



# 画像説明の取得
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


# """
# 画像カテゴリの取得
# """
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


# """
# 物体を検出する
# """
# print("===== Detect Object - local =====")
# detect_objects_results = computervision_client.detect_objects_in_stream(read_image)

# print("Detecting object in local image: ")
# if (len(detect_objects_results.objects) == 0):
#     print("No objects detected.")
# else:
#     for object in detect_objects_results.objects:
#         print("object at location {}, {}, {}, {}".format( \
#         object.rectangle.x, object.rectangle.x + object.rectangle.w, \
#         object.rectangle.y, object.rectangle.y + object.rectangle.h))
# print()


