%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
% 字符分割模块算法  
% 定位剪切后的彩色车牌图像－－灰度－－二值化－－统一到黑底白字－－去除上下边框  
% －－切割出最小范围－－滤波－－形态学处理－－分割出7个字符  
  
% 去除上下边框算法：  
% 1.黑白跳变小于阈值则被视为背景；2.连续白线大于某阈值则该白线被认为是背景  
% 3.单行白色大于阈值则被认为是背景，考虑FLAG的值；  
% 4.做完以上处理后，上边1/2 中搜索连续两条黑线，认为该黑线以上为背景；在下边1/2 中搜索连续两条黑线，认为该黑线以下为背景  
% 归一化为 40*20 ，商用系统程序中归一化为 32*16 ，此处仅演示作用  
function [d]=lpcseg(jpg)  
I=imread('car1.jpg');  
I1=rgb2gray(I);  
I2=edge(I1,'robert',0.15,'both');  
se=[1;1;1];  
I3=imerode(I2,se);  
se=strel('rectangle',[25,25]);  
I4=imclose(I3,se);  
I5=bwareaopen(I4,2000);  
[y,x,z]=size(I5);  
myI=double(I5);  
tic  
 white_y=zeros(y,1);  
 for i=1:y  
    for j=1:x  
             if(myI(i,j,1)==1)   
                white_y(i,1)= white_y(i,1)+1;   
            end    
     end         
 end  
 [temp MaxY]=max(white_y);  
 PY1=MaxY;  
 while ((white_y(PY1,1)>=5)&&(PY1>1))  
        PY1=PY1-1;  
 end      
 PY2=MaxY;  
 while ((white_y(PY2,1)>=5)&&(PY2<y))  
        PY2=PY2+1;  
 end  
 IY=I(PY1:PY2,:,:);  
 white_x=zeros(1,x);  
 for j=1:x  
     for i=PY1:PY2  
            if(myI(i,j,1)==1)  
                white_x(1,j)= white_x(1,j)+1;                 
            end    
     end         
 end  
    
 PX1=1;  
 while ((white_x(1,PX1)<3)&&(PX1<x))  
       PX1=PX1+1;  
 end      
 PX2=x;  
 while ((white_x(1,PX2)<3)&&(PX2>PX1))  
        PX2=PX2-1;  
 end  
 PX1=PX1-1;  
 PX2=PX2+1;  
  dw=I(PY1:PY2-8,PX1:PX2,:);  
 t=toc;   
figure(1),subplot(3,2,1),imshow(dw),title('定位剪切后的彩色车牌图像')  
imwrite(dw,'dw.jpg');  
[filename,filepath]=uigetfile('dw.jpg','输入一个定位裁剪后的车牌图像');  
jpg=strcat(filepath,filename);  
a=imread(jpg);  
%figure(1);subplot(3,2,1),imshow(a),title('1.定位剪切后的彩色车牌图像')  
b=rgb2gray(a);  
imwrite(b,'2.车牌灰度图像.jpg');  
figure(1);subplot(3,2,2),imshow(b),title('2.车牌灰度图像')  
g_max=double(max(max(b)));  
g_min=double(min(min(b)));  
T=round(g_max-(g_max-g_min)/3); % T 为二值化的阈值  
[m,n]=size(b);  
d=(double(b)>=T);  % d:二值图像  
imwrite(d,'3.车牌二值图像.jpg');  
figure(1);subplot(3,2,3),imshow(d),title('3.车牌二值图像')  
  
