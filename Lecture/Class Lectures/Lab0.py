def removeDuplicates(nums) -> int:
        i = 0
        k = 0
        temps = ""
        while i < len(nums):
            print("i: ", i,"Value: ",  nums[i],"Count: ",  nums.count(nums[i]), "Next: ", (i + nums.count(nums[i])))
            temps = temps + str(nums[i])
            count = nums.count(nums[i])
            temp = i + count
            print(i, count, temp)
            i = temp
            k += 1
        nums = [int(i) for i in temps]
        print(nums)
        return k
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)