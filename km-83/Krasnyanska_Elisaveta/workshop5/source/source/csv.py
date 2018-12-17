file = open('data/orders.csv')
f = file.read()
line = f.splitlines()

clients = []
for client in line[1:]:
    clients.append(client.split(', '))

dataset = {}
for client in clients:
    name = client[0]
    date = client[1]
    product = client[2]
    quantity = float(client[3])
    price = float(client[4])
    if name in dataset:
        if date in dataset[name]:
            if product in dataset[name][date]:
                dataset[name][date][product]['quantity'] += quantity
                dataset[name][date][product]['price'] += price
            else:
                dataset[name][date][product] = {'quantity': quantity, 'price': price}
        else:
            dataset[name][date] = {product:{'quantity': quantity, 'price': price}}
    else:
        dataset[name] = {date: {product: {'quantity': quantity, 'price': price}}}

if __name__ == '__main__':
    print(dataset)

file.close()
