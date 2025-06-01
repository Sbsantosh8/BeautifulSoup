# 1. ✅ tag['href']

# 🔍 What it does:
# Directly accesses the value of the href attribute (or any attribute) from a tag.


from bs4 import BeautifulSoup

html = '<a href="https://example.com">Visit Example</a>'
soup = BeautifulSoup(html, "html.parser")
tag = soup.find("a")

print(tag["href"])  # Accessing 'href' attribute directly

# 🧾 Output:

# https://example.com


# 2. ✅ tag.get('class')

# 🔍 What it does:
# Safely retrieves the value of the class attribute.

# If the attribute doesn’t exist, it returns None instead of raising an error.

html = '<p class="text highlight">Hello</p>'
soup = BeautifulSoup(html, "html.parser")
tag = soup.find("p")

print(tag.get("class"))

# 🧾 Output:

# ['text', 'highlight']
# Note: class returns a list of classes.


# 3. ✅ tag.get_text()

# 🔍 What it does:
# Extracts all the text content inside the tag (including text inside nested tags).

# Keeps extra spaces and line breaks by default.

# 🧪 Example:

html = "<div><p>Hello</p> <span>World</span></div>"
soup = BeautifulSoup(html, "html.parser")
tag = soup.find("div")

print(tag.get_text())

# 🧾 Output:

# Hello World
