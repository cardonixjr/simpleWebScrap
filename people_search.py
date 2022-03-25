import requests
import pprint
import pandas as pd

API_KEY = "5ab8223d30168371b6fb30642fabdec5"
API_VERSION = 3
API_BASE_URL = f"https://api.themoviedb.org/{API_VERSION}"

def search_movie(name:str):
        endpoint_path = f"/search/movie"
        endpoint = f"{API_BASE_URL}{endpoint_path}?api_key={API_KEY}&query={name}"

        r = requests.get(endpoint)
        if r.status_code in range(200,299):
                data = r.json()
                results = data['results']
                movie_ids = set()
                for result in results:
                        _id = result["id"]
                        #print(result['title'], _id)
                        movie_ids.add(_id)

        output = f'{name}_result.xlsx'
        movie_data = []
        for movie_id in movie_ids:
                endpoint_path = f"/movie/{movie_id}"
                endpoint = f"{API_BASE_URL}{endpoint_path}?api_key={API_KEY}"
                r=requests.get(endpoint)
                if r.status_code in range(200,299):
                        data = r.json()
                        movie_data.append(data)

        df = pd.DataFrame(movie_data)
        print(df)

        df.to_excel(output, index=False)        

def search_person(name:str):
        endpoint_path = f"/search/person"
        endpoint = f"{API_BASE_URL}{endpoint_path}?api_key={API_KEY}&query={name}"

        r = requests.get(endpoint)
        if r.status_code in range(200,299):
                data = r.json()
                results = data['results']
                person_ids = set()
                for result in results:
                        _id = result["id"]
                        #print(result['title'], _id)
                        person_ids.add(_id)
                        print(result["name"], person_ids)
        output = f'{name}_result.xlsx'
        person_data = []
        for person_id in person_ids:
                endpoint_path = f"/person/{person_id}"
                endpoint = f"{API_BASE_URL}{endpoint_path}?api_key={API_KEY}"
                r=requests.get(endpoint)
                if r.status_code in range(200,299):
                        data = r.json()
                        person_data.append(data)

        df = pd.DataFrame(person_data)
        print(df)

        df.to_excel(output, index=False)

if __name__ == "__main__":
        pass
        #search_movie("one piece")
        #search_person("nicolas cage")
