#!/usr/bin/env python3

import os
import sys
import xml.etree.ElementTree as ET

print(os.getcwd())
for d in os.listdir('./test'):
    if not os.path.exists(d):
        print("Examining directory:", d)
        xmlf = os.path.join('./test', d, 'test.xml')
        if os.path.exists(xmlf):
            print(xmlf)
            tree = ET.parse(xmlf)
            root = tree.getroot()
            for desc in root.findall('description'):
                print(desc.text)
