
#  10 b + 5 k + 0.5 t = 100
total = 0
for b in range(1, 10):
    for k in range(1, 20):
        for t in range(2, 101, 2):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                print(f'быков = {b}, коров = {k}, телят = {t}')
                total += 1
print(f'total result: {total}')

# быков = 1, коров = 9, телят = 90
# total result: 1



