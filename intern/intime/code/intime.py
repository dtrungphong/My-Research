from tensorflow.keras import Model, applications, models
from tensorflow.keras import regularizers, layers
import numpy as np
import os
import cv2


class PredictionModel:
    def __init__(self):
        Input_Shape=(int(299*1.25),int(299*1.25),3)
        ww = './weight_cut_data'
        w1 = '1a'
        w2 = '2a'
        w3 = '3a'
        w4 = '4a'
        num_disease = 9
        Pretrained_Model_1 = applications.inception_v3.InceptionV3(input_shape=Input_Shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        model_1 = models.Sequential()
        model_1.add(Pretrained_Model_1)
        model_1.add(layers.GlobalAveragePooling2D()) # note Flatten())
        model_1.add(layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
        model_1.add(layers.Dropout(0.5))
        model_1.add(layers.Dense(num_disease, activation='softmax', kernel_regularizer=regularizers.l2(0.01)))
        model_1.load_weights(os.path.join(ww,w1,'intime_model_2020-03-28_20:10:01.h5'))
        self.m1 = model_1
        print('xong 1')
        
        Pretrained_Model_2 = applications.inception_v3.InceptionV3(input_shape=Input_Shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        model_2 = models.Sequential()
        model_2.add(Pretrained_Model_2)
        model_2.add(layers.GlobalAveragePooling2D()) # note Flatten())
        model_2.add(layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
        model_2.add(layers.Dropout(0.5))
        model_2.add(layers.Dense(num_disease, activation='softmax', kernel_regularizer=regularizers.l2(0.01)))
        model_2.load_weights(os.path.join(ww,w2,'intime_model_2020-03-30_09:33:12.h5'))
        self.m2 = model_2
        print('xong 2')
        
        Pretrained_Model_3 = applications.inception_v3.InceptionV3(input_shape=Input_Shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        model_3 = models.Sequential()
        model_3.add(Pretrained_Model_3)
        model_3.add(layers.GlobalAveragePooling2D()) # note Flatten())
        model_3.add(layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
        model_3.add(layers.Dropout(0.5))
        model_3.add(layers.Dense(num_disease, activation='softmax', kernel_regularizer=regularizers.l2(0.01)))
        model_3.load_weights(os.path.join(ww,w3,'Intime_mode_mix_b+o+cut_fold_3_checkpointv3_2-49-0.8568.hdf5'))
        self.m3 = model_3
        print('xong 3')
        
        
        Pretrained_Model_4 = applications.inception_v3.InceptionV3(input_shape=Input_Shape, #note
                                                     include_top=False, 
                                                     input_tensor=None, #note
                                                     weights=None)
        model_4 = models.Sequential()
        model_4.add(Pretrained_Model_4)
        model_4.add(layers.GlobalAveragePooling2D()) # note Flatten())
        model_4.add(layers.Dense(1024, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
        model_4.add(layers.Dropout(0.5))
        model_4.add(layers.Dense(num_disease, activation='softmax', kernel_regularizer=regularizers.l2(0.01)))
        model_4.load_weights(os.path.join(ww,w4,'Intime_mode_mix_b+o+cut_fold_4_checkpointv3_2-48-0.8922.hdf5'))
        self.m4 = model_4
        print('xong 4')
        self.number_of_models= (1.1052306/0.94287103**1.0483404*0.891731)
        
    def voting_Nmodels_batchsizetime(self,img):
        #to transform for voting
        im = cv2.imread(img)
        im = cv2.resize(im,(373, 373))
        im = im /255.
        im = im[:,:,[2,1,0]]
        im = np.expand_dims(im,axis = 0)
        p1= self.m1.predict(im,batch_size=1)
        p2= self.m2.predict(im,batch_size=1)
        p3= self.m3.predict(im,batch_size=1)
        p4= self.m4.predict(im,batch_size=1)
        
        pr=1.0006962*p1+0.999734*p2+1.0001273*p3+0.9993668*p4
        predict=pr/(1.0006962+0.999734+1.0001273+0.9993668)
        return predict
    
    def process_result(self, path):
        return self.voting_Nmodels_batchsizetime(path)
    
#'Balanitis' =0
# 'Genital_Contact_Allergy' =1
# 'Genital_Psoriasis' =2
# 'Genital_Warts' =3
# 'Lichen_Sclerosus'=4
# 'Scabies'=5
# 'Tinea_Cruris'=6
# 'Trichomoniasis'=7
# 'Vagina_Discharge'=8