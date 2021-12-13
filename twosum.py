#***********************************************************************#
# 1. Two Sum                                                            #
#                                                                       #
# Given an array of integers nums and an integer target, return indices #
# of the two numbers such that they add up to target. You may assume    # 
# that each input would have exactly one solution, and you may not use  # 
# the same element twice. You can return the answer in any order.       #
#                                                                       #    
#***********************************************************************#
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        hashmap = {}
        for integer in nums:
            if integer in hashmap: 
                hashmap[integer]["second-index"] = index
                index += 1
                continue 
            else: 
                hashmap[integer] = {
                    "index": index,
                    "compliment": target - integer,
                    "second-index": -1
                }
                index += 1
        for integer in nums: 
            try:
                complement = target - integer
                if complement in hashmap: 
                    if(complement == integer): 
                        if(hashmap[integer]["second-index"] == -1):
                            continue 
                        else: 
                            index = hashmap[integer]["index"]
                            second_index = hashmap[integer]["second-index"]
                            return([index, second_index])
                    index = hashmap[integer]["index"]
                    second_index = hashmap[complement]["index"]
                    return([index, second_index])
                else: 
                    continue
            except: 
                continue
        