
class StringCalculator:
    def __init__(self):
        self.default_delimiters = [",", "\n"]

    def add(self,numbers:str)->int:
        if not numbers:
            return 0
        try:
            delimiters=self.default_delimiters
            if numbers.startswith("//"):
                custom_delimiter, numbers = self._extract_delimiters(numbers)
                delimiters = [custom_delimiter] + self.default_delimiters
            nums=self._parse_numbers(numbers, delimiters)
            self._validate_negative_numbers(nums)
            return sum(nums)
        except Exception as e:
            raise ValueError(str(e))
            
    
    def _parse_numbers(self, numbers:str, delimiters:list[str])->list:
        for delimiter in delimiters[1:]:
            numbers = numbers.replace(delimiter,delimiters[0])
        return [int(num) for num in numbers.split(delimiters[0])]
    
    def _extract_delimiters(self, numbers:str)->list:
        delimiter = numbers[2]
        numbers=numbers[4:] # this is to exlude // and \n 
        return delimiter, numbers
    
    def _validate_negative_numbers(self,numbers: list[int])->None:
        negative_nums=[num for num in numbers if num<0]
        if negative_nums:
            raise ValueError(f"negatives not allowed: { ', '.join(map(str,negative_nums))}")