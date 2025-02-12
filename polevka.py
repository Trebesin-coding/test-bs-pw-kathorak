from bs4 import BeautifulSoup
import json
import requests


def main():

    response = requests.get("https://js-trebesin.github.io/bsoup-exam/")
    soup = BeautifulSoup(response.content, "html.parser") #vytvoří polévku:) přeloží html pro soup 

    ingred = soup.find_all("h2")
    ingred_txt = []

    for i in ingred:
        ingred_txt.append(i.text)
    for x in range(4):
        print(ingred_txt[x])

    

    with open("polevka.json", "w") as data:
        json.dump(ingred_txt, data, indent=4, ascii=False)



if __name__ == "__main__":
    main()
