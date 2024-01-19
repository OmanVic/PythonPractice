from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
y_combinator = response.text
soup = BeautifulSoup(y_combinator, "html.parser")
print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for article in articles:
    text = article.a.getText()
    article_text.append(text)
    link = article.a.get("href")
    article_link.append(link)
article_upvote = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name="span", class_ = "score")]
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
# print(article_upvote[largest_index])
print(article_text[largest_index])
print(article_link[largest_index])
# print(largest_number)
# print(largest_index)

# print(article_text)
# print(article_link)
# print(article_upvote)
























# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# #for tags in all_anchor_tags:
#     # print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# name = soup.select(selector="#name")
# print(name)
#
# heading = soup.select(".heading")
# print(heading)