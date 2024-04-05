_file = open('project_5_storage.txt', 'a+')

def Insert(_name, _pwd):
    _fl = open('project_5_storage.txt', 'w+')
    _Data = dict(_fl)
    _Data[_name] = _pwd



    _fl.close()

#def View():
#    _fl = open('project_5_storage.txt', "r")
#    _fl = dict(_fl)




while True:
    _input = input("insert a command[insert/view/delete/update][q to Quit]: ").strip().lower()
    if _input == 'insert':
        Insert(input("Whats your name?: "), input("Whats your pwd?: "))
    elif _input == 'view':
        pass
    elif _input == 'delete':
        pass
    elif _input == 'update':
        pass
    elif _input == 'quit':
        break
    else:
        print("Pls try again...")
print("Operation Closed")