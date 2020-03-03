# 6. É muito comum que os títulos de documentos como avisos, declarações, atestados, etc., apareçam em letras maiúsculas
# separadas por um espaço em branco. Escreva uma função que receba uma palavra e a retorne no formato acima.


def titularizar(palavra):
    alfabeto = {"a": "A", "b": "B", "c": "C", "ç": "Ç", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I",
                "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S",
                "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z", "á": "Á", "â": "â", "ã": "Ã",
                "à": "À", "ä": "Ä", "é": "É", "ê": "Ê", "è": "È", "í": "Í", "î": "Î", "ì": "Ì", "ó": "Ó", "ô": "Ô",
                "õ": "Õ", "ò": "Ò", "ö": "Ö", "ú": "Ú", "û": "Û", "ù": "Ù", "ü": "Ü"}
    resultado = ""
    for x in palavra:
        if x != " ":
            resultado += alfabeto[x]
        resultado += " "
    return resultado[:-1]


print(titularizar("médico"))  # M É D I C O
print(titularizar("cuidado"))  # C U I D A D O
print(titularizar("atenção"))  # A T E N Ç Ã O
