# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
import tensorflow as tf

def get_label1_coor(path):
    """
    标签和坐标位置，输入图片为单位
    path:txt文件的存储目录
    return 标签，坐标
    """
    coor_list = []
    label_list1 = []
    label_name = os.listdir(path)

    for name in label_name:
        coor_list1 = []
        label_list2 = []
        pic_path = path + '\\' + name
        file = open(pic_path, 'r',encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            line_list = line.strip().split(',')
            if '#' not in set(line_list[8]):
                if len(line_list) == 9:
                    coor_list1.append([float(i) for i in line_list[0:8]])
                    label_list2.append(line_list[8])
        coor_list.append(coor_list1)
        label_list1.append(label_list2)
    
    coor_list = np.asarray(coor_list)
    label_list1 = np.asarray(label_list1)
    
    return coor_list, label_list1

coor, label = get_label1_coor('C:\\Users\\Administrator\\data\\tianchi\\Txt')
print(coor)
print(label)

def get_label_image(path,coor_list,label_list1):
    """
    标签和图片，单个图片为单位
    path: jpg图片的存储目录
    coor_list: 图片中坐标序列，输入图片为单位
    label_list1: 图片中标签序列，输入图片为单位
    return image_list, label_list 处理后图片为单位
    """
    image_list = []
    label_list = []
    picture_name = os.dirlist(path)
    
    for i in range(len(picture_name)):
        picture_path = path + '\\' + picture_name[i]
        img = cv2.imread(picture_path,0)
        count = 0
        for coord in coor_list[i]:
            # post1 原图中的四个角点 
            post1 = []
            for i in range(0,8,2):
                post1.append([coord[i],coord[i+1]])
            post1 = np.float32(post1)
            long = max(np.sqrt(np.sum(np.square(post1[0]-post1[3]))),
                       np.sqrt(np.sum(np.square(post1[1]-post1[2]))))
            height = max(np.sqrt(np.sum(np.square(post1[0]-post1[1]))),
                         np.sqrt(np.sum(np.square(post1[2]-post1[3]))))
            # post2 变换后的左上、右上、左下、右下
            post2 = np.float([[0,0],[long,0],[0,height],[long,height]])
            # 生成透视变换矩阵
            M = cv2.getPerspectiveTransform(post1,post2)
            # 进行透视变换，参数3是目标图像大小参数
            dst = cv2.warpPerspective(img,M,(long,height))
            
            # 保存图片到指定位置 label和image对应
            pre_label = label_list1[i][count]
            count += 1
            pre_path = '...' + '\\' + pre_label
            cv2.imwrite(pre_label,dst) # 存为png格式，怎么到指定位置？？？
            
            image_list.append(pre_path)
            label_list.append(pre_label)
            
        image_list = np.asarray(image_list)
        label_list = np.asarray(label_list)
        
        return image_list, label_list

def get_batch(train_list,image_size,batch_size,capacity):
    """
    获取训练批次
    train_list: 2—D list, [image_list,label_list]
    image_size: a int, 训练图像大小
    batch_size: a int，每个批次包含的样本数量
    capacity: a int, 队列容量
    """
    input_queue = tf.train.slice_input_procedure(train_list,shuffle = False)
    
    image_train = tf.read_file(input_queue[0])
    image_train = tf.image.decode_png(image_train) #解码chanel ???
    image_train = tf.image.resize_images(image_train,[image_size,image_size])
    image_train = tf.cast(image_train, tf.float32)/255
    label_train = input_queue[1]
    image_train_batch, label_train_batch = tf.train.shuffle_batch([image_train,label_train],batch_size=batch_size,capacity=capacity,min_after_dequeue=100,num_threads=2)
    return image_train_batch, label_train_batch

