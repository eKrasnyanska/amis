# Який найпопулярніший товар?
# Якого товару було куплено найменше?

from csv import dataset as ds

my_dict = {}
for client in ds:
    for data in ds[client]:
        for prod in ds[client][data]:
            if prod in my_dict:
                my_dict[prod] += ds[client][data][prod]['quantity']
            else:
                my_dict[prod] = ds[client][data][prod]['quantity']
print(my_dict)
max_prod = sorted(list(my_dict.values()))[-1]
min_prod = sorted(list(my_dict.values()))[0]
for item in my_dict:
    if my_dict[item] == max_prod:
        print('The most popular product is ', item)
    if my_dict[item] == min_prod:
        print('The rarest product is ', item)