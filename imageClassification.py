#!/usr/bin/env python
# coding: utf-8

# In[4]:


from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras import Sequential


# In[5]:


classifier = Sequential()


# In[6]:


##STEP 1: CONVOLUTIONAL LAYER
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation="relu"))


# In[7]:


##STEP 2: POOLING
classifier.add(MaxPooling2D(pool_size=(2,2)))


# In[8]:


##STEP 3: FLATTENING
classifier.add(Flatten())


# In[11]:


###ANN
##STEP 4: FULL CONNECTED LAYER
num_labels = 4
classifier.add(Dense(activation="relu", units=128))
classifier.add(Dense(activation="softmax", units=num_labels))


# In[12]:


##COMPILE MODEL
classifier.compile(optimizer="adam",loss="categorical_crossentropy",metrics=['accuracy'])


# In[15]:


####READING DATA
from keras.preprocessing.image import ImageDataGenerator
URL_TRAIN = "D:/UNI/TESIS1/data/train"
URL_TEST = "D:/UNI/TESIS1/data/test"
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(URL_TRAIN,
                                                    target_size=(64, 64),
                                                    batch_size=32,
                                                    class_mode='categorical')

test_set = test_datagen.flow_from_directory(URL_TEST,
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='categorical')


# In[17]:


classifier.fit_generator(train_set,
        steps_per_epoch=2481,
        epochs=20,
        validation_data=test_set,
        validation_steps=621)


# In[ ]:




