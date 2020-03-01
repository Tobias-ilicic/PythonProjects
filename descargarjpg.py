import bs4, requests, shutil, os, re
#Llamo a la pagina desde donde empieza el programa
pag=requests.get("https://xkcd.com/1953/")
soup=bs4.BeautifulSoup(pag.content, "lxml")

#cambio el working directory a la carpeta donde quiero descargar las imagenes
os.chdir(r"C:\Users\tobi\proyectospython\imagenes")

#MAIN LOOP
for a in range(0,2259):


#busco el comic principal y lo descargo a la carpeta

    imagen1=soup.find(id="comic")
    if a>0:
        anteriorpag= soup.find(attrs={"rel":"prev"})["href"]
        anteriorpag1="https://xkcd.com"+ anteriorpag
        pag=requests .get(anteriorpag1)
        soup=bs4.BeautifulSoup(pag.content,"lxml")
    for imagen in imagen1.find_all("img"):
        try:
            link= "http:" + imagen["src"]
            img=requests.get(link, stream=True)
            img.raw.decode_content=True
            imagenes=open(str(a)+"riki.jpg","wb")
            shutil.copyfileobj(img.raw,imagenes)
#Paso a la anterior pagina
            
        except:
            continue




#Repito el proceso



#pag=requests.get("http://imgs.xkcd.com/comics/reaction_maps.png", stream=True)
#imagen=open(
#pag.raw.decode_content=True
#shutil.copyfileobj(pag.raw, imagen)
