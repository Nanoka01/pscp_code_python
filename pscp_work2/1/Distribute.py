"""Distribute"""
def max_children_with_8_baht(n, k):
    """dsfdsf"""
    min_amount_needed = k
    remaining_money = n - min_amount_needed
    if remaining_money < 0:
        return -1
    max_8_baht_children = remaining_money // 7
    if max_8_baht_children > k:
        max_8_baht_children = k
    remaining_after_8_baht = remaining_money - (max_8_baht_children * 7)
    if remaining_after_8_baht == 4:
        max_8_baht_children -= 1
        remaining_after_8_baht += 7
    if remaining_after_8_baht > k - max_8_baht_children:
        return -1
    return max_8_baht_children
n = int(input())
k = int(input())
print(max_children_with_8_baht(n, k))
