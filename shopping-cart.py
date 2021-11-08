menu = ['1. Add item', '2. View cart', '3. Remove item', '4. Compute total', '5. Quit']
action = 0
shopping_cart = []

print()
print('Welcome to the Shopping Cart Program!')

while action != 5:
    print()
    print('Please select one of the following:')
    
    for menu_item in menu:
        print(menu_item)

    action = int(input('Please enter an action: '))

    if action == 1:
        item = input('What item would you like to add? ')
        shopping_cart.append(item)
        print(f'\'{item}\' has been added to the cart.')

    elif action == 2:
        print('The contents of the shopping cart are:')
        for item in shopping_cart:
            print(item)
