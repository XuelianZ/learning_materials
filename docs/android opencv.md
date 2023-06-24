# 1.android opencv概述

## 1.1什么是opencv

OpenCV，全称Open Source Computer VisionLibrary，是基于C/C++编写的，是BSD开源许可的计算机视觉开发框架，其开源协议允许在学术研究与商业应用开发中免费使用它。OpenCV支持Windows、Linux、Mac OS、ioS与Android操作系统上的应用开发。
OpenCV Android SDK是OpenCV针对Android平台提供的开发工具包。Android应用开发一般采用Java或者Kotin语言进行，而OpenCV主要模块采用C、C++语言编制，因在android环境下可以通过JNI技术，实现JAVA或者Kotlin调用OpenCV算法模块的目的。
在android开发环境中配置好OpenCV以后，我们可以方便的调用各种API函数对计算机图像进行各种处理。OpenCV目前可以实现的功能有:图像处理、人机互动、图像分割、人脸检测、动作识别、运动跟踪、运动分析等等

1.2 opencv环境配置

1.2.1 opencv Android SDK

OpenCV-Android-SDK是配置OpenCV环境的重要部分。我们可以到[OpenCV的官网](https://opencv.org/releases/)进行下载，目前最新版本为4.7.0([opencv java doc)](https://opencv-java-tutorials.readthedocs.io/en/latest/index.html)。下载完的SDK是一个压缩包，解压后SDK的目录结构如下:

![image-20230523105206581](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523105206581.png)

![image-20230523105618613](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523105618613.png)



# 2.opencv基础

## 2.1 安装过程

### 2.1.1 安装步骤

文档忘保存，以下是一些重要步骤的截图

![image-20230523110623626](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523110623626.png)

![image-20230523134649661](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523134649661.png)

![image-20230523134812637](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523134812637.png)

![image-20230523135806687](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523135806687.png)



### 2.1.2 初始化代码

```java
private void initLoadOpencv() {
    boolean success = OpenCVLoader.initDebug();
    if( success) {
        Toast.makeText(this.getApplicationContext(),"Loading OpenCV Libraries...",Toast.LENGTH_LONG).show();
    }else {
        Toast.makeText(this.getApplicationContext(),"WARNING: Could not load OpencV Libraries !",Toast.LENGTH_LONG).show();
    }
}
```



## 2.2 一些像素操作





![image-20230523142624131](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523142624131.png)

![image-20230523142647438](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523142647438.png)

![image-20230523160640742](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523160640742.png)

![image-20230523172415732](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230523172415732.png)

应用代码

```java
public class MainActivity extends AppCompatActivity {

    Button button1, button2;
    ImageView iv1, iv2, iv3;

    Mat srcmat1, srcmat2, dstmat;
    Bitmap bitmap;

    @Override
    protected void onDestroy() {
        super.onDestroy();
        srcmat1.release();
        srcmat2.release();
        dstmat.release();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initLoadOpencv();
        initWidget();

        srcmat1 = new Mat();
        srcmat2 = new Mat();
        dstmat = new Mat();

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    srcmat1 = Utils.loadResource(MainActivity.this, R.drawable.dog1);// BGR
                    srcmat2 = Utils.loadResource(MainActivity.this, R.drawable.dog2);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                // 像素运算
                Core.subtract(srcmat1, srcmat2, dstmat);
                bitmap = Bitmap.createBitmap(dstmat.width(), dstmat.height(), Bitmap.Config.ARGB_8888);
                Utils.matToBitmap(dstmat, bitmap);
                iv3.setImageBitmap(bitmap);
            }
        });
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 颜色空间转换
                Bitmap bp = BitmapFactory.decodeResource(getResources(),R.drawable.dog1); // 读取dog1.jpg，直接是RGB
                Utils.bitmapToMat(bp, srcmat1);
                Imgproc.cvtColor(srcmat1, dstmat,Imgproc.COLOR_BGR2GRAY); //颜色空间转换

                //Imgproc.threshold(dstmat, dstmat,125,255,Imgproc.THRESH_BINARY) ;//二值化

                Imgproc.adaptiveThreshold(dstmat, dstmat,255, Imgproc.ADAPTIVE_THRESH_GAUSSIAN_C,Imgproc.THRESH_BINARY,13,1); // 自适应阈值二值化


                Utils.matToBitmap(dstmat,bp);
                iv3.setImageBitmap(bp);

            }
        });

    }

    private void initWidget() {
        button1 = findViewById(R.id.button1);
        button2 = findViewById(R.id.button2);
        iv1 = findViewById(R.id.imageView1);
        iv2 = findViewById(R.id.imageView2);
        iv3 = findViewById(R.id.imageView3);
    }

    private void initLoadOpencv() {
        boolean success = OpenCVLoader.initDebug();
        if( success) {
            Toast.makeText(this.getApplicationContext(),"Loading OpenCV Libraries...",Toast.LENGTH_LONG).show();
        }else {
            Toast.makeText(this.getApplicationContext(),"WARNING: Could not load OpencV Libraries !",Toast.LENGTH_LONG).show();
        }
    }
}
```

## 2.3几何图形绘制

基础参考：[OpenCV4.3 Java 编程入门：绘制基本图形](https://gnetna.blog.csdn.net/article/details/124364362?spm=1001.2014.3001.5502)

绘制效果如下

![image-20230525103641164](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525103641164.png)



### 2.3.1直线绘制

几何图形绘制主要使用ImgProc类里的line、rectangle、polylines、circle、ellipse等函数，也可以使用putText函数绘制文字。图形绘制函数一般在APP中起到画面标注的功能。

```java
/**
     * 绘制两点之间的线段；
     *
     * 线段会被图像边界截断，粗线用圆形端点绘制，防锯齿线条使用高斯滤波绘制。
     * 
     * @param img 图像
     * @param pt1 线段起点
     * @param pt2 线段终点
     * @param color 颜色
     * @param thickness 线宽
     * @param lineType 类型：FILLED(-1)，LINE_4(4)，LINE_8(8)，LINE_AA(16)
     * @param shift 坐标中小数位数的移位.
     */
    public static void line(Mat img, Point pt1, Point pt2, Scalar color, int thickness, int lineType, int shift);
```

比如我们要在画面的左下到右上画一条蓝色的宽度为4的直线，可以这样调用。

```java
//画直线
Imgproc.line(dstmat, new Point(0, dstmat.height()), new Point(dstmat.width(), 0), new Scalar(255, 0, 0), 4);
```

### 2.3.2矩形绘制

函数原型:

```java
/**
     * 绘制矩形
     * 
     * @param img 目标图像
     * @param pt1 顶点1
     * @param pt2 顶点1的对角点
     * @param color 颜色
     * @param thickness 线宽，负数为填充
     * @param lineType 线型
     * @param shift 点坐标中的小数位数
     */
    public static void rectangle(Mat img, Point pt1, Point pt2, Scalar color, int thickness, int lineType, int shift);
```

```java
//画矩形
Imgproc.rectangle(dstmat, new Point(10, 10), new Point(500, 500), new Scalar(255, 255, 0), 6);
```

### 2.3.3多边形绘制

```java
/**
     * 绘制多边图形
     *
     * @param img 目标图像
     * @param pts Array of polygonal curves.
     * @param isClosed Flag indicating whether the drawn polylines are closed or not. If they are closed,
     * the function draws a line from the last vertex of each curve to its first vertex.
     * @param color Polyline color.
     * @param thickness Thickness of the polyline edges.
     * @param lineType Type of the line segments. See #LineTypes
     * @param shift Number of fractional bits in the vertex coordinates.
     *
     * The function cv::polylines draws one or more polygonal curves.
     */
    public static void polylines(Mat img, List<MatOfPoint> pts, boolean isClosed, Scalar color, int thickness, int lineType, int shift);
```

```java
// 绘制多边形
MatOfPoint point1 = new MatOfPoint();
point1.fromArray(new Point(0, 0), new Point(30, 40), new Point(80, 150), new Point(100, 300), new Point(130, 280), new Point(180, 150), new Point(300, 500));
Imgproc.polylines(dstmat, Arrays.asList(point1), true, new Scalar(0, 255, 0), 6, Imgproc.LINE_8);
```

### 2.3.5文字绘制

函数原型:
static void putText(Mat img, String text，Point org,int fontFace,double fontScale，Scalar color，int thickness)﹔
参数:

- img，输入
- text，文字内容
-  org，文本字符串的左下角位置
- fontFace，字体类型，可取值

![image-20230524183821661](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230524183821661.png)



```java
//打印文字
Imgproc.putText(dstmat, "I will succeed", new Point(dstmat.width() / 2, dstmat.height() / 2), Imgproc.FONT_HERSHEY_COMPLEX, 2, new Scalar(255, 0, 0), 4);
```

### 2.3.6 绘制圆形

```java
/**
     *  绘制圆形
     * 
     * @param img 目标图像
     * @param center 中心点
     * @param radius 半径
     * @param color 颜色
     * @param thickness 整数表示边线宽度, 负数表示填充
     * @param lineType 边界线形
     * @param shift 中心点坐标和半径值中的小数位数
     */
    public static void circle(Mat img, Point center, int radius, Scalar color, int thickness, int lineType, int shift);
```

```java
// 绘制圆形
Point center = new Point(Math.random() * 400, Math.random() * 400);
int radius = (int) (Math.random() * 100);
Scalar color = new Scalar(Math.random() * 255, Math.random() * 255, Math.random() * 255);
Imgproc.circle(dstmat, center, radius, color, 6, Imgproc.LINE_8);
```

### 2.3.7  绘制椭圆

```java
/**
     *  绘制椭圆
     *
     * @param img 目标图像
     * @param center 椭圆中心
     * @param axes 轴半径
     * @param angle 旋转角
     * @param startAngle 椭圆弧的起始角（度）
     * @param endAngle 椭圆弧的终止角
     * @param color 颜色
     * @param thickness 宽度，负数表示填充
     * @param lineType 边线类型
     * @param shift 中心坐标和轴值中的小数位数
     */

 public static void ellipse(Mat img, Point center, Size axes, double angle, double startAngle, double endAngle, Scalar color, int thickness, int lineType, int shift);
```



下图解释了绘制蓝色圆弧的参数的含义。

![image-20230524190354748](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230524190354748.png)



```java
// 绘制 椭圆 圆弧
center = new Point(200, 200);
Size size = new Size(60, 120);
color = new Scalar(50);
Imgproc.ellipse(dstmat, center, size, 45, 0, 270, color, -1, Imgproc.LINE_8);
```

### 2.3.8 绘制箭头

```java
/**
     * 绘制有箭头的线段
     *
     * @param img 目标图像
     * @param pt1 起点
     * @param pt2 终点
     * @param color 颜色
     * @param thickness 线宽
     * @param line_type 线型
     * @param shift 点坐标中的小数位数。
     * @param tipLength 相对于箭头长度的箭头尖端长度
     */
    public static void arrowedLine(Mat img, Point pt1, Point pt2, Scalar color, int thickness, int line_type, int shift, double tipLength);
```

```java
// 绘制箭头
Imgproc.arrowedLine(dstmat, new Point(100, 100), new Point(450, 450), new Scalar(255, 0, 0), 8);
```

2.3.9 绘制图标

```java
/**
     * 在图像中的预定义位置绘制标记
     *
     * @param img 目标图像
     * @param position 绘制点的位置
     * @param color 颜色
     * @param markerType 标记类型
     * @param thickness 线宽
     * @param line_type 线型
     * @param markerSize 标记大小
     */
    public static void drawMarker(Mat img, Point position, Scalar color, int markerType, int markerSize, int thickness, int line_type);
```

```java
// 绘制图标
color = new Scalar(255, 0, 0);
Imgproc.drawMarker(dstmat, new Point(100, 200), color, 0, 40);
Imgproc.drawMarker(dstmat, new Point(300, 200), color, 1, 40);
Imgproc.drawMarker(dstmat, new Point(500, 200), color, 2, 40);
Imgproc.drawMarker(dstmat, new Point(750, 200), color, 3, 40);
Imgproc.drawMarker(dstmat, new Point(900, 200), color, 4, 40);
Imgproc.drawMarker(dstmat, new Point(1150, 200), color, 5, 40);
```



# 3.颜色形状识别案例

## 3.1案例概述

本案例是基于历年的全国职业院校技能大赛嵌入式开发赛项中的颜色形状模块，该模块在国赛中已经考核了多年。该模块主要是通过摄像头拍摄一张显示屏照片，显示屏上显示一张各种颜色形状的图片，选手通过Android APP识别出指定颜色、指定形状的数量。

![image-20230525104443643](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525104443643.png)

## 3.2 图像切割

### 3.2.1扩展基础知识

参考：[OpenCV4.3 Java 编程入门：Core 组件中的数据结构与方法](https://blog.csdn.net/antony1776/article/details/124213955?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168498332016800211568319%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=168498332016800211568319&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-4-124213955-null-null.268^v1^control&utm_term=opencv%20java%20%20Rect&spm=1018.2226.3001.4450)

> org.opencv.core 核心功能模块，包括：
>
> - OpenCV基本数据结构，
> - 动态数据结构，
> - 绘图函数，
> - 数组操作相关函数；
> - 辅助功能
>
> **Rect 类：矩形区域**
>
> Rect 类的成员变量有 x，y，width，height，分别为左上角点（Point）的坐标和矩形的宽和高。
>
> 常用的成员函数有：
>
> - size(): 返回 Size() 对象，表示矩形区域的大小；
>
> - tl(): 返回左上角的点对应的 Point 对象；
> - br(): 返回右下角的点对应的 Point 对象；
> - area() : 矩形的面积
> - contains(Point p): 判断给定的点，是否在矩形内；
> - inside(Rect rect)： 判断给定的矩形是否在本矩形内；
>
> ```java
> public class Rect {
>     public int x, y, width, height;
> 
>     public Rect(int x, int y, int width, int height) {
>         this.x = x;
>         this.y = y;
>         this.width = width;
>         this.height = height;
>     }
>     
>     public Rect() {
>         this(0, 0, 0, 0);
>     }
>     
>     public Rect(Point p1, Point p2) {
>         x = (int) (p1.x < p2.x ? p1.x : p2.x);
>         y = (int) (p1.y < p2.y ? p1.y : p2.y);
>         width = (int) (p1.x > p2.x ? p1.x : p2.x) - x;
>         height = (int) (p1.y > p2.y ? p1.y : p2.y) - y;
>     }
>     
>     public Rect(Point p, Size s) {
>         this((int) p.x, (int) p.y, (int) s.width, (int) s.height);
>     }
> 
> }
> ```

### 3.2.2 Mat的切割

OpenCV对图像切割的方法可以用Rect类实现。定义一个Rect类对象，构造时的参数为切割区域左上角坐标和切割区域的宽度和高度，共4个参数。函数原型如下:
Rect (int x,int y,int weight,int height) ;
然后用Mat (Mat mat，Rect rect);构造函数构造一个基于原图的部分切割图像。代码如下:

```java
Rect rect = new Rect(216,127,363,211);
dstmat = new Mat(srcmat,rect);
```

然后可将切割后的dstmat转换为bitmap在界面上进行显示。但是显示完会发现颜色和原图不一致(RGB BGR切换)。

```java
Imgproc.cvtColor(srcmat,srcmat,Imgproc.COLOR_BGR2RGB);
```

## 3.3颜色识别

教字图像处理中常用的采用模型是RGB(红，绿，蓝）模型和HSV(色调，饱和度，亮度)，RGB广泛应用于彩色监视器和彩色视频摄像机，我们平时的图片一般都是RGB模型。而HSV模型更符合人描述和解释颜色的方式，HSV的彩色描述对人来说是自然且非常直观的。

### 3.3.1 HSV模型

HSV模型中颜色的参数分别是:色调(H: hue)，饱和度(S: saturation)，亮度(V: value)。由A.R.Smith在1978年创建的一种颜色空间,也称六角锥体模型(Hexcone Model)。

- 色调(H: hue)︰用角度度量，取值范围为0°～360°，从红色开始按逆时针方向计算，红色为0°，绿色为120°,蓝色为240°。它们的补色是:黄色为60°，青色为180°,品红为300°;
- 饱和度(S: saturation) :取值范围为0.0~1.0，值越大，颜色越饱和。
- 亮度(V: value) :取值范围为0.0(黑色)～1.0(白色)。

![image-20230525144524202](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525144524202.png)



传统的RGB模型可以通过以下的公式转换为HSV模型。

![image-20230525144626926](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525144626926.png)



对于颜色识别来说一般我们只关注H分量的值就可以。在OpenCV中H被映射到(0，180)的区间内，S和V都被映射到(0，255)的区间内。常用颜色H分量值如下表

![image-20230525145013823](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525145013823.png)



OpenCV中可以通过cvtColor()函数进行RGB到HSV的转换

```java
cvtColor(Mat src,Mat dst,Imgproc.COLOR_RGB2HSV);
```

### 3.3.2颜色检测

确定了需要检测的颜色HSV值以后在OpenCV中可以通过inRange()函数进行颜色检测。inRange()也叫颜色分割函数。函数原型:

```java
public static void inRange(imgHSV，Scalar(iLowH，iLowS，iLow),Scalar(iHighH，iHighs，iHighv), imeThresholded);
```

参数:

- imgHSV :HSV颜色空间的源图
- Scalar Low:HSV范围下限. 
- Scalar High: HSV范围上限
- imgThresholded :输出的图像

这个函数的作用就是检测imgHSV图像的每一个像素是不是在Scalar(Low和Scalar(High)之间，如果是，这个像素就设置为255，并保存在imgThresholded图像中，否则为0。

代码:(以检测红色为例)

```java
// 通过阈值，将HSV图像根据色调，饱和度、亮度变为二值图
Core.inRange(hsvmat, new Scalar(160,90,90),new Scalar(179,255,255), hsvmat);
```

得到的结果是—张底色为黑色，指定颜色为白色的二值图像。



### 3.3.3开运算和闭运算

**开运算（背景为黑色，开运算去除背景噪点）**

开运算的原理是通过先进行腐蚀操作，再进行膨胀操作得到。我们在移除小的对象时候很有用(假设物品是亮色，前景色是黑色)。开运算可以去除噪声，消除小物体;在纤细点处分离物体;平滑较大物体的边界的同时并不明显改变其面积。比如在二值化图像没处理好的时候会有一些白色的噪点，可以通过开运算进行消除。

**闭运算（背景为黑色，闭运算去除前景噪点）**
闭运算是开运算的一个相反的操作，具体是先进行膨胀然后进行腐蚀操作。通常是被用来填充前景物体中的小洞，或者抹去前景物体上的小黑点。因为可以想象，其就是先将白色部分变大，把小的黑色部分挤掉，然后再将一些大的黑色的部分还原回来，整体得到的效里就是:抹去前吾物体卜的小里点了

在执行开运算和闭运算之前我们要确定一个运算核，这个运算核是一个小矩阵。腐蚀运算就是在整张图像上计算给定内核区域的局部最小值，用最小值替换对应的像素值。而膨胀运算就是在整张图像上计算给定内核区域的局部最大值，用最大值替换对应的像素值。
我们在优化图像时可以先执行开运算消除背景上的白色噪点，再运行闭运算消除前景上的黑色杂点。代码如下：

```java
// 开运算（去除背景（黑色）噪点）、闭运算 去除前景噪点
Mat kernel = Imgproc.getStructuringElement(Imgproc.MORPH_RECT,new Size(3,3));
Imgproc.morphologyEx(hsvmat,hsvmat, Imgproc.MORPH_OPEN, kernel);
Imgproc.morphologyEx(hsvmat, hsvmat, Imgproc.MORPH_CLOSE, kernel);
Utils.matToBitmap(hsvmat, bitmap);
v4.setImageBitmap(bitmap);
```



## 3.4轮廓识别

### 3.4.1轮廓识别

在OpenCV中,轮廓对应着一系列的点的集合,OpenCV提供了一个findContours()函数用来获得这些点的集合。函数原型如下;

```java
public static void findContours(Mat image,List<MatOfPoint> contours,Mat hierarchy ,int mode,int method)
```

- image 一个8位的单通道图像。非零像素被视为1，0像素仍然是0。图像被当作二进制来处理。如果使用的mode是RETR_CCOMP或者RETR_FLOODFILL，那么输入的图像类型也可以是32位单通道整型，即CV_32SC1
- contours 检测到的轮廓。一个MatOfPoint 保存一个轮廓，所有轮廓放在List 中。
- hierarchy 可选的输出。包含轮廓之间的联系。4通道矩阵，元素个数为轮廓数量。通道【0】～通道【3】对应保存:后一个轮廓下标，前一个轮廓下标，父轮廓下标，内嵌轮廓下标。如果没有后一个，前一个，父轮廓，内嵌轮廓，那么该通道的值为-1。

- mode轮廓检索模式。

![image-20230525163438285](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525163438285.png)

![image-20230525163712033](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525163712033.png)

```java
//找轮廓
Imgproc.findContours(hsvmat,contours,new Mat(),Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE);
Log.d("zxl:", "轮廓数量是："+contours.size());
```

### 3.4.2轮廓绘制

为了更直观的查看轮廓识别的效果，我们可以通过绘制轮廓函数drawContours()将识别到的轮廓绘制出来。函数原型如下:

```java
public static void drawContours(Mat src , List<MatOfpoint> contours,int contourIdx, Scalar & color,int thickness)
```

参数:

- src:目标图像
- contours:输入的所有轮廓(每个轮廓以点集的方式存储)
- contoursldx:指定绘制轮廓的下标(若为负数，则绘制所有轮廓)
- color:绘制轮廓的颜色
- thickness:绘制轮廓的线的宽度（若为负数，则填充轮廓内部)

轮廓线会直接绘制在src上，但是如果src是二值图的话轮廓线也会二值化，所以建议把轮廓线绘制在原图上。

```java
//绘制轮廓
//轮廓线会直接绘制在src上，但是如果src是二值图的话轮廓线也会二值化，所以建议把轮廓线绘制在原图上
Imgproc.drawContours(dstmat, contours, -1,new Scalar(0,0,255),8);
Utils.matToBitmap(dstmat,bitmap);
v4.setImageBitmap(bitmap);
```

## 3.5形状识别

### 3.5.1多边形拟合

​	轮廓点集合找到以后我们可以通过多边形拟合的方式来寻找由轮廓点所组成的多边形的顶点。approxPolyDP()函数功能是把一个连续光滑曲线折线化，对图像轮廓点进行多边形拟合。简单来说就是该函数是用一条具有较少顶点的曲线/多边形去逼近另—条具有较多顶点的曲线或多边形。approxPolyDP函数的原理如下:

1. 在曲线首尾两点A，B之间连接一条直线AB，该直线为曲线的弦;.
2. 得到曲线上离该直线段距离最大的点C，计算其与AB的距离d;
3. 比较该距离与预先给定的阈值threshold的大小，如果小于threshold，则该直线段作为曲线的近似，该段曲线处理完毕。
4. 如果距离大于阈值，则用C将曲线分为两段AC和BC，并分别对两段取信进行1~3的处理。
5. 当所有曲线都处理完毕时，依次连接各个分割点形成的折线，即可以作为曲线的近似。

![image-20230525171847607](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525171847607.png)

approxPolyDPO函数原型如下:

```java
public static void approxPolyDP( MatOfPoint2f curve, MatOfPoint2f approxCurve,double epsilon, boolean closed)
```

参数:

- curve:输入的轮廓点集合
- approxCurve:输出的轮廓点集合。最小包容指定点集，保存的是多边形的顶点。
- epsilon:拟合的精度，原始曲线和拟合曲线间的最大值
- closed:是否为封闭曲线。如果为true，表示逼近曲线为封闭曲线。

其中逼近精度epsilon可以手动指定，也可以通过curve轮廓点的个数进行计算。

```java
epsilon = a * Imgproc.arcLength(curve，true);
```

代码：

```java
int tri,rect,circle;
tri = rect = circle = 0;
for (int i = 0; i < contours.size(); i++) {
    MatOfPoint2f contour2f = new MatOfPoint2f(contours.get(i).toArray());
    double epsilon = 0.04 * Imgproc.arcLength(contour2f,true);
    MatOfPoint2f approxCurve = new MatOfPoint2f();
    Imgproc.approxPolyDP(contour2f, approxCurve, epsilon, true);
    if (approxCurve.rows() == 3){
        tri++;
    } else if (approxCurve.rows() == 4) {
        rect++;
    } else if (approxCurve.rows() > 4) {
        circle++;
    }
}
Log.d("ZXL:","三角形："+tri+" 四边形："+rect+" 圆形："+circle);
```

### 3.5.2形状的识别

#### 3.5.2.1顶点判断法

形状识别的方法有很多种，本案例采用最简单的一种就是直接根据多边形顶点的个数进行判断。这种方法最简单但精度不高，只能识别差别较大的几种形状。

![image-20230525172515673](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525172515673.png)

#### 3.5.2.2自身面积与外接矩形面积比

也可以采用自身面积与外接矩形面积比的方法，不同的形状的自身面积和外接矩形面积比通常区别较大。圆形的外接矩形面积与自身面积之比大约在85%左右，三角形通常在50%左右，矩形大约在95%。

#### 3.5.2.3信号分析法

使用Moments ()函数计算多边形的重点，求绕多边形一周重心到多边形轮廓线的距离。把距离值形成信号曲线图，我们可以看到不同的形状信号曲线图区别很大。信号分析法可以识别多种类型的多边形形状。![image-20230525173930441](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525173930441.png)

![image-20230525173858500](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525173858500.png)

![image-20230525173919088](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525173919088.png)

# 4.图形滤镜效果处理

## 4.1案例概述

本案例是对图片进行处理，实现灰度化、黑白、素描、怀旧、连环画、浮雕色等简单滤镜效果。通过本案例，学习对图片的灰度化，二值化、颜色取反、像素操作等方法。

## 4.2图像灰度化

在RGB模型中，如果R=G=B时，则彩色表示一种灰度颜色，其中R=G=B的值叫灰度值，因此，灰度图像每个像素只需一个字节存放灰度值（又称强度值、亮度值），灰度范围为0-255。
图像的灰度化一般作为图像的预处理步骤，为之后更复杂的图像处理做准备。本案例中将图像的灰度化作为简单的滤镜效果。



opencv实现图像的灰度化非常简单，有两种方法。

方法1:在读取图片的时候以灰度图像的方式读取图片

```java
lmgcodecs.imread(String filename , int flag)
```

- 通过imread方法获取的Mat对象。
  第一个参数表示文件路径
- 第二个参数表示加载图片类型，如下所示︰

> IMREAD_UNCHANGED =-1无改动
> IMREAD_GRAYSCALE =0单通道灰色图像
> IMREAD_COLOR=1三通道BGR图像
> IMREAD_ANYDEPTH =2不改变图像深度
> IMREAD_ANYCOLOR= 4以任何可能的颜色格式读取图像
> IMREADLOADGDAL=8使用Gdal驱动程序加载图像
> IMREADREDUCEDGRAYSCALE_2=16单通道灰色图像，宽高减半
> IMREADREDUCEDCOLOR_2 =17三通单BGR图像，宽高减半
>
> IMREADREDUCEDGRAYSCALE_4=32单通道灰色图像，宽高为原图1/4
> IMREADREDUCEDGRAYSCALE_8 = 64单通道灰色图像，宽高为原图1/8
> IMREADREDUCEDCOLOR_8= 65三通单BGR图像，宽高为原图1/8
> IMREADIGNOREORIENTATION = 128忽略EXIF的方向标志

```java
Mat src=Imgcodecs.imread(".limages/RGBimg.jpg",lmgcodecs.IlMREAD_GRAYSCALE);
```

方法2∶利用cvtColor方法转换

本案例中采用的即此方法。


```java
//灰度化方法
Bitmap RGB2Gray(Bitmap photo) {
    Mat mat = new Mat(); //创建mat对象
    Utils.bitmapToMat(photo,mat);//将图像由Bitmap转换为mat.
    Imgproc.cvtColor(mat,mat,Imgproc.COLOR_RGB2GRAY);//灰度转换
    Bitmap grayBitmap = Bitmap.createBitmap(photo.getWidth(),photo.getHeight(),Bitmap.Config.ARGB_8888);
    Utils.matToBitmap(mat, grayBitmap) ;
    mat.release();//释放内存
    return grayBitmap;}
```

在OpenCV的cvtColor方法实现灰度转换时，实际上采用的是加权平均算法。

## 4.3 图像自适应二值化

```java
// 二值化
Bitmap RGB2binaryzation(Bitmap photo) {
    Mat mat = new Mat(); //创建mat对象
    Utils.bitmapToMat(photo,mat);//将图像由Bitmap转换为mat.
    Imgproc.cvtColor(mat,mat,Imgproc.COLOR_RGB2GRAY);//灰度转换
    Imgproc.adaptiveThreshold(mat,mat,255,Imgproc.ADAPTIVE_THRESH_MEAN_C,Imgproc.THRESH_BINARY,15, 1);
    Bitmap threBitmap = Bitmap.createBitmap(photo.getWidth(),photo.getHeight(),Bitmap.Config.ARGB_8888);
    Utils.matToBitmap(mat, threBitmap) ;
    mat.release();//释放内存
    return threBitmap;}
```

## 4.4 图像怀旧风格

通过对rgb三个颜色分量的调整可以将照片处理成一种老照片的怀日风格。调整的公式如下:

![image-20230525220222907](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525220222907.png)

要完成对颜色分量的调整，可利用Mat的各种像素操作。
Mat是OpenCV中用来存储图像信息的内存对象，当通过ingcodes.imread ()方法从文件读入一个图像文件时，imread方法就会返回Mat对象实例，或者通过Utils.bitmatToMat()方法把bitmap转换成Mat对象。

### 4.4.1加载图像与读取基本信息

Mat对象中除了存储图像的像素数据以外，还包括了图像的其他属性，具体为宽、高、类型、通道、大小、深度等。当你需要这些信息时，可以通过相关的PI来获取这些基本图像属性。

- public int channels()返回通道数
- public int cols()返回矩阵的列数（宽度)
- public int rows()返回矩阵的行数（高度)
- public int dims()返回矩阵的维度
- public int type()返回矩阵的类型

在获取图像数据的时候，知道Mat的类型与通道数目关重要，根据Ma的类型与通道数目，开辟适当大小的内存空间，然后通过get方法就可以实现对每个像素点值的读取、修改。然后再通过put方法修改与Mat对应的数据部分。
通道表示每个点能存放多少个数，如RGB彩色图中的每个像素点有三个值，即三通道的。
常见的通道数目有1、3、4，分别对应于单通道、三通道、四通道，其中四通道中通常会有透明通道数据。

- 灰度图片单通道图像
- RGB彩色图像3通道图像
- 带Alph通道的RGB图像4通道图像

图像深度表示每个值由多少位来存储，是一个精度问题，一般图片是8bit (位)的，则深度是8。

![image-20230525220703096](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525220703096.png)

![image-20230525220843099](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525220843099.png)

图像深度与类型密切相关。其中，U表示无符号整型、s表示符号整型、f表示浮点数。
OpenCV通过mread来加载图像，默认时候加载的是三通道顺序为BGR的彩色图像。本案例中通过Utils.bitmapToMat方法加载图像，得到的图像类型为cv_8UC4,通道顺序为BGRA。其中CV表示计算机视觉、8表示八位、U表示无符号整型、4表示四通道。

### 4.4.2读取像素数据、修改、写入

对于CV_8UC4的Mat类型来说，对应的数据类型是byte;则先初始化byte数组p，用来存取每次读取出来的一个像素点的所有通道值，数组的
长度取决于图像通道数目。
从矩阵中读取像素数据采用get方法，写入像素数据采用put方法。get与put方法支持如下所示的几种图像Mat数据。

![image-20230525221138798](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525221138798.png)



```java
// 怀旧风格
Bitmap RGB2remini(Bitmap photo) {
    Mat mat = new Mat(); //创建mat对象
    Utils.bitmapToMat(photo, mat);//将图像由Bitmap转换为mat. BGRA
    int channel = mat.channels();
    int width = mat.cols();
    int height = mat.rows();

    byte[] p = new byte[channel];//保存一个点的像素

    Mat matdst = new Mat(mat.rows(), mat.cols(), CV_8UC4);

    int b, g, r;
    for (int i = 0; i < mat.height(); i++) {
        for (int j = 0; j < mat.width(); j++) {

            Log.d("zxl:", " " + i + " " + j + " of " + mat.height() + "  " + mat.width());
            mat.get(i, j, p);
            b = p[0] & 0xff;
            g = p[1] & 0xff;
            r = p[2] & 0xff;

            int B = (int) (0.272 * r + 0.534 * g + 0.131 * b);
            int G = (int) (0.349 * r + 0.686 * g + 0.168 * b);
            int R = (int) (0.393 * r + 0.769 * g + 0.189 * b);

            R = R > 255 ? 255 : (R < 0 ? 0 : R);
            G = G > 255 ? 255 : (G < 0 ? 0 : G);
            B = B > 255 ? 255 : (B < 0 ? 0 : B);

            p[0] = (byte) B;
            p[1] = (byte) G;
            p[2] = (byte) R;
            matdst.put(i, j, p);
        }
    }
    Bitmap reminiBitmap = Bitmap.createBitmap(matdst.width(), matdst.height(), Bitmap.Config.ARGB_8888);
    Utils.matToBitmap(matdst, reminiBitmap);
    mat.release();//释放内存
    matdst.release();
    return reminiBitmap;
}
```

## 4.5图像连环画滤镜处理

连环画的效果与图像怀旧处理后的效果相似,但连环画增大了图像的对比度,使整体明暗效果更强.调整的公式如下

![image-20230525224932116](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\image-20230525224932116.png)

图像连环画滤镜处理与怀旧滤镜处理相似，同样先加载图像与读取基本信息，再读取像素数据、修改、写入。只是在读取和写入时，从Mat中每次读取一行像素数据。

```java
// 怀旧风格
Bitmap RGB2cartoon(Bitmap photo) {
    Mat mat = new Mat(); //创建mat对象
    Utils.bitmapToMat(photo, mat);//将图像由Bitmap转换为mat. BGRA
    int channel = mat.channels();
    int width = mat.cols();
    int height = mat.rows();

    byte[] p = new byte[channel * mat.cols()];//保存一行像素点

    Mat matdst = new Mat(mat.rows(), mat.cols(), CV_8UC4);

    int b, g, r;
    for (int i = 0; i < mat.height(); i++) {
        mat.get(i, 0, p);//从每一行第0列开始读取一行的值
        for (int j = 0; j < mat.width(); j++) {
            int index = j * channel; //每个像素点有 b,g,r,a，四个通道
            Log.d("zxl:", " " + i + " " + j + " of " + mat.height() + "  " + mat.width());
            b = p[index] & 0xff;
            g = p[index + 1] & 0xff;
            r = p[index + 2] & 0xff;

            int B = Math.abs(b - g + b + r) * g / 256;
            int G = Math.abs(b - g + b + r) * r / 256;
            int R = Math.abs(g - b + g + r) * r / 256;

            R = R > 255 ? 255 : (R < 0 ? 0 : R);
            G = G > 255 ? 255 : (G < 0 ? 0 : G);
            B = B > 255 ? 255 : (B < 0 ? 0 : B);

            p[0] = (byte) B;
            p[1] = (byte) G;
            p[2] = (byte) R;
            matdst.put(i, j, p);
        }
    }
    Bitmap cartoonBitmap = Bitmap.createBitmap(matdst.width(), matdst.height(), Bitmap.Config.ARGB_8888);
    Utils.matToBitmap(matdst, cartoonBitmap);
    mat.release();//释放内存
    matdst.release();
    return cartoonBitmap;
}
```

## 4.6 浮雕滤镜处理

浮雕的算法为，用当前像素点的前一个像素点值减去后一个像素点值，所得结果加上128作为当前像素点的值。

原理的公式为︰current(i, j) = current(i+1,j+1) - current(i-1,j-1)+ 128

以上的操作可以形成浮雕的原因在于，由于图片中相邻点的颜色值是比较接近的，因此这样的算法处理之后，只有颜色的边沿区域，也就是相邻颜色差异较大的部分的结果才会比较明显，而其他平滑区域则值都接近128左右，也就是灰色，这样就具有了浮雕效果。

# 5 使用JavaCameraView

移动端的设备一般都有前置摄像头和后置摄像头，对有多个摄像头的移动设备来说，OpenCV会检测获取的摄像头数目，然后根据索引的不同来决定使用哪个摄像头完成指定的数据采集。对于Android移动端的相机调用和读取，OpenCV是把原来C++的部分和本地的Android SDK进行了整合，通过桥接的方式调用Android摄像头。JavaCameraview类是OpenCV中调用Android手机摄像头的接口类，支持以代码和XML Vtew配置的方式使用，可以在Android设备中使用摄像头完成拍照和预览功能。

5.4.3 JavaCameraView对象的获取及初始化操作
在Android平台中使用JavaCameraVview默认都是LANDSCAPE横屏显示模式，当改成PORTRAT竖屏显示时，就会发现预览发生逆时针方向90度的旋转，要正确显示图像，需要对预览帧进行实时处理，进行翻转，这样会导致帧率有所降低。本案例中的策略是简单设置显示，将窗口设置成横屏显示，同时在
layout中指定View的高度与宽度都是match_parent。

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000"
    android:orientation="horizontal"
    tools:context=".AiCameraActivity">

    <org.opencv.android.JavaCameraView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:id="@+id/javacameraview"
        android:layout_weight="1"

        ></org.opencv.android.JavaCameraView>
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/switch_camera"
        android:layout_gravity="center"
        android:background="@drawable/ic_camera2"
        android:layout_weight="1"
        android:text="111"></Button>


</LinearLayout>
```

```java
private void initWindowSettings() {
    getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);//全屏
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON); //常亮
    setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // 横屏

}
```

```java
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    initWindowSettings();//初始化窗口设置，包括全屏、横屏、常亮
    setContentView(R.layout.activity_ai_camera);
    cameraView = findViewById(R.id.javacameraview);
            switchBtn = findViewById(R.id.switch_camera);}
```

5.4.4权限的配置
本案例中需要调用摄像头，要配置相应权限。
·向AndroidManifest.xml文件中添加文本

```xml
<uses-permission android:name="android.permission.CAMERA"/>
```

。在Android6.0以上版本，由于授权方式升级，需在onCreate中添加以下代码
f(ContextCompat.checkSelfPermission(this，Manifest.permission.CAMERA)
!= PackageManager.PERMISSION_GRANTED){
ActivityCompat.requestPermissions(this,
new String[]{Manifest.permission.CAMERA}，1);
}else {
cameraview.setCameraPermissionGranted( ) ;
