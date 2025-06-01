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


# h1 = soup.find('h1')
# print(h1.parent.name)  # div

# All ancestors
# for parent in h1.parents:
#     print(parent.name)


# ====================================================================

# 3. Navigating Sideways (Siblings)
# .next_sibling / .previous_sibling – Get the next/previous sibling (may include text or whitespace).

# .next_siblings / .previous_siblings – Iterators over all siblings.


subtitle = soup.find('p', class_='subtitle')

# Next sibling (could be whitespace)
# print(subtitle.next_sibling)

# Iterate over all next siblings
for sib in subtitle.next_siblings:
    print(sib)



# | Direction | Property            | Type      |
# | --------- | ------------------- | --------- |
# | Down      | `.contents`         | List      |
# | Down      | `.children`         | Iterator  |
# | Down      | `.descendants`      | Iterator  |
# | Up        | `.parent`           | Tag       |
# | Up        | `.parents`          | Generator |
# | Side      | `.next_sibling`     | Tag/Text  |
# | Side      | `.previous_sibling` | Tag/Text  |
# | Side      | `.next_siblings`    | Iterator  |
