a = [3, 4, 2]

prefix_sums = [a[0]]

for i in range(1, len(a)):
    prefix_sums.append(prefix_sums[i - 1] + a[i])

suffix_sums = [0] * len(a)
suffix_sums[-1] = a[-1]

i = len(a) - 2

while i >= 0:
    suffix_sums[i] = suffix_sums[i + 1] + a[i]
    i -= 1

res = []

for i in range(len(a)):
    for j in range(i, len(a)):
        print(a[i:j+1])
        if j - 1 < 0:
            sub = 0
        else:
            sub = prefix_sums[i-1]

        cur_avg = (prefix_sums[j] - sub) / (j - i + 1)
        left_sum = prefix_sums[i - 1] if i - 1 >= 0 else 0
        right_sum = suffix_sums[j + 1] if j + 1 < len(a) else 0

        if (i + (len(a) - j - 1)) > 0:
            other_avg = (left_sum + right_sum) / (i + (len(a) - j - 1))
            if cur_avg > other_avg:
                res.append((i, j, cur_avg))

        else:
            res.append((i, j, cur_avg))


print('---------')
print(prefix_sums)
print(suffix_sums)
print('---------')

res      
