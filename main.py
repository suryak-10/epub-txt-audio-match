import sys
from bs4 import BeautifulSoup, Comment
import re

def read_file(file_path, mode='r'):
    try:
        with open(file_path, mode) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file at path {file_path} does not exist.")
        raise
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        raise
    
codes = [
    {
        "code": "&#x201C;",
        "value": "."
    },
    {
        "code": "&#x201D;",
        "value": ","
    },
    {
        "code": "&#x2019;",
        "value": "'"
    },
]

def replacer(text, findKey, replaceKey):
    for code in codes:
        find, replace = code[findKey], code[replaceKey]
        text = text.replace(find, replace)
        # text = re.sub(rf'{find}', repace, text)
    return text

text = read_file("D:\Antares\Python\epub-txt-audio-match\page002.xhtml")
print(replacer(text, "code", "value"))
print(replacer(text, "value", "code"))
sys.exit()

smil_doc = BeautifulSoup(read_file("D:\Antares\Python\epub-txt-audio-match\page002.smil"), 'html.parser')
xhtml_doc = BeautifulSoup(read_file("D:\Antares\Python\epub-txt-audio-match\page002.xhtml"), 'html.parser')

words = xhtml_doc.find(class_="text-container").find_all('div')

word_ids = {}

# def forward_backword_check(word, index):
    
last_index = 0

for par in smil_doc.find_all('par'): 
    word = str(par.find(string=lambda text: isinstance(text, Comment))).strip()
    id = re.search(r'#(\w+)', par.find('text').attrs['src']).group(1)
    for i, element in enumerate(words):
        print(element)
    word_ids[word] = id
    # print(word, id)
word_ids