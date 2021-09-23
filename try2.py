# Firstly we have to import 'xml.etree.ElementTree' for creating a subtree
import xml.etree.ElementTree as ET
  
# users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]
f=open("try100.txt","r")
users_list=f.readlines()
print(list(users_list))

# def create_xml():
#     # we make root element
#     usrconfig = ET.Element("File_Name")
#     # create sub element
#     usrconfig = ET.SubElement(usrconfig, "sub")
#     # insert list element into sub elements
#     for user in range(len( users_list)):
#         usr = ET.SubElement(usrconfig, "usr")
#         usr.text = str(users_list[user])
#     tree = ET.ElementTree(usrconfig)
#     # write the tree into an XML file
#     tree.write("Output.xml", encoding ='utf-8', xml_declaration = True)
#     print(tree[0])
# create_xml()

# with open("try100.txt") as lines_file:
#     lines=lines_file.read()
# root=ET.Element('root')
# for line in lines:
#     head,subhead=line.split(":")

#     head_branch=root.find(head)
#     if not head_branch:
#         head_branch=ET.SubElement(root,head)

#     subhead_branch=head_branch.find(subhead)
#     if not subhead_branch:
#         subhead_branch=ET.SubElement(branch1,subhead)
#     subhead_branch.text=subhead
# tree=ET.ElementTree(root)
# a=ET.dump(tree)
# print(a)

import xml.etree.ElementTree as ET
import fileinput
import os
import itertools as it
import xml.dom.minidom as minidom

root = ET.Element('root')
with open('try100.txt') as f:
    lines = f.read().splitlines()
    print(lines)
celldata = ET.SubElement(root, 'filedata')
for line in it.groupby(lines):
    line=line[0]
    if not line:
        celldata = ET.SubElement(root, 'filedata')
    else:
        tag = line.split(":")
        print(tag)
        el=ET.SubElement(celldata,tag[0].replace(" ",""))
        tag=' '.join(tag[1:]).strip()
        if 'File Name' in line:
            tag = line.split("\\")[-1].strip()
        elif 'File Size' in line:
            splist =  filter(None,line.split(" "))
            tag = splist[splist.index('Low:')+1]
            #splist[splist.index('High:')+1]
        el.text = tag

formatedXML = minidom.parseString(ET.tostring(root)).toprettyxml(indent=" ",encoding='utf-8').strip()

with open("test.xml","wb") as f:
    f.write(formatedXML)