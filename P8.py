mat = []
vetor = []

for _ in range(8):
    linha_mat = input().split()
    linha_mat = [int(num) for num in linha_mat]
    mat.append(linha_mat)

i = 0
c = 0
while i < 8 and c < 8:
    if (c + i) % 2 == 0:
        while i >= 0 and c < 8:
            vetor.append(mat[i][c])
            i -= 1
            c += 1
        if c < 8:
            i += 1
        else:
            i += 2
            c -= 1
    else:
        while c >= 0 and i < 8:
            vetor.append(mat[i][c])
            c -= 1
            i += 1
        if i < 8:
            c += 1
        else:
            c += 2
            i -= 1

print(*vetor)
