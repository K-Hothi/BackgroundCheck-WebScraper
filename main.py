import requests
from bs4 import BeautifulSoup
import datetime
import textwrap

def get_age(birth_date):
    today = datetime.datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def format_text(text, width=80):
    # Wrap text to the specified width
     return textwrap.fill(text, width=width)


full_name_original = input("Enter full name (e.g., John Doe): ").split(" ")
full_name_modified = full_name_original[0].capitalize() + "_" + full_name_original[1].capitalize()

url = "https://en.wikipedia.org/wiki/" + full_name_modified
wiki_r = requests.get(url)

soup = BeautifulSoup(wiki_r.content, 'html.parser')

# Write prettified HTML to a file
with open("ParsedData.txt", "w+", encoding='utf-8') as f:
    f.write(soup.prettify())

# Extract the name (title of the page)
name = soup.find('h1', {'id': 'firstHeading'}).text


# Extract and format the birthdate
birth_date_span = soup.find('span', {'class': 'bday'})
if birth_date_span:
    date_str = birth_date_span.text
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
   
    
    # Calculate the age
    age = get_age(date_obj)
    
else:
    print("Birth date not found.")
    formatted_date = None
    age = None

about_paragraphs = soup.find_all('p')
if about_paragraphs:
    # Look for the first meaningful paragraph
    about = next((p.text.strip() for p in about_paragraphs if p.text.strip()), "About section not found.")
    print("About:", about)
else:
    print("About section not found.")

about = format_text(about)


def printAllData(name, bday, age, about):
    f = open("caseFile.txt", "w+")
    f.write(name.capitalize() + "\n\n")
    f.write("Born on " + bday + "\n\n")
    f.write(str(age) + " years old" + "\n\n")
    f.write("About: " + about)

# Call the function to print all data
printAllData(name, formatted_date, age, about)
