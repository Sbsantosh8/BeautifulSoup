from bs4 import BeautifulSoup
import requests


url = "https://timesofindia.indiatimes.com/entertainment/telugu/movies/news/kalki-2898-ad-lucky-baskhar-dominate-inaugural-gaddar-telangana-film-awards/articleshow/121493131.cms"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# it will print source code of web page

# print(soup.title)

# searching tags

# soup.find("div", {"class": "footer"})  => you can search tag and attribute

# print(soup.find("div"))
# ----------------------------------------------
# to find all

# print(soup.find_all("div"))

# -------------------------------------------------

# to select (CSS Selector)

# print(soup.select())

# 1. Select by Tag

# soup.select("p")

# → [<p class="description">This is a test.</p>]
# Example: select all <p> tags


# 2. Select by Class

# soup.select(".link")

# → [<a class="link" ...>, <a class="link special" ...>]


# 3. Select by ID

# soup.select("#title")

# → [<h1 id="title">Welcome</h1>]


# 4. Descendant Selector

# soup.select("div.container a")

# → Selects all <a> inside <div class="container">


# ------------------------------------------------------------

# Extracts tag text

# print(soup.get_text())

# Returns a single string containing all the text from the document.

# Ignores/Removes all HTML tags.



