
class StringCalculator:

    def add(self,numbers:str)->int:
        if not numbers:
            return 0
        nums=numbers.split(",")
        return sum(int(num) for num in nums)
    
    