import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
data = response.text

web_data = BeautifulSoup(data, "html.parser")
movies = web_data.find_all(name="h3", class_="title")
movies_list = []
for movie in movies:
    movies_list.append(movie.getText())
movies_list.reverse()

for item in movies_list:
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{item}\n")