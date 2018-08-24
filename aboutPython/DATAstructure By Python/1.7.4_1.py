
f=open("integers.txt","r")
sum=0
for line in f:
	line =line.strip()
	number = int (line)
	sum+=number
print("The sum is ",sum)


#读取有空格隔开的数字文本，利用一个for循环读取行，
#用字符串方法split来获取表示这些整数的字符串的列表
#然后使用另外一个for循环来处理这个列表中的每一个字符串
#


f=open("integers.txt","r")
sum=0
for line in f:
	wordlist=line.split()
	for word in wordlist:
		number=int(word)
		sum+=number
	
print("The sum is ",sum)	