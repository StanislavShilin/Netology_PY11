import osa
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_average_temperature():
    file_name = 'temps.txt'
    way_to_file = os.path.join(current_dir, file_name)
    list_of_temperature_f = []
    with open(way_to_file, 'r') as file_with_temperature:
        for line in file_with_temperature:
            temperature_f = line.strip().split()
            list_of_temperature_f.append(int(temperature_f[0]))

    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    result = client.service.ConvertTemp(sum(list_of_temperature_f) / len(list_of_temperature_f), 'degreeFahrenheit', 'degreeCelsius')
    print(result)


def get_cost_of_trip():
    file_name = 'currencies.txt'
    way_to_file = os.path.join(current_dir, file_name)
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    final_currency = 'RUB'
    summ_of_costs = 0
    with open(way_to_file) as file_with_price:
        for line in file_with_price:
            list_of_line = line.strip().split()
            if list_of_line[2] == final_currency:
                cost_of_final_currency = int(list_of_line[1])
            else:
                cost_of_final_currency = client.service.ConvertToNum('', list_of_line[2], final_currency,
                                                                     int(list_of_line[1]), False)
            summ_of_costs += cost_of_final_currency
    print(summ_of_costs)


def get_distance():
    file_name = 'travel.txt'
    way_to_file = os.path.join(current_dir, file_name)
    list_of_distance = []
    with open(way_to_file) as file_with_price:
        for line in file_with_price:
            list_of_line = line.strip().split()
            list_of_distance.append(float(list_of_line[1].replace(',', '')))
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    result = client.service.ChangeLengthUnit(sum(list_of_distance), 'Miles', 'Kilometers')
    print('{0:.2f}'.format(result))


get_average_temperature()
get_cost_of_trip()
get_distance()
