import xml.etree.ElementTree as ET
# def send():
#     tree=ET.parse("test.xml")
#     root=tree.getroot()
#     return(root[0].text)
# # print(root[5][0].text)
# print(send())

# # import xml.etree.ElementTree as ET
# tree = ET.parse('test.xml')
# root = tree.getroot()
# print(root[0][0].text)
# # for child in root:
# #     print(child.tag, child.tag)

from xml.dom import Node, minidom
dom = minidom.parse('test.xml')
print(dom.toxml()) # .toxml() creates a string from the dom object

def print_some_info(node):
    print('node representation: {0}'.format(node))
    print('.nodeName: ' + node.nodeName)
    print('.nodeValue: {0}'.format(node.nodeValue))
    for child in node.childNodes:
        print_some_info(child)
print_some_info()