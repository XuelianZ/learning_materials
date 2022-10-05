# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/5 15:54
@Auth ： XuelianZ 1558919395@qq.com
@Purpose：clip 基本用法验证和使用，检测、识别新方法寻找idea
"""
import os
import torch
import clip
from  PIL import Image

imgdir = "/mnt/d/zxl_workspace/projects/000_largefiles/datasets/tmp_images"
modelfile = "/mnt/d/zxl_workspace/projects/000_largefiles/models/clip/ViT-L-14-336px.pt"


class_labels = ['a bike', 'a motobike', 'baby carriage', 'a toy', 'other']

print("*****"*5)
print("model:", os.path.basename(modelfile))
print('class_labels:', class_labels)
print("*****"*5)

device = "cuda" if torch.cuda.is_available() else "cpu"
# ctrl+/ 可注释掉多行
# clip.available_models()
# Out[3]:
# ['RN50',
#  'RN101',
#  'RN50x4',
#  'RN50x16',
#  'RN50x64',
#  'ViT-B/32',
#  'ViT-B/16',
#  'ViT-L/14',
#  'ViT-L/14@336px']
model, preprocess = clip.load(name=modelfile, device=device)

for root, dirs, files in os.walk(imgdir):
    for file in files:
        imagefile = os.path.join(root, file)
    
        image = preprocess(Image.open(imagefile)).unsqueeze(0).to(device)
        text = clip.tokenize(class_labels).to(device)
        
        with torch.no_grad():
            # image_features  = model.encode_image(image)
            # text_features = model.encode_text(text)
            logits_per_image, logits_per_text = model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy() # 单张图片，
        probs = list(probs[0])
        class_idx = probs.index(max(probs))
        print("[{}] -- [{}]    probs：{}".format(file, class_labels[class_idx], probs))


