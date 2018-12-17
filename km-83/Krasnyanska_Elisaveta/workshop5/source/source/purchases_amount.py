# Скільки грошей витрачає кожний покупець на покупки? (графік)

from csv import dataset as ds
import plotly
import plotly.graph_objs as go


purch ={}
for client in ds:
    for date in ds[client]:
        for pr in ds[client][date]:
            if client in purch:
                purch[client] += (ds[client][date][pr]['quantity']*ds[client][date][pr]['price'])
            else:
                purch[client] = (ds[client][date][pr]['quantity'] * ds[client][date][pr]['price'])

#print(purch)
data = [go.Bar(
    x = list(purch.keys()),
    y = list(purch.values())
    )]
plotly.offline.plot(data, filename = 'test.html')