# Який найдорожчий товар?

from csv import dataset as ds


my_dict = {}
for client in ds:
    for data in ds[client]:
        for prod in ds[client][data]:
            if prod in my_dict:
                if my_dict[prod] < ds[client][data][prod]['price']:
                    my_dict[prod] = ds[client][data][prod]['price']
            else:
                my_dict[prod] = ds[client][data][prod]['price']
print(my_dict)
most_exp_price = sorted(list(my_dict.values()))[-1]

for item in my_dict:
    if my_dict[item] == most_exp_price:
        print('The most expensive product is', item)