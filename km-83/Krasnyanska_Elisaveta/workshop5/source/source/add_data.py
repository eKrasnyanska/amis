# Написати функціонал для додавання нових даних

from csv import dataset as ds


def addUserPurchase(database, customer, date, product, quantity, price):
    if customer in database:
        if date in database[customer]:
            if product in database[customer][date]:
                qt = database[customer][date][product]['quantity']
                pr = database[customer][date][product]['price']
                database[customer][date][product]['quantity'] = qt + quantity
                database[customer][date][product]['price'] = (qt*pr + quantity*price)/(qt + quantity)
            else:
                database[customer][date][product] = {'quantity': quantity, 'price': price}
        else:
            database[customer][date] = {product: {'quantity': quantity, 'price': price}}
    else:
        database[customer] = {date: {product: {'quantity': quantity, 'price': price}}}


if __name__== '__main__':
    addUserPurchase(ds, 'Jane', '10.11.2018', 'apple', 3, 5.5)
    addUserPurchase(ds, 'Jane', '10.11.2018', 'bred', 1, 3)
    addUserPurchase(ds, 'Greg', '30.02.2018', 'cake', 2, 12)
    addUserPurchase(ds, 'Greg', '15.07.2018', 'milk', 5, 14)
    print(ds)