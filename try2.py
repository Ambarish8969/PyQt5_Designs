# Firstly we have to import 'xml.etree.ElementTree' for creating a subtree
import xml.etree.ElementTree as ET
  
# users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]
f=open("try100.txt","r")
users_list=f.read()
print(users_list)

def create_xml():
    # we make root element
    usrconfig = ET.Element("File_Name")
    # create sub element
    usrconfig = ET.SubElement(usrconfig, "sub")
    # insert list element into sub elements
    for user in range(len( users_list)):
        usr = ET.SubElement(usrconfig, "usr")
        usr.text = str(users_list[user])
    tree = ET.ElementTree(usrconfig)
    # write the tree into an XML file
    tree.write("Output.xml", encoding ='utf-8', xml_declaration = True)
create_xml()
