#!/usr/bin/env python3

import os
import sys
import xml.etree.ElementTree as ET

# First pass
for d in os.listdir('./test'):
    if not os.path.exists(d):
        print("Examining directory:", d)
        xmlf = os.path.join('./test', d, 'test.xml')
        if os.path.exists(xmlf):
            tree = ET.parse(xmlf)
            root = tree.getroot()
            for desc in root.findall('description'):
                print(desc.text)

# Recursive search
def searchdir(directory):
    print("Searching directory:", directory)
    for item in os.listdir(directory):
        print("Examining item:", item)
        if os.path.isdir(item):
            searchdir(item)
        elif item.endswith('.xml'):
            print("Found XML file:", itempath)
            tree = ET.parse(xmlf)
            root = tree.getroot()
            for desc in root.findall('description'):
                print(desc.text)

searchdir('./test')
