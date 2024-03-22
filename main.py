# COMSC 240 Midterm solution

COLUMNS = 4

def main():
    names = ['Aspirin','Tylenol','Lipitor','Prilosec','Glucophage','Zocor','Toprol',
             'Zithromax','Zoloft','Xanax','Wellbutrin','Flexeril','Prozac','Effexor','Adderall']
    inventory = [15,20,18,24,19,29,32,42,25,42,52,19,100,40,20]
    med_numbers = [i+1 for i in range(len(names))]  # list of medication numbers
    # dictionary with (k, v) = (names, quantities)
    names_inventory = {name: qty for name, qty in zip(names, inventory)}
    # dictionary with (k, v) = (medication numbers, names)
    index_names = {med_numbers: name for med_numbers, name in zip(med_numbers, names)}

    # program engine
    choice = 0  
    while choice != 4:
        choice = displayMenu()
        if choice == 1:
          output_inventory(index_names, names_inventory)
        elif choice == 2:
          add_medication(index_names, names_inventory)
        elif choice == 3:
          remove_medication(index_names, names_inventory)
    print('\nProgram ending.')

# displayMenu() returns the validated user choice from the menu
def displayMenu():
    print('**** Main Menu ****')
    print('Enter: [1] Medication status')
    print('       [2] Add medication to inventory')
    print('       [3] Remove medication from inventory')
    print('       [4] Quit')
    choice = int(input('       Choice --> '))
    while not 1 <= choice <= 4:
        choice = int(input('\t\t\tERROR: 1-4 only --> '))
    return choice
    
# status() displays the current inventory
# input: two dictionaries
def output_inventory(dict1, dict2):
    print('\n------------------')
    print('Medication Inventory:')
    print('------------------')
    for i in range(COLUMNS):
        print('## Name        Qty   ', end='')
    print()
    for med_nr in dict1:
        print(f'{med_nr:2} {dict1[med_nr]:10}{dict2[dict1[med_nr]]:5}', end='   ')
        if med_nr % COLUMNS == 0:
            print()
    print(); print()
    
# add_medication() displays the inventory and adds medication to it
# input: two dictionaries
def add_medication(dict1, dict2):
    output_inventory(dict1, dict2)
    print('Which medication do you want to deposit?')
    med_nr = int(input('Enter the medication number: '))
    while not 1 <= med_nr <= len(dict1):
        med_nr = int(input(f'\tERROR: invalid number (must be between 1 and {len(dict1)}) --> '))
    qty = int(input(f'How many pills of {dict1[med_nr]} to add --> '))
    while qty < 0:
        qty = int(input('\tERROR: invalid number --> '))
    dict2[dict1[med_nr]] += qty
    print(f'\tUPDATE: {dict1[med_nr]} new balance: {dict2[dict1[med_nr]]}')
    print()
    
# remove_medication() displays the inventory and removes medication from it
# input: two dictionaries
def remove_medication(dict1, dict2):
    output_inventory(dict1, dict2)
    print('Which medication fo you want to remove?')
    med_nr = int(input('Enter the medication number: '))
    while not 1 <= med_nr <= len(dict1):
        med_nr = int(input(f'\tERROR: invalid number (must be between 1 and {len(dict1)}) --> '))
    if dict2[dict1[med_nr]] == 0:
        print('\tERROR, there is no medication available to remove.\n')
    else:
        print(f'How many pills of {dict1[med_nr]} do you want to remove?')
        print(f'\tMaximum available is: {dict2[dict1[med_nr]]}')
        qty = int(input("Enter amount --> "))
        while not 0 <= qty <= dict2[dict1[med_nr]]:
            if qty > dict2[dict1[med_nr]]:
                qty = int(input(f'\tERROR: invalid number (must be no greater than {dict2[dict1[med_nr]]}) --> '))
            else:
                qty = int(input('\tERROR: invalid number (must be a positive number) --?  '))
        dict2[dict1[med_nr]] -= qty
        print(f'\tUPDATE: {dict1[med_nr]} new balance: {dict2[dict1[med_nr]]}') 
        print()
      
main()