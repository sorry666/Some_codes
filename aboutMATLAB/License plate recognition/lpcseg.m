%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
% �ַ��ָ�ģ���㷨  
% ��λ���к�Ĳ�ɫ����ͼ�񣭣��Ҷȣ�����ֵ������ͳһ���ڵװ��֣���ȥ�����±߿�  
% �����и����С��Χ�����˲�������̬ѧ�������ָ��7���ַ�  
  
% ȥ�����±߿��㷨��  
% 1.�ڰ�����С����ֵ����Ϊ������2.�������ߴ���ĳ��ֵ��ð��߱���Ϊ�Ǳ���  
% 3.���а�ɫ������ֵ����Ϊ�Ǳ���������FLAG��ֵ��  
% 4.�������ϴ�����ϱ�1/2 �����������������ߣ���Ϊ�ú�������Ϊ���������±�1/2 �����������������ߣ���Ϊ�ú�������Ϊ����  
% ��һ��Ϊ 40*20 ������ϵͳ�����й�һ��Ϊ 32*16 ���˴�����ʾ����  
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
figure(1),subplot(3,2,1),imshow(dw),title('��λ���к�Ĳ�ɫ����ͼ��')  
imwrite(dw,'dw.jpg');  
[filename,filepath]=uigetfile('dw.jpg','����һ����λ�ü���ĳ���ͼ��');  
jpg=strcat(filepath,filename);  
a=imread(jpg);  
%figure(1);subplot(3,2,1),imshow(a),title('1.��λ���к�Ĳ�ɫ����ͼ��')  
b=rgb2gray(a);  
imwrite(b,'2.���ƻҶ�ͼ��.jpg');  
figure(1);subplot(3,2,2),imshow(b),title('2.���ƻҶ�ͼ��')  
g_max=double(max(max(b)));  
g_min=double(min(min(b)));  
T=round(g_max-(g_max-g_min)/3); % T Ϊ��ֵ������ֵ  
[m,n]=size(b);  
d=(double(b)>=T);  % d:��ֵͼ��  
imwrite(d,'3.���ƶ�ֵͼ��.jpg');  
figure(1);subplot(3,2,3),imshow(d),title('3.���ƶ�ֵͼ��')  
  
% ��ת  
rotate=0;  
d=imread('3.���ƶ�ֵͼ��.jpg');  
bw=edge(d);  
[m,n]=size(d);  
theta=1:179;  
% bw ��ʾ��Ҫ�任��ͼ��theta ��ʾ�任�ĽǶ�  
% ����ֵ r ��ʾ�����а����˶�Ӧ�� theta��ÿһ���Ƕȵ� Radon �任���  
% ���� xp ������Ӧ���� x�������  
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
        else  % ���� x Ϊ��ֵ  
            x=90; % ��ʵ���ǲ���ת  
        end  
        d=imrotate(d,abs(90-x)); % ��תͼ��  
        rotate=1;  
    end  
end  
imwrite(d,'4.Radon �任��ת��Ķ�ֵͼ��.jpg');  
figure(1),subplot(3,2,4),imshow(d),title('4.Radon �任��ת��Ķ�ֵͼ��')  
  
% ͳһ���׵׺���  
[m,n]=size(d);  
% flag=0 ��ʾԭ�����ǰ׵׺��֣������ʾԭ���Ǻڵװ���  
flag=0;  
c=d([round(m/3):m-round(m/3)],[round(n/3):n-round(n/3)]);  
if sum(sum(c))/m/n*9>0.5  
    d=~d;flag=1;  
end  
% �Է�ɫ���ͼ��Ԥ�������м���Ϊ�׵���Ϊ�Ǳ���  
if flag==1  
    for j=1:n  
        if sum(sum(d(:,j)))/m>=0.95  
            d(:,j)=0;  
        end  
    end  
    % �����ϴ�����ͼ���ٴ���  
    % ����� 1/2 ���������������ߣ���Ϊ�ú������Ϊ���������ұ� 1/2 ���������������ߣ���Ϊ�ú����ұ��Ǳ���  
    % ��� 1/2  
    jj=0;  
    for j=1:round(n/2)  
        if sum(sum(d(:,[j:j+0])))==0  
            jj=j;  
        end  
    end  
    d(:,[1:jj])=0;  
    % �ұ� 1/2  
    for j=n:-1:round(n/2)  
        if sum(sum(d(:,[j-0:j])))==0  
            jj=j;  
        end  
    end  
    d(:,[jj:n])=0;  
end  
imwrite(d,'5.ͳһ�ɺڵװ���.jpg');  
figure(1),subplot(3,2,5),imshow(d),title('5.����ɫͳһ�ɺڵװ���')  
figure(2),subplot(5,1,1),imshow(d),title('5.�ڵװ��ֵĶ�ֵ����ͼ��')  
  
% ȥ�����±߿�  
% STEP 1  �ڰ�����С����ֵ����Ϊ����  
% ���� 2/5  
y1=10;  % y1: ������ֵ  
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
% ���� 2/5  
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
imwrite(d,'6.�ڰ�����С��ĳ��ֵ��������Ϊ����.jpg');  
figure(2),subplot(5,1,2),imshow(d),title('6.�ڰ�����С��ĳ��ֵ��������Ϊ����')  
  
