
class StringCalculator:
    def __init__(self):
        self.default_delimiters = [",", "\n"]

    def add(self,numbers:str)->int:
        if not numbers:
            return 0
        return sum(self._parse_numbers(numbers))
    
    def _parse_numbers(self, numbers:str)->list:
        for delimiter in self.default_delimiters:
            numbers = numbers.replace(delimiter,self.default_delimiters[0])
        return [int(num) for num in numbers.split(self.default_delimiters[0])]
    
    