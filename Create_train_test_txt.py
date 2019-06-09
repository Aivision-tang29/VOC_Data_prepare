#coding:utf-8
import os

train_file=open('./VOC_Rebar/ImageSets/Main/train.txt','w')
test_file=open('./VOC_Rebar/ImageSets/Main/test.txt','w')

train_file_names=os.listdir('./train_dataset')
for image_name in train_file_names:
	train_file.write(image_name.split('.')[0]+'\n')

test_file_names=os.listdir('./test_dataset')
for image_name in test_file_names:
	test_file.write(image_name.split('.')[0]+'\n')

