import csv
import os
import wget
import zipfile

coppia = 'BNBBUSD'
intervallo = '1m'
anno = '2021'


def read_from_csv(test_file):
    try:
        with open(test_file, newline='') as csvinput:
            reader = csv.reader(csvinput)

            for row in reader:
                if row[1] > row[4]:
                    print('R', end='')
                else:
                    print('G', end='')
    except Exception:
        pass


print('downloading files..')
try:
    for x in range(12):
        wget.download('https://data.binance.vision/data/spot/monthly/klines/'+coppia+'/'+intervallo+'/'+coppia+'-'+intervallo+'-'+anno+'-'+(str(x+1)).zfill(2)+'.zip', out=os.path.dirname(__file__))
except Exception:
    pass

print('extracting files..')
try:
    for x in range(12):
        with zipfile.ZipFile(os.path.join(os.path.dirname(__file__), coppia+'-'+intervallo+'-'+anno+'-'+(str(x+1)).zfill(2)+'.zip'), 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(__file__))
except Exception:
    pass

try:
    for x in range(12):
        read_from_csv(os.path.join(os.path.dirname(__file__), coppia+'-'+intervallo+'-'+anno+'-'+(str(x+1)).zfill(2)+'.csv'))
except Exception:
    pass


# grafico 1: GRRRGGGRRRGGRRRGRGRGRGRGRGRGRGGRGGGGGGRRG
# grafico 2: RGGRRRRGGGRRGGRGRRRRGRGGGRGRRGGRGGRGR
# grafico 3: RGGGRRRGGGRGGGRRRRGRRGRGRGGGGRGRRGRGGGRG
# grafico 4: GGGGGGRGGRRGRRRGGRGRRRGRGRRRRGGGRRRGRRGGGG
