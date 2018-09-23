# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:27:18 2018

@author: user
"""

import json
import xmltodict
 
with open("IBM_MAP_4.xml", 'r') as f:
    xmlString = f.read()
 
print("XML input (IBM_MAP_4.xml):")
xmlString=xmlString.lstrip("0")
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

 
print("\nJSON output(xmltojson_4.json):")

print(jsonString)

 
with open("xmltojson_4.json", 'w') as f:
    f.write(jsonString.lower())
    
    
    
    
    
    