% 旋转  
rotate=0;  
d=imread('3.车牌二值图像.jpg');  
bw=edge(d);  
[m,n]=size(d);  
theta=1:179;  
% bw 表示需要变换的图像，theta 表示变换的角度  
% 返回值 r 表示的列中包含了对应于 theta中每一个角度的 Radon 变换结果  
% 向量 xp 包含相应的沿 x轴的坐标  
[r,xp]=radon(bw,theta);  
i=find(r>0);  
[foo,ind]=sort(-r(i));  
k=i(ind(1:size(i)));  
[y,x]=ind2sub(size(r),k);  
[mm,nn]=size(x);  
if mm~=0 && nn~=0  
    j=1;  
    while mm~=1 && j<180 && nn~=0  
        i=find(r>j);  
        [foo,ind]=sort(-r(i));  
        k=i(ind(1:size(i)));  
        [y,x]=ind2sub(size(r),k);  
        [mm,nn]=size(x);  
        j=j+1;  
    end  
    if nn~=0  
        if x   % Enpty matrix: 0-by-1 when x is an enpty array.  
            x=x;  
        else  % 可能 x 为空值  
            x=90; % 其实就是不旋转  
        end  
        d=imrotate(d,abs(90-x)); % 旋转图像  
        rotate=1;  
    end  
end  
imwrite(d,'4.Radon 变换旋转后的二值图像.jpg');  
figure(1),subplot(3,2,4),imshow(d),title('4.Radon 变换旋转后的二值图像')  
  
% 统一到白底黑字  
[m,n]=size(d);  
% flag=0 表示原来就是白底黑字，否则表示原来是黑底白字  
flag=0;  
c=d([round(m/3):m-round(m/3)],[round(n/3):n-round(n/3)]);  
if sum(sum(c))/m/n*9>0.5  
    d=~d;flag=1;  
end  
% 对反色后的图像预处理，整列几乎为白的认为是背景  
if flag==1  
    for j=1:n  
        if sum(sum(d(:,j)))/m>=0.95  
            d(:,j)=0;  
        end  
    end  
    % 对以上处理后的图像再处理  
    % 在左边 1/2 处找连续两条黑线，认为该黑线左边为背景；在右边 1/2 处找连续两条黑线，认为该黑线右边是背景  
    % 左边 1/2  
    jj=0;  
    for j=1:round(n/2)  
        if sum(sum(d(:,[j:j+0])))==0  
            jj=j;  
        end  
    end  
    d(:,[1:jj])=0;  
    % 右边 1/2  
    for j=n:-1:round(n/2)  
        if sum(sum(d(:,[j-0:j])))==0  
            jj=j;  
        end  
    end  
    d(:,[jj:n])=0;  
end  
imwrite(d,'5.统一成黑底白字.jpg');  
figure(1),subplot(3,2,5),imshow(d),title('5.背景色统一成黑底白字')  
figure(2),subplot(5,1,1),imshow(d),title('5.黑底白字的二值车牌图像')  
  
% 去除上下边框  
% STEP 1  黑白跳变小于阈值则被视为背景  
% 上面 2/5  
y1=10;  % y1: 跳变阈值  
for i=1:round(m/5*2)  
    count=0;jump=0;temp=0;  
    for j=1:n  
        if d(i,j)==1  
            temp=1;  
        else  
            temp=0;  
        end  
        if temp==jump  
            count=count;  
        else  
            count=count+1;  
        end  
        jump=temp;  
    end  
    if count<y1  
        d(i,:)=0;  
    end  
end  
% 下面 2/5  
for i=3*round(m/5):m  
    count=0;jump=0;temp=0;  
    for j=1:n  
        if d(i,j)==1  
            temp=1;  
        else  
            temp=0;  
        end  
        if temp==jump  
            count=count;  
        else  
            count=count+1;  
        end  
        jump=temp;  
    end  
    if count<y1  
        d(i,:)=0;  
    end  
end  
imwrite(d,'6.黑白跳变小于某阈值的行则被视为背景.jpg');  
figure(2),subplot(5,1,2),imshow(d),title('6.黑白跳变小于某阈值的行则被视为背景')  
  
