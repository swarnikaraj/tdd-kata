
class StringCalculator:
    def __init__(self):
        self.default_delimiters = [",", "\n"]

    def add(self,numbers:str)->int:
        if not numbers:
            return 0
        try:
            delimiters=self.default_delimiters
            if numbers.startswith("//"):
                print("has // 12")
                custom_delimiter, numbers = self._extract_delimiters(numbers)
                print(custom_delimiter, 18)
                print(numbers, 19)
                delimiters = custom_delimiter + self.default_delimiters
                print(delimiters, 20)
            nums=self._parse_numbers(numbers, delimiters)
            self._validate_negative_numbers(nums)
            return sum(nums)
        except Exception as e:
            raise ValueError(str(e))
            
    
    def _parse_numbers(self, numbers:str, delimiters:list[str])->list:
        print(numbers, 23)
        for delimiter in delimiters[1:]:
            numbers = numbers.replace(delimiter,delimiters[0])
            print(numbers,24)

        return [num for num in [int(n) for n in numbers.split(delimiters[0])] if num<=1000]
    
    def _extract_delimiters(self, numbers: str) -> tuple[list[str], str]:
        print("==========")
        print(numbers, 29)
        print("=========")
        if numbers[2]=="[":
            delimiters=[]
            curr=2
            while numbers[curr]=="[":
                end_brack = numbers.index(']', curr)
                delimiters.append(numbers[curr + 1:end_brack])
                curr = end_brack + 1
            
            
            numbers = numbers[curr + 1:]  # \n
            print(numbers, "numbers at 44")
            return delimiters, numbers
            
        else:
            delimiter=[numbers[2]]
            numbers=numbers[4:] # this is to exlude // and \n 
        return delimiter, numbers
    
    def _validate_negative_numbers(self,numbers: list[int])->None:
        negative_nums=[num for num in numbers if num<0]
        if negative_nums:
            raise ValueError(f"negatives not allowed: { ', '.join(map(str,negative_nums))}")