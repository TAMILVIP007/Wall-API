from requests import get
from bs4 import BeautifulSoup
import lxml


def get_wallpapers(q):
    try:
        k = f"https://wall.alphacoders.com/search.php?search={q.replace(' ','+')}"
        m = get(k, timeout=5)
        r = m.text
        soup = BeautifulSoup(r, "lxml")
        walls = soup.find_all("img", class_="img-responsive")
        return [x["src"] for x in walls]
    except TimeoutError:
        return "ERROR PLEASE REPORT ON @METAVOIDSUPPORT"
    except:
        return "ERROR PLEASE REPORT ON @METAVOIDSUPPORT"