% STEP 2  单行白色大于阈值则被认为是背景，考虑 FLAG 的值  
% 上面 2/5  
y2=round(n/2); % y2: 阈值  
for i=1:round(m/5*2)  
    if flag==0  
        temp=sum(d(i,:));y2=round(n/2);  
        if temp>y2  
            d(i,:)=0;  
        end  
    else  
        temp=m-sum(d(i,:));y2=m-round(n/2);  
        if temp<y2  
            d(i,:)=0;  
        end  
    end  
end  
% 下面 2/5  
for i=round(3*m/5):m  
    if flag==0  
        temp=sum(d(i,:));y2=round(n/2);  
        if temp>y2  
            d(i,:)=0;  
        end  
    else  
        temp=m-sum(d(i,:));y2=m-round(n/2);  
        if temp<y2  
            d(i,:)=0;  
        end  
    end  
end  
imwrite(d,'7.单行白色点总数大于某阈值则该行被认为是背景.jpg');  
figure(2),subplot(5,1,3),imshow(d),title('7.单行白色点总数大于某阈值则该行被认为是背景')  
% STEP 3  单行白色大于阈值则被认为是背景，考虑 FLAG 的值  
% 上面 2/5  
y2=round(n/2); % y2: 阈值  
for i=1:round(m/5*2)  
    if flag==0  
        temp=sum(d(i,:));y2=round(n/2);  
        if temp>y2  
            d(i,:)=0;  
        end  
    else  
        temp=m-sum(d(i,:));y2=m-round(n/2);  
        if temp<y2  
            d(i,:)=0;  
        end  
    end  
end  
% 下面 2/5  
for i=round(3*m/5):m  
    if flag==0  
        temp=sum(d(i,:));y2=round(n/2);  
        if temp>y2  
            d(i,:)=0;  
        end  
    else  
        temp=m-sum(d(i,:));y2=m-round(n/2);  
        if temp<y2  
            d(i,:)=0;  
        end  
    end  
end  
imwrite(d,'8.单行白色点总数大于某阈值则该行被认为是背景.jpg');  
figure(2),subplot(5,1,4),imshow(d),title('8.单行白色点总数大于某阈值则该行被认为是背景')  
%  STEP 4 做完以上处理后，上边 1/2 中搜索连续两条黑线，认为该黑线以上为背景；  
% 在下边 1/2 中搜索连续两条黑线，认为该黑线以下为背景  
% 上边 1/2  
for i=1:round(m/2)  
    if sum(sum(d([i,i+0],:)))==0  
        ii=i;  
    end  
end  
d([1:ii],:)=0;  
% 下边 1/2  
for i=m:-1:round(m/2)  
    if sum(sum(d([i-0:i],:)))==0  
        ii=i;  
    end  
end  
d([ii:m],:)=0;  
imwrite(d,'9.搜索上下两条黑线后的结果.jpg');  
figure(2),subplot(5,1,5),imshow(d),title('9.搜索上下两条黑线后的结果')  
  
% 反旋转  
if rotate==1  
    d=imrotate(d,-abs(x-90));  
end  
imwrite(d,'10.反旋转去毛刺后.jpg');  
figure(3),subplot(3,2,1),imshow(d),title('10.反旋转去毛刺后')  
% 切割处最小范围  
d=qiege(d);e=d;  
imwrite(d,'11.切割处最小范围.jpg');  
figure(3),subplot(3,2,2),imshow(d),title('11.切割处最小范围')  
figure(3),subplot(3,2,3),imshow(d),title('11.均值滤波前')  
  
% 滤波  
h=fspecial('average',3);  
d=im2bw(round(filter2(h,d)));  
imwrite(d,'12.均值滤波后.jpg');  
figure(3),subplot(3,2,4),imshow(d),title('12.均值滤波后')  
  
% 某些图像进行操作  
% 膨胀或腐蚀  
% se=strel('square',3);  % 使用一个3X3的正方形结果元素对象对创建的图像进行膨胀  
% 'line'/'diamond'/'ball'...  
se=eye(2); % eye(n) returns the n-by-n identity matrix 单位矩阵  
[m,n]=size(d);  
if bwarea(d)/m/n>=0.365  
    d=imerode(d,se);  
