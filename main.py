import time
import requests
import pycountry_convert
import click


class CityInfo:
    print_decorator_upper = "--------------"
    print_decorator_lower = "=============="

    def __init__(self, city) -> None:
        self.city_name = city

    def data_printer(self) -> None:
        """
        This method is responsible for extracting and printing data received from the api.
        If there are more than one city  with provided name all the existing cities will be printed. In that case,
        program will sleep for two seconds to avoid api per-second request limit
        """
        city_data: list = self.get_city_data()
        for city in city_data:
            city_name: str = city['name']
            country_id: str = city['country']
            population: str = city['population']
            full_country_name: str = pycountry_convert.country_alpha2_to_country_name(city['country'])
            currency: str = self.get_currency_data(country_id)
            print(f'{self.print_decorator_upper}\n{city_name}\n\n{full_country_name}\n{currency}\n{population}\n'
                  f'{self.print_decorator_lower}')
            time.sleep(2)

    def get_city_data(self) -> list:
        """
        This method gets data about city such as name, country_id and population from api and returns it.
        :return: list with data about city
        """
        api_url_city_data: str = f'https://api.api-ninjas.com/v1/city?name={self.city_name}&limit=10'
        headers: dict = {'X-Api-Key': 'LXnesvgw4/s+HoOfKMiLOw==42pTLnXxmPKv0KCi'}
        response_city_data = requests.get(api_url_city_data, headers=headers)
        if response_city_data.status_code == requests.codes.ok:
            raw_city_data: list = response_city_data.json()
            if raw_city_data:
                return raw_city_data
            else:
                print(self.print_decorator_upper)
                print(f"Invalid city name: {self.city_name}")
                print(self.print_decorator_lower)
                raise SystemExit(1)
        else:
            print("Error:", response_city_data.status_code, response_city_data.text)
            raise SystemExit(1)

    @staticmethod
    def get_currency_data(country_id) -> str:
        """
        This method is called by data_printer method and takes alpha-2 country code as a parameter
        :param country_id: country code ISO 3166-1 alpha-2 gotten from the get_city_data method
        :return: currency of the provided country
        """
        api_url_currency_data: str = "https://wft-geo-db.p.rapidapi.com/v1/locale/currencies"
        querystring: dict = {"countryId": country_id}
        headers: dict = {
            "X-RapidAPI-Key": "9478f173abmsh1a465559722e723p10a0b1jsne9a876bb5e93",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        response_currency = requests.request("GET", api_url_currency_data, headers=headers, params=querystring)
        if response_currency.status_code == requests.codes.ok:
            raw_currency_data = response_currency.json()
            if raw_currency_data:
                currency: str = raw_currency_data['data'][0]['code']
                return currency
            else:
                print("En empty response from API. Program will be terminated")
                raise SystemExit(1)
        else:
            print("Error:", response_currency.status_code, response_currency.text)
            raise SystemExit(1)


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
