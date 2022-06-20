# LPR_plus-

自动车牌识别系统
 
### 文件目录介绍

1. LPRGUI.py 本系统的界面文件
2. LPRGUI.ui qtdesigner生成的系统的界面文件
3. README.md 本系统的介绍文件
4. Run.py 本系统的启动文件
5. LLP.py 定位车牌的文件
6. Split_ch.py 字符分割文件
7. Ch_r.py 字符识别文件

### 功能介绍

1. 使用Python+OpenCV+PyTorch/Tensorflow，通过深度学习技术实现CCPD中国车牌公共数据库的CCPD-Base集中车牌的识别 要求系统带有界面和菜单。
2. 车牌识别系统要求功能如下：
    - 从图像中定位出车牌。
    - 能够从车牌中分割出字符。
    - 使用深度学习算法完成分割字符的识别。

### 相关背景及技术：

1. CCPD中国车牌公共数据库： 数据库网站：https://github.com/detectRecog/CCPD
2. 数据库使用教程：https://blog.csdn.net/LuohenYJ/article/details/117752120
3. 车牌定位：
    - 传统车牌定位：https://blog.csdn.net/qq_42722197/article/details/118688542
    - 基于深度学习的车牌定位：https://blog.csdn.net/qq_32892383/article/details/123088309
    - 使用YOLO3进行车牌定位：https://blog.csdn.net/sinat_20276189/article/details/106855068
4. 字符分割：
    - 车牌字符分割：https://www.cnblogs.com/silence-hust/p/4191853.html
    - 车牌识别算法—字符分割：https://blog.csdn.net/shanglianlm/article/details/78045170
5. 字符识别： TensorFlow MNIST手写数字识别案例深入剖析：https://www.jianshu.com/p/833989651210
6. 车牌字符识别小思路：https://blog.csdn.net/newlittlewhite/article/details/88219424
7. 车牌识别-Mask_RCNN定位车牌+手写方法分割字符+CNN单个字符识别：https://my.oschina.net/airxiechao/blog/2239875

### 系统要求：

1. 为了快速对系统进行评价，要求设计的车牌图像识别系统界面中包含“集中测试”菜单
    - 用户选择该菜单后能够对指定文件夹中的所有图像进行车牌检测和识别
    - 根据识别结果和图像车牌标签（每个图像仅含一张车牌）计算出识别率，并显示在界面上。
2. 选择了“集中测试”菜单后，用户可以通过“上一张”、“下一张”按钮查看该文件夹中每一张车牌的具体定位、分割和识别结果。






