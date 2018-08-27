
import time

# start_time=time.time()


# for a in range(0,1001):
# 	for b in range(0,1001):
# 		for c in range(0,1001):
# 			if a+b+c==1000 and a*a+b*b==c*c:
# 				print (str(a)+" "+str(b)+" "+str(c))
				
# end_time=time.time()
# print("time: %d"%(end_time-start_time))





start_time=time.time()


for a in range(0,1001):
	for b in range(0,1001):
		c=1000-a-b
		if a+b+c==1000 and a*a+b*b==c*c:
			print (str(a)+" "+str(b)+" "+str(c))
				
end_time=time.time()
print("time: %f"%(end_time-start_time))
