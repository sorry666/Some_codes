//划痕检测  
void CheckScratch()  
{  
    Mat image, imagemen, diff, Mask;  
    image = imread("C:\\Users\\Tony\\Desktop\\blemish.bmp");  
  
  
    //均值模糊  
    blur(image, imagemen, Size(13, 13));  
  
    //图像差分  
    subtract(imagemen, image, diff);  
  
    //同动态阈值分割dyn_threshold  
    threshold(diff, Mask, 50, 255, THRESH_BINARY_INV);  
    imshow("imagemean", imagemen);  
    waitKey(0);  
    imshow("diff", diff);  
    waitKey(0);  
    imshow("Mask", Mask);  
    waitKey(0);  
    Mat imagegray;  
    cvtColor(Mask, imagegray, CV_RGB2GRAY);  
    vector<vector<Point>> contours;  
    vector<Vec4i>hierarchy;  
    findContours(imagegray, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));  
    Mat drawing = Mat::zeros(Mask.size(), CV_8U);  
    int j = 0;  
  
    for (int i = 0; i < contours.size(); i++)  
    {  
        Moments moms = moments(Mat(contours[i]));  
        double area = moms.m00;//零阶矩即为二值图像的面积  double area = moms.m00;零阶距.m00表示轮廓的面积，.m10为轮廓重心  
  
        //如果面积超出了设定的范围，则不再考虑该斑点   
        if (area > 20 && area < 1000)  
        {  
            drawContours(drawing, contours, i, Scalar(255), FILLED, 8, hierarchy, 0, Point());  
            j = j + 1;  
  
        }  
    }  
  
    Mat element15(3, 3, CV_8U, Scalar::all(1));  
    Mat close;  
    morphologyEx(drawing, close, MORPH_CLOSE, element15);  
    imshow("drawing", drawing);  
    waitKey(0);  
    vector<vector<Point> > contours1;  
    vector<Vec4i> hierarchy1;  
    findContours(close, contours1, hierarchy1, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));  
    imshow("close", close);  
    waitKey(0);  
    j = 0;  
    int m = 0;  
    for (int i = 0; i < contours1.size(); i++)  
    {  
        Moments moms = moments(Mat(contours1[i]));  
        double area = moms.m00;//零阶矩即为二值图像的面积  double area = moms.m00;  
        //如果面积超出了设定的范围，则不再考虑该斑点    
  
        double area1 = contourArea(contours1[i]);  
        if (area > 50 && area < 100000)  
        {  
            drawContours(image, contours1, i, Scalar(0, 0, 255), FILLED, 8, hierarchy1, 0, Point());  
            j = j + 1;  
  
        }  
        else if (area >= 0 && area <= 50)  
        {  
            drawContours(image, contours1, i, Scalar(255, 0, 0), FILLED, 8, hierarchy1, 0, Point());  
            m = m + 1;  
  
        }  
    }  
  
    char t[256];  
    sprintf_s(t, "%01d", j);  
    string s = t;  
    string txt = "Long NG : " + s;  
    putText(image, txt, Point(20, 30), CV_FONT_HERSHEY_COMPLEX, 1,  
        Scalar(0, 0, 255), 2, 8);  
  
    sprintf_s(t, "%01d", m);  
    s = t;  
    txt = "Short NG : " + s;  
    putText(image, txt, Point(20, 60), CV_FONT_HERSHEY_COMPLEX, 1,  
        Scalar(255, 0, 0), 2, 8);  
    imwrite("C:\\Users\\Tony\\Desktop\\result.bmp", image);  
}  