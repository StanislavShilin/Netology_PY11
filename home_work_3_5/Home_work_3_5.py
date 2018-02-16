#Утром 17.02.2018 доделаю остальные задачи. Списибо за понимание!
import osa
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_average_temperature():
    file_name = 'temps.txt'
    way_to_file = os.path.join(current_dir, file_name)
    list_of_temperature_f = []
    with open(way_to_file, 'r') as file_with_temperature:
        temperature_f = file_with_temperature.readline().strip().split()
        list_of_temperature_f.append(int(temperature_f[0]))

    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    result = client.service.ConvertTemp(sum(list_of_temperature_f) / len(list_of_temperature_f), 'degreeFahrenheit', 'degreeCelsius')
    print(result)

get_average_temperature()


