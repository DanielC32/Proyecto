import pandas as pd
import matplotlib.pyplot as plt
import couchdb
import yfinance as yf

bd_appl = yf.download('AAPL', start='2002-01-01', end='2022-09-14')

bd_nestle  = yf.download('NSRGY', start='2002-01-01', end='2022-09-14')

Close = bd_appl['Close']
moving_avg=Close.rolling(130).mean()

plt.figure(figsize=(15,10))
Close.plot(label='AAPL')
moving_avg.plot(label='Moving_avg')

nestle = bd_appl['Close']
moving_avg=Close.rolling(130).mean()

plt.figure(figsize=(15,10))
nestle.plot(label='Nestle')
moving_avg.plot(label='Moving_avg')

bd_appl['Empresa']='APPLE'
bd_nestle['Empresa']='NESTLE'

df=pd.concat([bd_appl,bd_nestle],axis=0)
df=df.reset_index()

del df['Volume']

lista=[]
lista=df.to_numpy().tolist()

user = "admin"
password = "12345"
couch = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))
db = couch.create("proyecto")

contador = 0
for datos in lista:
    while contador < 100:
     string = str(lista[contador])
     parts = string.split(', ')
     txt = parts[0];
     x = txt.replace("[Timestamp(", "")
     x = x.replace("'", "")
     x = x.replace(" 00:00:00)", "")
     txt1 = parts[6];
     x1 = txt1.replace("]", "")
     x1 = x1.replace(" '", "")
     x1 = x1.replace("'", "")
     db[str(contador) + "Tuit"] = {'Data': str(x),'Open':str(parts[1]),'High':str(parts[2]),'Low':str(parts[3]),'Close':str(parts[4]),'Adj Close':str(parts[5]),'Empresa':str(x1)}
     contador = contador + 1

contador = 0
for datos in lista:
    db.get(doc_id)
    
contadorim = 0
for datos1 in lista:
    a = db.get(str(contadorim) + "Tuit")
    print(a)
    contadorim = contadorim + 1

