import webbrowser
from pathlib import Path
import requests


r = requests.get("https://api.adviceslip.com/advice")
api = r.json()
api_dict = api["slip"]
value = api_dict["advice"]


content = Path("uppgift29_template.html").read_text()
fil = content.replace('QUOTE_TEXT', value)
p = Path('Goat_Quote.html')
p.write_text(fil, encoding='utf8')
webbrowser.open(str(p))