% STEP 2  ���а�ɫ������ֵ����Ϊ�Ǳ��������� FLAG ��ֵ  
% ���� 2/5  
y2=round(n/2); % y2: ��ֵ  
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
% ���� 2/5  
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
imwrite(d,'7.���а�ɫ����������ĳ��ֵ����б���Ϊ�Ǳ���.jpg');  
figure(2),subplot(5,1,3),imshow(d),title('7.���а�ɫ����������ĳ��ֵ����б���Ϊ�Ǳ���')  
% STEP 3  ���а�ɫ������ֵ����Ϊ�Ǳ��������� FLAG ��ֵ  
% ���� 2/5  
y2=round(n/2); % y2: ��ֵ  
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
% ���� 2/5  
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
imwrite(d,'8.���а�ɫ����������ĳ��ֵ����б���Ϊ�Ǳ���.jpg');  
figure(2),subplot(5,1,4),imshow(d),title('8.���а�ɫ����������ĳ��ֵ����б���Ϊ�Ǳ���')  
%  STEP 4 �������ϴ�����ϱ� 1/2 �����������������ߣ���Ϊ�ú�������Ϊ������  
% ���±� 1/2 �����������������ߣ���Ϊ�ú�������Ϊ����  
% �ϱ� 1/2  
for i=1:round(m/2)  
    if sum(sum(d([i,i+0],:)))==0  
        ii=i;  
    end  
end  
d([1:ii],:)=0;  
% �±� 1/2  
for i=m:-1:round(m/2)  
    if sum(sum(d([i-0:i],:)))==0  
        ii=i;  
    end  
end  
d([ii:m],:)=0;  
imwrite(d,'9.���������������ߺ�Ľ��.jpg');  
figure(2),subplot(5,1,5),imshow(d),title('9.���������������ߺ�Ľ��')  
  
% ����ת  
if rotate==1  
    d=imrotate(d,-abs(x-90));  
end  
imwrite(d,'10.����תȥë�̺�.jpg');  
figure(3),subplot(3,2,1),imshow(d),title('10.����תȥë�̺�')  
% �и��С��Χ  
d=qiege(d);e=d;  
imwrite(d,'11.�и��С��Χ.jpg');  
figure(3),subplot(3,2,2),imshow(d),title('11.�и��С��Χ')  
figure(3),subplot(3,2,3),imshow(d),title('11.��ֵ�˲�ǰ')  
  
% �˲�  
h=fspecial('average',3);  
d=im2bw(round(filter2(h,d)));  
imwrite(d,'12.��ֵ�˲���.jpg');  
figure(3),subplot(3,2,4),imshow(d),title('12.��ֵ�˲���')  
  
% ĳЩͼ����в���  
% ���ͻ�ʴ  
% se=strel('square',3);  % ʹ��һ��3X3�������ν��Ԫ�ض���Դ�����ͼ���������  
% 'line'/'diamond'/'ball'...  
se=eye(2); % eye(n) returns the n-by-n identity matrix ��λ����  
[m,n]=size(d);  
if bwarea(d)/m/n>=0.365  
    d=imerode(d,se);  
elseif bwarea(d)/m/n<=0.235  
    d=imdilate(d,se);  
end  
imwrite(d,'13.���ͻ�ʴ�����.jpg');  
figure(3),subplot(3,2,5),imshow(d),title('13.���ͻ�ʴ�����')  
  
% Ѱ�����������ֵĿ飬�����ȴ���ĳ��ֵ������Ϊ�ÿ��������ַ���ɣ���Ҫ�ָ�  
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
        d(:,k1+num+5)=0;  % �ָ�  
    end  
end  
% ���и�  
d=qiege(d);  
% �и�� 7 ���ַ�  
y1=10;y2=0.25;flag=0;word1=[];  
while flag==0  
    [m,n]=size(d);  
    left=1;wide=0;  
    while sum(d(:,wide+1))~=0  
        wide=wide+1;  
    end  
    if wide<y1   % ��Ϊ��������  
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
% �ָ���ڶ����ַ�  
[word2,d]=getword(d);  
% �ָ���������ַ�  
[word3,d]=getword(d);  
% �ָ�����ĸ��ַ�  
[word4,d]=getword(d);  
% �ָ��������ַ�  
[word5,d]=getword(d);  
% �ָ���������ַ�  
[word6,d]=getword(d);  
% �ָ�����߸��ַ�  
[word7,d]=getword(d);  
subplot(5,7,1),imshow(word1),title('1');  
subplot(5,7,2),imshow(word2),title('2');  
subplot(5,7,3),imshow(word3),title('3');  
subplot(5,7,4),imshow(word4),title('4');  
subplot(5,7,5),imshow(word5),title('5');  
subplot(5,7,6),imshow(word6),title('6');  
subplot(5,7,7),imshow(word7),title('7');  
[m,n]=size(word1);  
% ����ϵͳ�����й�һ����СΪ 32*16,�˴���ʾ  
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
imwrite(word1,'14.�ַ��ָ��һ���� 1.jpg');  
imwrite(word2,'14.�ַ��ָ��һ���� 2.jpg');  
imwrite(word3,'14.�ַ��ָ��һ���� 3.jpg');  
imwrite(word4,'14.�ַ��ָ��һ���� 4.jpg');  
imwrite(word5,'14.�ַ��ָ��һ���� 5.jpg');  
imwrite(word6,'14.�ַ��ָ��һ���� 6.jpg');  
imwrite(word7,'14.�ַ��ָ��һ���� 7.jpg');  
  