import xml.etree.ElementTree as ET
def send():
    tree=ET.parse("output.xml")
    root=tree.getroot()
    return(root[0].attrib)
   
# print(root[5][0].text)
print(send())
# dic={'data': '11 01'}
# print((dic['data']))
# if dic['data']=="11 01":
#     print("Yes")
# else:
#     print("No")