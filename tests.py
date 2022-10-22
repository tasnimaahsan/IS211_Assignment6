import unittest


def convertCelsiusToKelvin(celsius):
    kelvins = (celsius+273.15)
    return round(kelvins, 2)


def convertCelsiusToFahrenheit(celsius):
    fahrenheit = (celsius*(9/5)+32)
    return round(fahrenheit, 2)


def convertFahrenheittoCelsius(fahrenheit):
    celsius = (fahrenheit-32)*(5/9)
    return round(celsius, 2)


def convertFahrenheittoKelvin(fahrenheit):
    kelvins = (fahrenheit + 459.67)*(5/9)
    return round(kelvins, 2)


def convertKelvintoCelsius(kelvins):
    celsius = (kelvins - 273.15)
    return round(celsius, 2)


def convertKelvintoFahrenheit(kelvins):
    fahrenheit = (kelvins *(9/5) - 459.67)
    return round(fahrenheit, 2)


class conversionTest(unittest.TestCase):
    knownCFK = ((0, 32, 273.15),
                (5, 41, 278.15),
                (14, 57.2, 287.15),
                (35, 95, 308.15),
                (40, 104, 313.15))

    def test_ctof(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)

    def test_ctok(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvins, result)

    def test_ftoc(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertFahrenheittoCelsius(fahrenheit)
            self.assertEqual(celsius, result)

    def test_ftok(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertFahrenheittoKelvin(fahrenheit)
            self.assertEqual(kelvins, result)

    def test_ktoc(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertKelvintoCelsius(kelvins)
            self.assertEqual(celsius, result)

    def test_ktof(self):
        for celsius, fahrenheit, kelvins in self.knownCFK:
            result = convertKelvintoFahrenheit(kelvins)
            self.assertEqual(fahrenheit, result)

if __name__ == '__main__':
    unittest.main()
