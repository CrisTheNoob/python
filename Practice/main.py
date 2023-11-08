f_name = input('What is your name? ')
l_name = input('What is last name? ')

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(f'{formated_f_name} {formated_l_name}')

fullname = format_name(f_name, l_name)
print(fullname)