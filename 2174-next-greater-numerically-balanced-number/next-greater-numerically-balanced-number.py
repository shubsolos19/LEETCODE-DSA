class Solution:
    
    def is_balanced(self, n):

        freq_dict = Counter(str(n))

        for d, f in freq_dict.items():
            
            if(f != int(d)):
                return False
        
        return True
    
    def nextBeautifulNumber(self, n: int) -> int:

        n += 1
        while(not self.is_balanced(n)):
            n += 1
        return n 
        