from csv import dataset as ds


all_products = []
for name in ds:
    for date in ds[name]:
        for pr in ds[name][date].keys():
            if pr not in all_products:
                all_products.append(pr)

print('All product list is', all_products)