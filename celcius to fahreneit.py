#class Temperature
class temperature:
    def __init__(self,temperature,fahrenheit):
        self.temperature=temperature
        self.fahrenheit=fahrenheit
    def convert_fahrenheit(self):
        return (self.temperature*1.8)+32
    def convert_celcius(self):
        return (self.fahrenheit-32)*(5/9)
t=temperature(14,68)
print(t.convert_fahrenheit())
print(t.convert_celcius())