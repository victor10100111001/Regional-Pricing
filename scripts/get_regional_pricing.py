import pycountry
from countries import *

SITES_THAT_REQUIRE_PROXY = [
    "formula1.com",
    "disneyplus.com",
]

SITES_THAT_DO_NOT_REQUIRE_PROXY = [
    "max.com",
    "netflix.com",
]

def main():
    print(DATAIMPULSE_COUNTRY_LIST)
    print(list(pycountry.countries))
    for country in DATAIMPULSE_COUNTRY_LIST:
        try:
            country = pycountry.countries.lookup(country).alpha_2

        except LookupError:
            print(f"cooked: {country}")


if __name__ == "__main__":
    main()