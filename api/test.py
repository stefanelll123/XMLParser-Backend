import xml.etree.ElementTree as ET
def test1():
    tree = ET.parse('Xml_files/text.xml')
    root = tree.getroot()
    print(root.findall("[.='Some textAnother textHere I am']"))
    # for element in root.findall("[.='Some textAnother textHere I am']"):
    #     print(element)