from keras.preprocessing.image import ImageDataGenerator 
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D 
from keras.layers import Activation, Dropout, Flatten, Dense 
from keras import backend as K

train_data_dir = 'C:\\Users\\hp pc\\Desktop\\HAND WASHING\\B.Tech Project\\8 Steps'


print(train_data_dir)