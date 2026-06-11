name = str("Баліо Бобік Борисович")

for ind in name:
    if ind.isalpha():
        if ind == name[-1]:
            if name.istitle():
                print("Рядок складається з літер та кожне слово починається з великої літери")
            else:
                print("Рядок складається з літер, проте не усі слова починаються з великої літери")
    elif ind.isspace():
            continue
    else:
        print("Рядок не складається з літер")
        break