# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:07:16 2019

@author: wizza
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#img=cv2.imread(r'D:\TIANCHI\image_train\T1mLyYXvRaXXXXXXXX_!!1-item_pic.jpg.jpg')
#name='T1mLyYXvRaXXXXXXXX_!!1-item_pic.gif.jpg'
#txt_path='D:/TIANCHI/txt_train/'

def deal_txt(direction):
    positions=[]
    labels=[]
    file=open(direction,encoding='utf-8-sig')
    with file as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip().split(',')
            position=[float(i) for i in line[0:8]]
            position_deal=[[position[i],position[i+1]] for i in range(0,8,2)]
            positions.append(position_deal)
            labels.append(line[-1])
    return positions,labels

def convert_img(img,name,txt_path):
    positions,labels=deal_txt(txt_path+name[:-3]+'txt')
    deal_img,deal_labels=[],[]
    for i in range(len(positions)):
        if labels[i]!='###':
            pts1=np.float32(positions[i])
            h1=np.sqrt(np.sum(np.square(pts1[0]-pts1[1])))
            h2=np.sqrt(np.sum(np.square(pts1[2]-pts1[3])))
            w1=np.sqrt(np.sum(np.square(pts1[1]-pts1[2])))
            w2=np.sqrt(np.sum(np.square(pts1[0]-pts1[3])))
            w=np.ceil(max(w1,w2))
            h=np.ceil(max(h1,h2))
            pts2=np.float32([[0,h],[0,0],[w,0],[w,h]])
            M = cv2.getPerspectiveTransform(pts1, pts2)
# 进行透视变换，参数3是目标图像大小
            dst = cv2.warpPerspective(img, M, (w, h))
            dst=cv2.resize(dst,(100,100))
            deal_img.append(dst)
            deal_labels.append(labels[i])
    return deal_img,deal_labels
#convert_img(img,name,txt_path)
#    plt.show()  
#plt.subplot(121), plt.imshow(deal_img[17][:, :, ::-1]), plt.title('input')

def to3dim(dirs):
    imgplt=plt.imread(dirs)
    a,b,c,d=cv2.split(imgplt)
    img=cv2.merge((a,b,c))
    return img

import os
root_path="D:/TIANCHI/"
dir_img=root_path + 'image_train/'
dir_txt=root_path+'txt_train/'
deal_imgs,labels=[],[]
break_name=''
import time
start=time.time()
for root,dirs,files in os.walk(dir_img):
    for name in files:
        img=cv2.imread(dir_img+name)
        if img is None:
            img=to3dim(dir_img+name)
        break_name=name
        deal_img,label=convert_img(img,name,dir_txt)
        deal_imgs.extend(deal_img)
        labels.extend(label)
print('time:',time.time()-start)
print(deal_imgs[:2])
print(labels[:2])
