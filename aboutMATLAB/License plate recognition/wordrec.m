%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
% ��ţ�A-Z �ֱ�Ϊ 1-26; 0-9 �ֱ�Ϊ 27-36;  
% ��  ��  ��  ��  ��  ��  ��  ��  ³  ԥ  ��  ��  ��  ��  ��  ��  ��  
% ��  ��  ��  ��  ��  ̨  ��  ��  ��  ��  ��  ��  ��  ��  ��  ��  ��  
% 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59   
% 60 61 62 63 64 65 66 67 68 69 70  
% ʹ�� BP ����  
function word=wordrec(xx)  
% clear  
% clc  
load bp net;  
xx=im2bw(xx);xx=double(xx(:));  % ʹ����ֵ��ͼ��ת��Ϊ������ͼ��  
a=sim(net,xx);  % ��һ��Ϊ�� 32*16,�� xx=512*1;  
[val,num]=max(a);  
if num<=26  
    word=char(double('A')+num-1);  
elseif num<=36  
    word=char(double('0')+num-1-26);  
else  
    switch num  
        case 37  
            word='��';  
        case 38  
            word='��';  
        case 39  
            word='��';  
        case 40  
            word='��';  
        case 41  
            word='��';  
        case 42  
            word='��';  
        case 43  
            word='��';  
        case 44  
            word='��';  
        case 45  
            word='³';  
        case 46  
            word='ԥ';  
        case 47  
            word='��';  
        case 48  
            word='��';  
        case 49  
            word='��';  
        case 50  
            word='��';  
        case 51  
            word='��';  
        case 52  
            word='��';  
        case 53  
            word='��';  
        case 54  
            word='��';  
        case 55  
            word='��';  
        case 56  
            word='��';  
        case 57  
            word='��';  
        case 58  
            word='��';  
        case 59  
            word='̨';  
        case 60  
            word='��';  
        case 61  
            word='��';  
        case 62  
            word='��';  
        case 63  
            word='��';  
        case 64  
            word='��';  
        case 65  
            word='��';  
        case 66  
            word='��';  
        case 67  
            word='��';  
        case 68  
            word='��';  
        case 69  
            word='��';  
        case 70  
            word='��';  
    end  
end  