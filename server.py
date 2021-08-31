import requests
from bs4 import BeautifulSoup

def find_country_info(country):
    if country == '':
        return { "Message": "This country doesn't exist or was not found." }
    
    website = requests.get(f'https://www.worldometers.info/coronavirus/country/{country}').text
    soup = BeautifulSoup(website, 'lxml')
    info = soup.find_all('div', class_='maincounter-number')
    country_name = country.capitalize()
    
    try:
        result_array = []

        for r in info:
            result_array.append(r.find('span').text)
        
        return { "country": country_name, "total_cases": result_array[0], "deaths": result_array[1], "recovered": result_array[2] }

    except IndexError:
        return { "Message": "This country doesn't exist or was not found." }

if __name__ == '__main__':
    print(find_country_info('russia'))