elseif bwarea(d)/m/n<=0.235  
    d=imdilate(d,se);  
end  
imwrite(d,'13.膨胀或腐蚀处理后.jpg');  
figure(3),subplot(3,2,5),imshow(d),title('13.膨胀或腐蚀处理后')  
  
% 寻找连续有文字的块，若长度大于某阈值，则认为该块有两个字符组成，需要分割  
d=qiege(d);  
[m,n]=size(d);  
figure,subplot(2,1,1),imshow(d),title(n)  
k1=1;k2=1;s=sum(d);j=1;  
while j~=n  
    while s(j)==0  
        j=j+1;  
    end  
    k1=j;  
    while s(j)~=0 && j<=n-1  
        j=j+1;  
    end  
    k2=j-1;  
    if k2-k1>=round(n/6.5)  
        [val,num]=min(sum(d(:,[k1+5:k2-5])));  
        d(:,k1+num+5)=0;  % 分割  
    end  
end  
% 再切割  
d=qiege(d);  
% 切割出 7 个字符  
y1=10;y2=0.25;flag=0;word1=[];  
while flag==0  
    [m,n]=size(d);  
    left=1;wide=0;  
    while sum(d(:,wide+1))~=0  
        wide=wide+1;  
    end  
    if wide<y1   % 认为是左侧干扰  
        d(:,[1:wide])=0;  
        d=qiege(d);  
    else  
        temp=qiege(imcrop(d,[1 1 wide m]));  
        [m,n]=size(temp);  
        all=sum(sum(temp));  
        two_thirds=sum(sum(temp([round(m/3):2*round(m/3)],:)));  
        if two_thirds/all>y2  
            flag=1;word1=temp;   % WORD 1  
        end  
        d(:,[1:wide])=0;d=qiege(d);  
    end  
end  
% 分割出第二个字符  
[word2,d]=getword(d);  
% 分割出第三个字符  
[word3,d]=getword(d);  
% 分割出第四个字符  
[word4,d]=getword(d);  
% 分割出第五个字符  
[word5,d]=getword(d);  
% 分割出第六个字符  
[word6,d]=getword(d);  
% 分割出第七个字符  
[word7,d]=getword(d);  
subplot(5,7,1),imshow(word1),title('1');  
subplot(5,7,2),imshow(word2),title('2');  
subplot(5,7,3),imshow(word3),title('3');  
subplot(5,7,4),imshow(word4),title('4');  
subplot(5,7,5),imshow(word5),title('5');  
subplot(5,7,6),imshow(word6),title('6');  
subplot(5,7,7),imshow(word7),title('7');  
[m,n]=size(word1);  
% 商用系统程序中归一化大小为 32*16,此处演示  
word1=imresize(word1,[40 20]);  
word2=wordprocess(word2);  
word3=wordprocess(word3);  
word4=wordprocess(word4);  
word5=wordprocess(word5);  
word6=wordprocess(word6);  
word7=wordprocess(word7);  
  
  
subplot(5,7,15),imshow(word1),title('1');  
subplot(5,7,16),imshow(word2),title('2');  
subplot(5,7,17),imshow(word3),title('3');  
subplot(5,7,18),imshow(word4),title('4');  
subplot(5,7,19),imshow(word5),title('5');  
subplot(5,7,20),imshow(word6),title('6');  
subplot(5,7,21),imshow(word7),title('7');  
imwrite(word1,'14.字符分割归一化后 1.jpg');  
imwrite(word2,'14.字符分割归一化后 2.jpg');  
imwrite(word3,'14.字符分割归一化后 3.jpg');  
imwrite(word4,'14.字符分割归一化后 4.jpg');  
imwrite(word5,'14.字符分割归一化后 5.jpg');  
imwrite(word6,'14.字符分割归一化后 6.jpg');  
imwrite(word7,'14.字符分割归一化后 7.jpg');  
  