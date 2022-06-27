# -*- coding:utf-8 -*-
# @Time : 2022/6/27 21:58
# @Author : 西~南~北
# @File : test.py
# @Software: PyCharm
DATASET_DIR = 'dataset/carplate'
classes = os.listdir(DATASET_DIR + "/ann/")

num_classes = len(classes)
img_rows, img_cols = 20, 20

if K.image_data_format() == 'channels_first':
    input_shape = [1, img_rows, img_cols]
else:
    input_shape = [img_rows, img_cols, 1]
model_char = Sequential()
model_char.add(Conv2D(32, kernel_size=(3, 3),
                      activation='relu',
                      input_shape=input_shape))
model_char.add(Conv2D(64, (3, 3), activation='relu'))
model_char.add(MaxPooling2D(pool_size=(2, 2)))
model_char.add(Dropout(0.25))
model_char.add(Flatten())
model_char.add(Dense(128, activation='relu'))
model_char.add(Dropout(0.5))
model_char.add(Dense(num_classes, activation='softmax'))

model_char.compile(loss=keras.losses.categorical_crossentropy,
                   optimizer=keras.optimizers.Adadelta(),
                   metrics=['accuracy'])
model_char.load_weights("char_cnn/char_cnn.h5")


def extend_channel(data):
    if K.image_data_format() == 'channels_first':
        data = data.reshape(data.shape[0], 1, img_rows, img_cols)
    else:
        data = data.reshape(data.shape[0], img_rows, img_cols, 1)

    return data


chars2 = []
for ch in chars:
    chars2.append(transform.resize(ch, [img_rows, img_cols]))

chars2 = np.stack(chars2)
ys = np.unique(classes)

p_test = model_char.predict_classes(extend_channel(chars2))
print(' '.join([ys[p_test[i]] for i in range(len(p_test))]))