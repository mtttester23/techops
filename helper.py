def convert_str_of_digits_to_float(string):
    temporary_list = []
    for i in string:
        if i.isdigit() is True:
            temporary_list.append(i)
        if i is ',':
            temporary_list.append('.')

    var_str = ''
    for i in temporary_list:
        var_str+=str(i)

    return float(var_str)
