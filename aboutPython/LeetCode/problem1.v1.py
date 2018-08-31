

"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""




class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        try:
            for item1 in range(0,len(nums)):
        	    for item2 in range(0,len(nums)):
        		    if item1==item2:
        			    item2+=1
        		    else:	
        		        if nums[item1]==target-nums[item2]:
        		        	
        		        	# return [item1,item2]
        			        print([item1,item2])


        except ValueError:
        	print("Attention !  this list has no solution")		        




s1=Solution
s1.twoSum(range(0,10021),18006)
