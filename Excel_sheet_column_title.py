class Solution:
    def convertToTitle(self, n: int) -> str:
        answer=''
        i=0
        while n>0:
            remainder=n%26
            if remainder==0:
                answer=answer+'Z'
                i+=1
                n=(n//26) -1
            else:
                answer+= chr((remainder-1)+ord('A'))
                i+=1
                n=(n//26) 
        return ''.join(reversed(answer))