import time
import requests
import pycountry_convert
import click


class CityInfo:
    print_decorator_upper = "--------------"
    print_decorator_lower = "=============="

    def __init__(self, city):
        self.city_name = city

    def data_printer(self):
        city_data = self.get_city_data()
        for city in city_data:
            city_name = city['name']
            country_id = city['country']
            population = city['population']
            full_country_name = pycountry_convert.country_alpha2_to_country_name(city['country'])
            currency = self.get_currency_data(country_id)
            print(f'{self.print_decorator_upper}\n{city_name}\n\n{full_country_name}\n{currency}\n{population}\n'
                  f'{self.print_decorator_lower}')
            time.sleep(1)

    def get_city_data(self):
        api_url_city_data = f'https://api.api-ninjas.com/v1/city?name={self.city_name}&limit=10'
        headers = {'X-Api-Key': 'LXnesvgw4/s+HoOfKMiLOw==42pTLnXxmPKv0KCi'}
        response_city_data = requests.get(api_url_city_data, headers=headers)
        if response_city_data.status_code == requests.codes.ok:
            raw_city_data = response_city_data.json()
            if not raw_city_data:
                print(self.print_decorator_upper)
                print(f"Invalid city name: {self.city_name}")
                print(self.print_decorator_lower)
                raise SystemExit(1)
            return raw_city_data
        else:
            print("Error:", response_city_data.status_code, response_city_data.text)
            raise SystemExit(1)

    def get_currency_data(self, country_id):
        api_url_currency_data = "https://wft-geo-db.p.rapidapi.com/v1/locale/currencies"
        querystring = {"countryId": country_id}
        headers = {
            "X-RapidAPI-Key": "9478f173abmsh1a465559722e723p10a0b1jsne9a876bb5e93",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        response_currency = requests.request("GET", api_url_currency_data, headers=headers, params=querystring)
        if response_currency.status_code == requests.codes.ok:
            raw_currency_data = response_currency.json()
            currency = raw_currency_data['data'][0]['code']
            return currency
        else:
            print("Error:", response_currency.status_code, response_currency.text)


@click.command()
@click.argument('city_name')
def main(city_name):
    try:
        city_data = CityInfo(city=city_name)
        city_data.data_printer()
    except KeyboardInterrupt:
        print(CityInfo.print_decorator_upper)
        print("Program interrupted from keybord")
        print(CityInfo.print_decorator_lower)
    except Exception:
        print(CityInfo.print_decorator_upper)
        print("System Error")
        print(CityInfo.print_decorator_lower)


if __name__ == '__main__':
    main()
