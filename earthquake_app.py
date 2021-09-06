import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'

starttime = input('Введите стартовое дату (Формат:2014-01-01): ')
endtime = input('Введите конечную дату (Формат:2014-01-02): ')
latitude = input('Укажите широту, которая будет использоваться для поиска радиуса (Евпатория: 45.2009): ')
longitude = input('Укажите долготу, которая будет использоваться для поиска радиуса (Евпатория: 33.3665): ')
maxradiuskm = input('Ограничить событиями в пределах указанного максимального количества километров от географической'
                    'точки, определенной параметрами широты и долготы): ')
minlatitude = input('Введите минимальную магнитуду: ')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime':starttime,
    'endtime': endtime,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': maxradiuskm,
    'minlatitude': minlatitude
})

data = response.json()

earthquake_list = data['features']

cnt = 0

for earthquake in earthquake_list:
    cnt += 1
    print(f" {cnt}. Расположение: {earthquake['properties']['place']}  Магнитуда: {earthquake['properties']['mag']}")
