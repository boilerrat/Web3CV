import requests
from bs4 import BeautifulSoup
import base64

# Function to convert image or font to Base64
def convert_to_base64(url):
    response = requests.get(url)
    return base64.b64encode(response.content).decode()

# Read the HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Inline CSS
css_code = """
    body {
  background-color: #1d1d1d;
  border: none;
  color: #444;
  font-family: "Inter",sans-serif;
  font-size: 20px;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
}

a:hover {
  text-decoration: none;
}

.btn {
  background: #333;
  padding: 20px; /* Increase Button Height */
  font-size: 1.2em; /* Increase button font size */
}

.btn:hover {
  background-color: #567730;
}
  
.header-inner {
  position: relative;
  text-align: center;
}

.site-title {
  font-size: 2.75em;
  font-family: "Gloock",cursive; /* Updated to Gloock font */
  font-style: normal;
  font-weight: 400;
  text-align: center;
  text-shadow: 1px 1px 2px rgba(0,0,0,.25);
}

.site-title a {
  color: #fff;
}

.site-title a:hover {
  color: #567730;
}

.site-description {
  color: #999;
  font-size: 1.1em;
  font-family: "Inter", sans-serif;
  font-weight: 400;
  line-height: 110%;
  margin: 20px 0 0;
  text-align: center;
  text-shadow: 1px 1px 1px rgba(0,0,0,.25);
}

.image-border {
  border: 10px solid #567730;
  box-sizing: border-box;
}
.section-header {
  color: #fff;
  font-size: 2em;
  font-family: "Gloock", cursive; /* Updated to Gloock font */
  font-style: normal;
  font-weight: 400;
  text-align: center;
  margin-top: .5em;
  margin-bottom: .5em;
  border: 1px solid #fff; /* Add a thin white border */
  padding: 10px; /* Add some padding */
  box-sizing: border-box; /* Include border and padding in the element's total width and height */
}
.figure img {
  height: 400px; /* Set a maximum height for the images */
  max-width: 100%;
  object-fit: cover; /* Resize the images to cover the entire area while maintaining the aspect ratio */
}
.figure figcaption {
  text-align: center; /* Center the caption */
  color: #fff; /* Set the text color to white */
  font-family: "Inter",sans-serif; /* Match the font with the rest of the webpage */
  font-size: 1em; /* Set the font size */
}
/* Media query for screens smaller than 600px */
@media (max-width: 600px) {
  body {
      font-size: 18px;
  }

  .btn {
      padding: 15px;
      font-size: 1em;
  }
}
/* Media query for screens smaller than 400px */
@media (max-width: 400px) {
  body {
      font-size: 16px;
  }

  .btn {
      padding: 10px;
      font-size: 0.8em;
  }
}
"""
style_tag = soup.new_tag('style')
style_tag.string = css_code
soup.head.append(style_tag)

# Inline external CSS files
for link_tag in soup.find_all('link', {'rel': 'stylesheet'}):
    css_url = link_tag['href']
    response = requests.get(css_url)
    css_content = response.text
    style_tag = soup.new_tag('style')
    style_tag.string = css_content
    link_tag.replace_with(style_tag)

# Inline images
for img_tag in soup.find_all('img'):
    img_url = img_tag['src']
    img_base64 = convert_to_base64(img_url)
    img_tag['src'] = f"data:image/png;base64,{img_base64}"

# Inline JavaScript files
for script_tag in soup.find_all('script', {'src': True}):
    js_url = script_tag['src']
    response = requests.get(js_url)
    js_content = response.text
    script_tag['src'] = ''
    script_tag.string = js_content

# Inline fonts (Google Fonts)
for font_link in soup.find_all('link', {'href': True}):
    if 'fonts.googleapis.com' in font_link['href']:
        font_css_url = font_link['href']
        response = requests.get(font_css_url)
        font_css_content = response.text
        style_tag = soup.new_tag('style')
        style_tag.string = font_css_content
        font_link.replace_with(style_tag)

# Write the modified HTML to a new file
with open('output.html', 'w') as file:
    file.write(str(soup))

print("Inlining completed. Check the 'output.html' file.")
