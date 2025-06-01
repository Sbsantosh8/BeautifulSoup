from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <div id="main">
      <h1>Title</h1>
      <p class="subtitle">Subtitle</p>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')



# 🌳 Tree Traversal Techniques

# 1. Navigating Downward (Children)

# .contents – Gets a list of a tag’s children.

# .children – Returns an iterator.

# .descendants – All nested children, recursively.


main_div = soup.find('div', id='main')

# Content

# for cont in main_div.contents:
#     print(cont)

# Direct children
# for child in main_div.children:
#     print(child)

# All descendants
# for desc in main_div.descendants:
#     print(desc)


# ===================================================================

# 2. Navigating Upward (Parents)
# .parent – The immediate parent.

# .parents – All ancestors, recursively.


h1 = soup.find('h1')
print(h1.parent.name)  # div

# All ancestors
# for parent in h1.parents:
#     print(parent.name)
