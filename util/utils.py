from xml.etree.ElementTree import XMLParser

class MaxDepth:
    maxDepth = 0
    depth = 0

    def start(self, tag, attrib):
        self.depth += 1

        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        return self.maxDepth


def get_max_depth(exampleXml):
    target = MaxDepth()
    parser = XMLParser(target=target)
    parser.feed(exampleXml)
    depth = parser.close()
    
    return depth

def get_info(root, xml_string, file_name):
    meta = {
        'attributes': set()
    }
    dictt = {}
    size = 0

    for elem in list(root.iter()):
        size += 1
        text = elem.text

        meta['attributes'].add(elem.tag)

        if text == None:
            continue

        text = text.replace('\n', '')
        text = text.replace('\t', '')
        text = text.strip(' ')

        if text == '':
            continue

        if elem.tag in dictt.keys():
            dictt[elem.tag].append(text)
        else:
            dictt[elem.tag] = [text]

    meta['attributes'] = list(meta['attributes'])
    meta['max_depth'] = get_max_depth(xml_string)
    meta['size'] = size
    meta['file_name'] = file_name

    for key in dictt.keys():
        dictt[key] = list(set(dictt[key]))

    dictt['file_name'] = file_name

    return {
        'meta': meta, 
        'dictt': dictt
    }       