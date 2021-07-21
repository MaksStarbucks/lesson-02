import random


def format_string(*args):
    if len(args) == 0:
        return
    args_sum = 0
    max_el = args[0]
    for element in args:
        if element > max_el:
            max_el = element
        args_sum += element
    return args_sum, max_el


random_elements = []
for _ in range(10):
    random_el = random.randint(1, 100)
random_elements.append(random_el)
args_sum, max_el = format_string(*random_elements)
print(args_sum, max_el)
