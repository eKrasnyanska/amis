from csv import dataset as ds
import datetime
import plotly
import plotly.graph_objs as go


dates = []
prices = []
my_dict = {}
for name in ds:
    for date, pr in ds[name].items():
        if 'apple' in pr.keys():
            my_dict[date] = pr['apple']['price']

kk = sorted(my_dict.keys(), key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'))
for k in kk:
    dates.append(k)
    prices.append(my_dict[k])
    print(k, my_dict[k])


data = [go.Bar(
    x = dates,
    y = prices
    )]
plotly.offline.plot(data, filename = 'test.html')