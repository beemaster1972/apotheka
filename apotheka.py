from lxml import objectify
import pandas as pd

xml_data = objectify.parse('./xml/0dd9cd98-9774-441d-9960-07c330726771.xml')
root = xml_data.getroot()

data = []
cols = []
for i in range(len(root.getchildren())):
    child = root.getchildren()[i]
    data.append([subchild.text for subchild in child.getchildren()])
    cols.append(child.tag)
df = pd.DataFrame(data).T
df.columns = cols
print(df.info())
