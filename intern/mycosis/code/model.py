import cv2
import numpy as np
import tensorflow as tf
import os
from tensorflow.keras import Model, applications, models
from tensorflow.keras import regularizers, layers

class PredictionModel():
    def __init__(self):
        super(PredictionModel, self).__init__()

    def create_model(self):
        if hasattr(self, 'm'):
            print('model already created')
            return
        
        ww = './weight'
        w0 = 'f0.h5'
        w1 = 'f1.h5'
        w2 = 'f2.h5'
        w3 = 'f3.h5'
        w4 = 'f4.hdf5'
        
        f0_shape = (200,200,3)
        f2_shape = (299,299,3)
        f1_shape = (200,200,3)
        f4_shape = (int(299*1.25),int(299*1.25),3)
        f3_shape = (299,299,3)
        
        Pretrained_Model_0 = applications.inception_resnet_v2.InceptionResNetV2(input_shape=f0_shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        
        num_class = 8
        
        x_0 = Pretrained_Model_0.output
        x_0 = tf.keras.layers.GlobalAveragePooling2D()(x_0)

        x_0 = layers.Dense(256, activation='relu')(x_0)
        x_0 = layers.Dropout(0.5)(x_0)

        x_0 = layers.Dense(128, activation='relu')(x_0)
        x_0 = layers.Dropout(0.5)(x_0)

        output_layer_0 = layers.Dense(num_class, activation='softmax', name='softmax')(x_0)
        model_0 = Model(inputs=Pretrained_Model_0.input, outputs=output_layer_0)
        
        self.m0 = model_0
        self.m0.load_weights(os.path.join(ww,w0))
        print('xong 0')
        
        Pretrained_Model_1 = applications.inception_v3.InceptionV3(input_shape=f1_shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        
        x_1 = Pretrained_Model_1.output
        x_1 = tf.keras.layers.GlobalAveragePooling2D()(x_1)
        x_1 = tf.keras.layers.Dense(1024,activation='relu')(x_1)
        x_1 = tf.keras.layers.Dropout(0.5)(x_1)

        output_layer_1 = layers.Dense(num_class, activation='softmax', name='softmax')(x_1)
        model_1 = Model(inputs=Pretrained_Model_1.input, outputs=output_layer_1)
        
        self.m1 = model_1
        self.m1.load_weights(os.path.join(ww,w1))
        
        print('xong 1')
        
        
        Pretrained_Model_2 = applications.inception_v3.InceptionV3(input_shape=f2_shape, 
                                                         include_top=False
                                                         ,weights=None
                                                        )
        model_2 = models.Sequential([Pretrained_Model_2
                                   ,layers.Flatten()
                                   ,layers.Dense(num_class, activation='softmax')
                                  ])
        
        self.m2 =model_2
        self.m2.load_weights(os.path.join(ww,w2))
        print('xong 2')
        
        Pretrained_Model_3 = applications.inception_v3.InceptionV3(input_shape=f3_shape, 
                                                         include_top=False
                                                         ,weights=None
                                                        )
        model_3 = models.Sequential([Pretrained_Model_3
                                   ,layers.Flatten()
                                   ,layers.Dense(num_class, activation='softmax')
                                  ])
        
        
        
        self.m3 =model_3
        self.m3.load_weights(os.path.join(ww,w3))
        print('xong 3')
        
        Pretrained_Model_4 = applications.inception_v3.InceptionV3(input_shape=f4_shape, #note
                                                         include_top=False, 
                                                         input_tensor=None, #note
                                                         weights=None)
        Regularizer_Dense=regularizers.l2(0.01)
        Dropout=0.5
        
        model_4 = models.Sequential()
        model_4.add(Pretrained_Model_4)
        model_4.add(layers.GlobalAveragePooling2D()) # note Flatten())
        model_4.add(layers.Dense(1024, activation='relu', kernel_regularizer=Regularizer_Dense))
        model_4.add(layers.Dropout(Dropout))
        model_4.add(layers.Dense(num_class, activation='softmax', kernel_regularizer=Regularizer_Dense))
        
        self.m4 =model_4
        self.m4.load_weights(os.path.join(ww,w4))
        print('xong 4') 
        
        self.number_of_models= (1.1052306/0.94287103**1.0483404*0.891731)
    
    def convert(self,arr):
        aws=[]
        for vec in arr:
            tmp = vec[:len(vec)-1]
            vec = [vec[len(vec)-1]]
            vec.extend(tmp)
            aws.extend([vec])
        return aws
    
    def voting_Nmodels_batchsizetime(self,img):
        #to transform for voting
        
        f0_shape = (200,200)
        f2_shape = (299,299)
        f1_shape = (200,200)
        f4_shape = (int(299*1.25),int(299*1.25))
        f3_shape = (299,299)
        
        im = cv2.imread(img)
        im = cv2.resize(im,f0_shape)
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        
        p0= self.m1.predict(im,batch_size=1)
        
        im = cv2.imread(img)
        im = cv2.resize(im,f1_shape)
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        
        p1= self.m1.predict(im,batch_size=1)
        
        im = cv2.imread(img)
        im = cv2.resize(im,f2_shape)
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        
        p2= self.m2.predict(im,batch_size=1)
        
        im = cv2.imread(img)
        im = cv2.resize(im,f3_shape)
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        
        p3= self.m3.predict(im,batch_size=1)
        
        im = cv2.imread(img)
        im = cv2.resize(im,f4_shape)
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        
        p4= np.array(self.convert(self.m4.predict(im,batch_size=1)))
        

        pr=0*p0+1.*p1+1.*p2+1.*p3+(2480./1000)*p4
        predict=pr/(3+2480./1000)
        return predict
    
    def process_result(self, path):
        return self.voting_Nmodels_batchsizetime(path)
    
