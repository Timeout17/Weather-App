from pathlib import Path

class CityLoaderClass():

    def loadfile(self, filename):

        city_names: list[str] = []

        file_path = Path(__file__).resolve().parents[3] / filename
        try:
                
            with open(file_path, encoding="utf-8") as data:
                sor = data.readlines()
                city_names = [city.strip() for city in sor]
        except FileNotFoundError as e:
            print(e)

        return city_names

    

        
if __name__ == "__main__":
    x = CityLoaderClass()
    print(x.loadfile("citynames.txt"))