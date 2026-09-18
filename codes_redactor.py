import json

with open("setting.json", 'r', encoding='utf-8') as file:
    setting = json.load(file)

code=11111111111111

while code!=0:
    print(f"Обычный рекорд {setting["standart_record"]}")
    print(f"Хардкорный рекорд {setting["hardcor_record"]}")
    print(f"Все применёные коды {setting["codes"]}",sep=" ,")
    print()
    print("0 - выход")
    print("11 - включить режем хардкор")
    print("998875 - отменить 'красивые' переходы")
    print("123456 - обнулить обычный рекорд")
    print("123456789 - обнулить хардкорный рекорд")
    print("10 - удалить код")
    code=int(input())
    if code==12348687:
        print("868989 - бессмертие")
        print("8685848 - медленный босс")
        print("8784858689 - долгий босс")
        print("123789 - без боя")
        print("987321 - без фарма")
        print("147852 - изменить обычный рекорд")
        print("147963 - изменить хардкорный рекорд")
    elif code==147852:
        print("Введите новый стандартный рекорд")
        setting["standart_record"]=int(input())
    elif code==147963:
        print("Введите новый хардкорный рекорд")
        setting["hardcor_record"]=int(input())
    elif code==123456:
        print("Обычный рекорд обнулён")
        setting["standart_record"]=0
    elif code==123456789:
        print("Хардкорный рекорд обнулён")
        setting["hardcor_record"]=0
    elif code==10:
            print("Введите номер удаляемого кода")
            del setting["codes"][int(input())]
    elif code!=0:
        print("Код добавлен")
        setting["codes"].append(code)
    
with open("setting.json", 'w', encoding='utf-8') as file:
    json.dump(setting, file, indent=4)