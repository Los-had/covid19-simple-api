import requests
from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError

def find_country_info(country):
    def default_error_message():
        return { "Message": "This country doesn't exist or was not found." }
    
    def default_httperror_message(error):
        return { "Message": f"Sorry, we have an httperror(error: {error}), please try again"  }
    
    def default_connectionerror_message():
        return { "Message": f"Sorry, we have an connection error try again" }

    if country == '':
        return default_error_message()

    try:
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
            return default_error_message()
        
    except HTTPError as error:
        if error.code == 404:
            return default_error_message()
        else:
            return default_httperror_message(error)
    except ConnectionError:
        return default_connectionerror_message()

if __name__ == '__main__':
    print(find_country_info('russia'))