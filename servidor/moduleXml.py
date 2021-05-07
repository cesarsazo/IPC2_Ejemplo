from xml.dom import minidom
mydoc = minidom.parse('entrada.xml')
items = mydoc.getElementsByTagName('EVENTO')

def returnArray():
    data = {}
    contador = 1
    for elem in items:
        data[str(contador)] = elem.firstChild.data
        contador = contador + 1
    return data
    