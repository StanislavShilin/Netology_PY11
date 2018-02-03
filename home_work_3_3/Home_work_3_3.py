import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(way_to_text, way_to_result, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """
    with open(way_to_text) as file_with_text:
        text = file_with_text.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    result = open(way_to_result, 'w')
    result.write(''.join(json_['text']))


current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = input('Введите название файла без расширения: ').upper()
full_file_name = '{}.txt'.format(file_name)
way_to_text = os.path.join(current_dir, full_file_name)
result_full_file_name = '{}_translate.txt'.format(file_name)
way_to_result = os.path.join(current_dir, result_full_file_name)

translate_it(way_to_text, way_to_result, file_name.lower(), 'ru')

requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))