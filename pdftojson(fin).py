# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 23:50:38 2018

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:20:04 2018

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 00:07:41 2018

@author: user
"""

import pandas as pd
import tabula
import json
from tabula import wrapper
from tabula import read_pdf
#reading all the tables from the pdf into a list of dataframe

#Enter the number of Pages with different column names

df=tabula.read_pdf("IBM_MAP_5.pdf",
                   pages='2-26')

df = df.fillna(0)#preplaced nan values with zero
df

n=list(df.columns.values)
#b=tuple(n)
#a=a.append((b)


j = (df.groupby([n[0]], as_index=False)
             .apply(lambda x: x[n].to_dict('r'))
             .reset_index()
             .rename(columns={0:'Type'})
             .to_json(orient='records'))
j=j.lower()

    
with open('data7.json', 'w') as outfile:
    json.dump(j, outfile)

print(json.dumps(json.loads(j), indent=9, sort_keys=True))



    
    
'''Not Defined:  Pos Id Segment Name Req Max Use Repeat Notes Usage   
  ISA Interchange Control Header M 1     Must use     GS Functional Group Header M 1     Must use'''