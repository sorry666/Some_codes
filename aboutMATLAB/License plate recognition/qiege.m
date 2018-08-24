% 该子程序用于切割出最小范围  
function e=qiege(d)  
[m,n]=size(d);  
top=1;bottom=m;left=1;right=n;   % init  
while sum(d(top,:))==0 && top<=m  
    top=top+1;  
end  
while sum(d(bottom,:))==0 && bottom>=1  
    bottom=bottom-1;  
end  
while sum(d(:,left))==0 && left<=n  
    left=left+1;  
end  
while sum(d(:,right))==0 && right>=1  
    right=right-1;  
end  
dd=right-left;  
hh=bottom-top;  
e=imcrop(d,[left top dd hh]);  
  
% 分割字符  
function [word,result]=getword(d)  
word=[];flag=0;y1=8;y2=0.5;  
% if d==[]  
%   word=[];  
% else  
    while flag==0  
        [m,n]=size(d);  
        wide=0;  
        while sum(d(:,wide+1))~=0 && wide<=n-2  
            wide=wide+1;  
        end  
        temp=qiege(imcrop(d,[1 1 wide m]));  
        [m1,n1]=size(temp);  
        if wide<y1 && n1/m1>y2  
            d(:,[1:wide])=0;  
            if sum(sum(d))~=0  
                d=qiege(d);  % 切割出最小范围  
            else word=[];flag=1;  
            end  
        else  
            word=qiege(imcrop(d,[1 1 wide m]));  
            d(:,[1:wide])=0;  
            if sum(sum(d))~=0;  
                d=qiege(d);flag=1;  
            else d=[];  
            end  
        end  
    end  
%end  
          result=d;  