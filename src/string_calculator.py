
class StringCalculator:
    def __init__(self):
        self.default_delimiters = [",", "\n"]

    def add(self,numbers:str)->int:
        if not numbers:
            return 0
        delimiters=self.default_delimiters
        if numbers.startswith("//"):
            try:
                delimiter, numbers = self._extract_delimiters(numbers)
                delimiters.append(delimiter)
            except:
                raise ValueError("Invalid input")
            
        return sum(self._parse_numbers(numbers, delimiters))
    
    def _parse_numbers(self, numbers:str, delimiters:list[str])->list:
        for delimiter in delimiters[1:]:
            numbers = numbers.replace(delimiter,delimiters[0])
        return [int(num) for num in numbers.split(delimiters[0])]
    
    def _extract_delimiters(self, numbers:str)->list:
        delimiter = numbers[2]
        numbers=numbers[4:] # this is to exlude // and \n 
        return delimiter, numbers