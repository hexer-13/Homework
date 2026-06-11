links = dict()
full_link = input("Введіть посилання котре ви бажаєте скоротити: ")
link_name = input("Введіть назву для цього посилання: ")
links[link_name] = full_link


link_search = input("Введіть назву за котрою скорочене необхідне посилання: ")
if link_search in link_name.lower():
    print("Повне посилання",link_search,"-", links[link_search])
else:
    print("Посиланя з такою назвою не збережено")