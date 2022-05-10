a, b = int(input()), int(input())
num_sum_div, num_max = 0, None
for num in range(a, b + 1):
    sum_list_div = 0
    for k in range(1, num + 1):
        if num % k == 0:
            sum_list_div += k
    if sum_list_div >= num_sum_div:
        num_sum_div = sum_list_div
        num_max = num
print(num_max, num_sum_div)

