#Function for converting text file to xml file.......
from pathlib import Path
import xml.etree.ElementTree as et
import xml.dom.minidom as minidom

def convert_to_xml():
    filename="D:\PyQt5_Designs\ try100.txt"
    root_name=Path(filename)
    root = et.Element(root_name.name)
    with open(filename) as f:
        lines = f.read().splitlines()
    celldata = et.SubElement(root, 'FileData')
    for line in it.groupby(lines):
        line=line[0]
        if not line:
            celldata = et.SubElement(root, 'FileData')
        else:
            tag = line.split(":")
            el=et.SubElement(celldata,tag[0].replace(" ",""))
            tag=' '.join(tag[1:]).strip()
            if 'File Name' in line:
                tag = line.split("\\")[-1].strip()
            elif 'File Size' in line:
                splist =  filter(None,line.split(" "))
                tag = splist[splist.index('Low:')+1]
                #splist[splist.index('High:')+1]
            el.text = tag
    formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ",encoding='utf-8').strip()
    with open("test.xml","wb") as f:
        f.write(formatedXML)
convert_to_xml()