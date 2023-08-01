def findDuplicate(nums) -> int:
        slowPointer = 0
        fastPointer = 0
     
        while True:
            fastPointer = nums[fastPointer]
            fast = nums[fastPointer]
            fastPointer=fast
            fast=nums[fastPointer]
            slowPointer = nums[slowPointer]
            slow=nums[slowPointer]
            if slow==fast and slowPointer!=fastPointer:
                return slow
            elif slow==fast and fastPointer==slowPointer:
                 fastPointer+=1
                 slowPointer+=1

            
a = findDuplicate([1,3,4,2,2])
print(a)