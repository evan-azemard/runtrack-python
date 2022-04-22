# import xml.etree.ElementTree as et
#
# my_tree = et.parse('domains.xml')
# my_root = my_tree.getroot()
# print("L'élément racine : ", my_root.tag)

# la balise du premier enfant de l'élément racine
# print("Le premier enfant de la racine : ", my_root[0].tag)

# afficher toutes les balises
# print("\nLes balise sont : ")
# for a in my_root[0]:
#     print(a.tag)
#
# xmlfile = "domains.xml"
#
#
# tree = ET.parse(xmlfile)
# root = tree.getroot()
#
# ET.dump(tree)
#
# print(tree)
# fichier = open('domains.xml', "r")
#
# lines = fichier.read()
#
# fichier.close()
#
# print(lines)
#
# print(tree)

from xml.dom import minidom

doc = minidom.parse('domains.xml')

elements = doc.getElementsByTagName("column")

print(elements)

print(f"Nous avons {elements.length / 2} extension")

# for i in elements:
#     print(i.getAttribute("name"))
#
# print(doc.nodeName)
# print(doc.firstChild.tagName)


# import xml.etree.ElementTree as ET
#
# mytree = ET.parse('domains.xml')
# myroot = mytree.getroot()
#
# for x in myroot.findall("darabase"):
#     item = x
#     print(item)
