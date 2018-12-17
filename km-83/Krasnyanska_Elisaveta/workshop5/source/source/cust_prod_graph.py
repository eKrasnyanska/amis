# Якого товару, скільки покупців купляє? (графік)

from csv import dataset as ds
import plotly
import plotly.graph_objs as go

my_dict = {}
for client in ds:
    for data in ds[client]:
        for prod in ds[client][data]:
            if prod in my_dict:
                my_dict[prod].update({client})
            else:
                my_dict[prod] = {client}
#print(my_dict)
for item in my_dict:
    my_dict[item] = len(my_dict[item])

data = [go.Bar(
    x = list(my_dict.keys()),
    y = list(my_dict.values())
    )]
plotly.offline.plot(data, filename = 'test.html')