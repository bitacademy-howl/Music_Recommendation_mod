i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
batch_size = 3
for offset in range(0, len(i), batch_size):
    print(i[offset:offset + batch_size])

