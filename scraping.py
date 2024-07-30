from requests import get
from bs4 import BeautifulSoup

def scraping(url):
    profile = {}

    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # Procurar o nome do perfil
        name = soup.find("a", {"class": "_2nlw _2nlv"})
        profile["name"] = name.get_text().strip() if name else "Nome não encontrado"
    except Exception as e:
        profile["name"] = "Nome não encontrado"
        print(f"Erro ao obter nome: {e}")

    try:
        # Procurar seções de informação do perfil
        info_sections = soup.find_all("div", {"class": "_4qm1"})
        for section in info_sections:
            header = section.find("div", {"class": "clearfix _h71"})
            if header:
                label = header.get_text().strip().lower()
                if "trabalho" in label:
                    works = [work.get_text().strip() for work in section.find_all("div", {"class": "_2lzr _50f5 _50f7"})]
                    profile["work"] = works
                elif "educação" in label:
                    studies = [study.get_text().strip() for study in section.find_all("div", {"class": "_2lzr _50f5 _50f7"})]
                    profile["study"] = studies
                elif "cidade" in label:
                    cities = [city.get_text().strip() for city in section.find_all("span", {"class": "_2iel _50f7"})]
                    profile["cities"] = cities
    except Exception as e:
        print(f"Erro ao obter informações adicionais: {e}")

    try:
        # Procurar favoritos
        favorites = []
        favorites_section = soup.find("div", {"class": "favorites"})
        if favorites_section:
            favorites = [fav.get_text().strip() for fav in favorites_section.find_all("a")]
        profile["favorites"] = favorites
    except Exception as e:
        profile["favorites"] = []
        print(f"Erro ao obter favoritos: {e}")

    return profile
