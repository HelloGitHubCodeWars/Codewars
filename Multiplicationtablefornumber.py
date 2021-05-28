def multi_table(number):
    tab=[]
    for x in range(1,11):
        a=f"{x} * {number} = {x*number}\n"
        tab.append(a)
    return ''.join(tab)[:-1]