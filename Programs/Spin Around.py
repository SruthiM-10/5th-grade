def spin_around(lst):
    n = len(lst)
    count = 0
    total_rotation_count = 0
    for i in range(0, n):
        if (i == 0):
            first = lst[0]
            count += 1
        else:
            if (lst[i] == first):
               count = count + 1
            else:
                count = count - 1

    total_rotation_count = count // 4
    return(total_rotation_count)


print(spin_around(['right','right','right','right','right','right','right','right','left','left']))