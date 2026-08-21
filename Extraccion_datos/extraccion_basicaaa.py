from bs4 import BeautifulSoup


def pagina() -> str:
    return """
        <html>
            <body>
                <div>
                    <h1 id="titulo">Libros Disponibles </h1>
                    <div class="libro" data-isbn="902">
                        <h2> Python basico</h2>
                        <span> class="precio"> $1200 </span>
                    </di>
                    <div class="libro" data-isbn="903">
                        <h2> Python for dummies</h2>
                        <span> class="precio"> $1500 </span>
                    </di>
                    <div class="libro" data-isbn="904">
                        <h2> Zapato</h2>
                        <span> class="precio"> $200 </span>
                    </di>
                    <div class="libro" data-isbn="905">
                        <h2> Chocokrispis</h2>
                        <span> class="precio"> $1000 </span>
                    </di>
                </div>
            </body>
        </html>
    """

def extraer(html:str):
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    print(soup.div.div.h2.prettify())
    print(soup.div.h1.prettify())
    soup.find("h1")
    titulo = soup.find("h1", id="titulo")
    print(titulo)
    print(titulo.text)

    lista_libros = soup.find_all("div", class_="libro")
    print(len(lista_libros))

    data = []
    for libro in lista_libros:
        titulo = libro.find("h2")
        precio = libro.find("span", class_="precio")
        isbn = libro["data-isbn"]
        data.append(
            {
                "titulo": titulo.text,
                "precio": precio.text,
                "isbn": isbn,
            }
        )

    return data

if __name__ == "__main__":
    html = pagina()
    data = extraer(html)
    print(data)