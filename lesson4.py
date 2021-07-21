def format_string(name):
    return f"hello, {name}"


my_names = ["maks", "anna", "gleb", "olga", "Tolik"]

for my_name in my_names:
    my_string = format_string(my_name)
    print(my_string)
