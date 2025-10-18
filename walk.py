#!/usr/bin/env python3

import os
import sys
import xml.etree.ElementTree as ET

def search(directory):
    print("Searching ", directory)

    for folder, subs, files in os.walk("./test"):

        for d in subs:
            print("Examining directory:", os.path.join(folder, d))

        for filename in files:
            if filename.endswith('.xml'):
                filepath = os.path.join(folder, filename)
                print("Found XML file:", filepath)
                tree = ET.parse(filepath)
                root = tree.getroot()
                for desc in root.findall('description'):
                    print(desc.text)


# Invoke this via "./walk.py ./test"
search(sys.argv[1])

# ... or invoke it directly here, like so:
#search("./test")
