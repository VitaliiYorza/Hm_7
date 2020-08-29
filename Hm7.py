cook_book = {}
name = ''
num = 0
count_words = 0
first_ = ''
second_ = ''
thirds = ''
sum = 0
with open('Cook.txt',encoding='Utf-8') as f:
    file_length = len(f.readlines())
    f.seek(0)
    while sum != file_length:
        line_ = f.readline()
        for i in line_:
            if len(line_) == 1 and i == '\n':
                line_ = f.readline()
                sum += 1
        for i in line_:
            if i == '\n':
                continue
            name += ''.join(i)
        sum += 1
        for i in f.readline():
            if i == '\n'or i == ' ':
                continue
            num = int(i)
        sum += 1
        for i in range(0,num):
            for letters in f.readline():
                if letters == '|' or letters == '\n':
                    count_words += 1
                    continue
                if count_words == 0:
                    first_ += ''.join(letters)
                elif count_words == 1:
                    second_ += ''.join(letters)
                elif count_words == 2:
                    thirds += ''.join(letters)
            if i == 0:
                cook_book[name] = [{'ingredient_name': first_, 'quantity': second_, 'measure': thirds}]
            else:
                cook_book[name].append({'ingredient_name': first_, 'quantity': second_, 'measure': thirds})
                if i == num-1:
                    name = ''
            count_words = 0
            first_ = ''
            second_ = ''
            thirds = ''
            sum += 1
            num = 0
        name = ''
def get_shop_list_by_dishes(dishes,person_count):
    dict_ = {}
    if type(dishes) == list:
        for name_of_dishes in dishes:
            for i in range(0,len(cook_book[name_of_dishes])):
                dict_[cook_book[name_of_dishes][i]['ingredient_name']] = [
                    {'quantity':int(cook_book[name_of_dishes][i]['quantity'])*person_count,
                     'measure':cook_book[name_of_dishes][i]['measure']}]
    else:
        for i in range(0,len(cook_book[dishes])):
            dict_[cook_book[dishes][i]['ingredient_name']] = [
                {'quantity': int(cook_book[dishes][i]['quantity'])*person_count,
                 'measure': cook_book[dishes][i]['measure']}]
    return  dict_
print(get_shop_list_by_dishes(['Запеченный картофель'], 2))