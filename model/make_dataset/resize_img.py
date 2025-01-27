
import matplotlib.image as mpimg
import numpy as np
import os
from tool import Tools
from PIL import Image
import random
import time
from tqdm import tqdm
import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('width',type=int)
    parser.add_argument('height',type=int)
    parser.add_argument('output_dir')
    return parser.parse_args()

# 单张图片转换为三通道,相同大小,保存到目标文件夹
def standardize_img(label,img_path,height,width,output_dir):
    try:
        # tmp=mpimg.imread(directory+'/'+img_path)
        img=Image.open(img_path).convert('RGB').resize((width,height))
    except Exception as e:
        print(str(e))
        print(directory+','+img_path)
        return
    
    filename=str(time.time())+str(random.randint(1,100))+'.png'
    # imsave(output_dir+directory+filename,tmp)
    img.save(os.path.join(output_dir,label,filename))
    
args=get_args()
input_dir='E:/双创数据'
output_dir=args.output_dir
Tools.create_save_dir(output_dir)
directories=os.listdir(input_dir)
for directory in directories:
    Tools.create_save_dir(os.path.join(output_dir,directory))
    for img_file in tqdm(os.listdir(os.path.join(input_dir,directory)),ncols=10):
        standardize_img(directory,os.path.join(input_dir,directory,img_file),args.height,args.width,output_dir)
