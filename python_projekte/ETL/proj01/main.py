import pandas as pd

zeitreihe = pd.date_range('01.01.1978', '31.12.1978')
#print(zeitreihe[20])

tabelle = pd.DataFrame({'col1':[1,2], 'col2':[3,4]})
print(tabelle)
print(tabelle.axes)
