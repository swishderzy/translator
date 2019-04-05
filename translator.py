from py_translator import Translator
translator = Translator()
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys


def translate(text, to, source, path, key):
    """
    translating text using google translator or yandex.
    """
    try:
        # using google translator
        t = translator.translate(text, src = source, dest = to).text
    except:
        # using yandex translator
        t = "%20".join(text.split(" "))
        url = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={key}&text={t}&lang={to}&[format=plain]&[options=1]&[callback=JSONP]"
        page = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(page).read()

        soup = BeautifulSoup(page, "lxml").select("p")
        t = re.findall("text\":\[\"(.*)\"\]", soup[0].text)[0]

    print(t)
    if ".txt" in path:
        open(path, "w").write(t)
    else:
        open(path + f"/translated_text_{source}_to_{to}.txt", "w").write(t)
    return t


if __name__ == "__main__":
    translate(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[4]))
    print("Done")

