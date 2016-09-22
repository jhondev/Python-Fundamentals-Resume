class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No arilane code in '{}''".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid arilane code in '{}''".format(number))
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}''".format(number))

        self._number = number

    def number(self):
        return self._number

    def airlane(self):
        return self._number[:2]
        
    def test(self):
        return "test"

    def testNoInstance(self):
        return 'no instance'

f = Flight("SN978")
print(f.number())
print(Flight.number(f))