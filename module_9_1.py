def apply_all_func(int_list, *functions):
    name_func = []
    name_func_list = []
    for x in functions:
        name_func.append(x)
        name_func_list.append(x(int_list))
    results = {}
    for n, z in zip(name_func, name_func_list):
        results[n.__name__] = z

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
