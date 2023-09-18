class Result:
    #function to check if a number is a power of two
    def isPowerofTwo(self,n):

        if(n<=0):
            return False
        #To check if a number is divisible by 2 we can either use the else statement that has the while loop or use the below return statetment
        #return(n&(n-1))==0
        else:
            while n % 2 == 0:
                n//=2

            return n == 1
res = Result()

sample=res.isPowerofTwo(64)

print(sample)
