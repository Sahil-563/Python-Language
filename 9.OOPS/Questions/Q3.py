#Create a temperature class.Make two methods:
  #convertFahrenheit--It will take celcius and will print it into Fahrenheit.
  #convertCelcius--It will take Fahrenheit and will convert it into celsius

class Temperature():
    def __init__(self,temp):
        self.temp = temp
    def converttoFahrenheit(self):
        self.temp=(self.temp * 9/5) + 32
        print(f"Temperature in fahrenheit is: {round(self.temp,2)}")
    def converttocelsius(self):
        self.temp=(self.temp -32) * 5/9
        print(f"Temperature in celcius is: {round(self.temp , 2)}")

x = float(input("Enter the temperature in celcius: "))
celsius = Temperature(x)
y = float(input("Enter the temperature in Fahrenheit: "))
celsius.converttoFahrenheit()
