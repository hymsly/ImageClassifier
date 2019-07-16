import cv2 as cv
from os import listdir
from os.path import isfile, join, isdir

mypath = 'images'

tags = [f for f in listdir(mypath) if isdir(join(mypath, f))]

cntImages = 0

dic = {}

for tag in tags:
    pathTag = join(mypath,tag)
    images = [f for f in listdir(pathTag) if isfile(join(pathTag, f))]
    for image in images:
        try:
            img = cv.imread(join(pathTag,image))
        #h,w,c = img.shape
        #h= (h//20)
        #w= (w//20)
        #if((h,w) in dic):
        #    dic[(h,w)]+=1
        #else:
        #    dic[(h,w)]=1
        except:
            print(join(pathTag,image))
#for d in dic:
#    print(d[0],d[1],dic[d])