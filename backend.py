import requests as rq


def get_data(place, days, topic):
    if not(days > 5):
        api_key = '324eaa3951961fb8173e2b779e01b42e'
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
        content = rq.get(url).json()
        list_data = content['list']
        no_of_days = 8 * days
        list_data = list_data[:no_of_days]
        print(list_data[0].keys())
        # print(list_data[1])
        # return list_data
        if topic == 'Temperature':
            temp_data = [i['main']['temp'] for i in list_data]
            dt_data = [i['dt_txt'] for i in list_data]
            return dt_data, temp_data
        elif topic == 'Sky':
            sky_data = [i['weather'][0]['main'] for i in list_data]
            dt_data = [i['dt_txt'] for i in list_data]
            return dt_data, sky_data
    else:
        return ' Only last 5 days data are available'


if __name__ == '__main__':
    result = get_data('London', 1, 'Sky')
    print(result)
