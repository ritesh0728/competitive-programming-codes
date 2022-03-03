'''An integer array is called arithmetic if it consists of
 at least three elements and if the difference between 
any two consecutive elements is the same.'''

def numberOfArithmeticSlices(nums) :
        s=[];cn=1
        for i in range(len(nums)-2):
            if (nums[i+1]-nums[i])==(nums[i+2]-nums[i+1]):
                cn+=1
            else:
                s.append(cn)
                cn=1
        s.append(cn)           
        ans=0   
        for i in s:
            if i==2:
                ans+=1
            if i>2:
                i-=1
                ans+=((i)*(i+1))//2
        return ans