import requests, bs4, re

ML=requests.get("https://www.zonaprop.com.ar/departamentos-alquiler-vicente-lopez-orden-precio-ascendente.html")
soup= bs4.BeautifulSoup(ML.content, "lxml")
elems=[]
i=0
for propiedad in soup.find_all(class_="posting-card"):
    caracteristicas=propiedad.find(class_="main-features go-to-posting")
    elems.append(caracteristicas.text)
    precio=propiedad.find(attrs={"class":"first-price"})
    elems.append(precio.text)
    link=propiedad.find("a")
    link1=link.get("href")
    link1=link1.split(" ")
    elems.append("\n")
    elems.append("https://www.zonaprop.com.ar"+link1[i])
elems="".join(elems)
print(elems)

