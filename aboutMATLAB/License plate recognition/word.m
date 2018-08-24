%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
clc  
word='';  
word(1)=wordrec(word1);  
word(2)=wordrec(word2);  
word(3)=wordrec(word3);  
word(4)=wordrec(word4);  
word(5)=wordrec(word5);  
word(6)=wordrec(word6);  
word(7)=wordrec(word7);  
clc  
save I  'word1' 'word2' 'word3' 'word4' 'word5' 'word6' 'word7'  
clear  
load I;  
load bp net;  
word='';  
word(1)=wordrec(word1);  
word(2)=wordrec(word2);  
word(3)=wordrec(word3);  
word(4)=wordrec(word4);  
word(5)=wordrec(word5);  
word(6)=wordrec(word6);  
word(7)=wordrec(word7);  
word=strcat('识别结果:',word);  
subplot(5,3,14),imshow([]),title(word,'fontsize',24)  