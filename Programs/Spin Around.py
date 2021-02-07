# Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the list counts as a 90° rotation in that direction.
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