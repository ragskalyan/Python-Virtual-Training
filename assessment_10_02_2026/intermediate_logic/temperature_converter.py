"""
Temperature Converter Write a function that converts Celsius to Fahrenheit. then write a second function that call the
first one to print a list of converted temperatures for 0deg Celsius, 20deg Celsius and 100deg Celsius
"""


def temperature_converter(temperature):
    fahrenheit = temperature * 1.8 + 32

    return fahrenheit


def list_of_temperature_converter(*args):

    # list_of_temperature = [0, 20, 100]

    converted_temperature = []
    for i in args:
        converted_temperature.append(temperature_converter(i))

    return converted_temperature


print(
    temperature_converter(38),
    list_of_temperature_converter(0, 20, 100)
)