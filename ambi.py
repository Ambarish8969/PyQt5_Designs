import xml.etree.ElementTree as ET
# def send():
#     tree=ET.parse("try.xml")
#     root=tree.getroot()
#     return(root[0].attrib)
#     # print(root[5][0].text)

# print(send())
tree=ET.parse('try.xml')
root=tree.getroot()
print(root.tag)
for child in root:
    print(child.tag+" = "+child.text)
print(root[2].text)

# import codecs
# infile=codecs.open("try100.txt",encoding="utf-8")
# outfile=codecs.open("out.xml","w",encoding="utf-8")
