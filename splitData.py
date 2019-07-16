from os import listdir,mkdir
from os.path import isdir,isfile, join
from shutil import rmtree,copy2
import random

inPath = 'images'

animals = [f for f in listdir(inPath) if isdir(join(inPath, f))]

train = 0.8

outPath = 'data'

if isdir(outPath):
    rmtree(outPath, ignore_errors=True)

trainPath = join(outPath,'train')
testPath = join(outPath,'test')

mkdir(outPath)
mkdir(trainPath)
mkdir(testPath)

minimo = 10000

for animal in animals:
    animalPath = join(inPath,animal)
    images = [f for f in listdir(animalPath) if isfile(join(animalPath, f))]

    random.shuffle(images)

    cntImges = len(images)
    cntTrain = int(cntImges*train)
    
    animalOutPathTrain = join(trainPath,animal)
    animalOutPathTest = join(testPath,animal)

    mkdir(animalOutPathTrain)
    mkdir(animalOutPathTest)
    minimo = min(minimo,cntImges-cntTrain)
    if(cntImges-cntTrain<16):
        print(animal,cntImges-cntTrain)
    for i in range(cntImges):
        src = join(animalPath,images[i])
        if(i<cntTrain):#le pertenece a train
            dst = join(animalOutPathTrain,images[i])
            copy2(src,dst)
        else:#le pertenece a test
            dst = join(animalOutPathTest,images[i])
            copy2(src,dst)

print(minimo)