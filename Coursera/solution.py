import sys

base = {}
for line in sys.stdin:
    command, family_summa = line.strip().split(' ', 1)
    if command in ['DEPOSIT', 'WITHDRAW', 'TRANSFER']:
        if
        family, summa = family_summa.split()
        base.setdefault(family, 0)
        if command == 'DEPOSIT':
            base[family] += int(summa)
        elif command == 'WITHDRAW':
            base[family] -= int(summa)
        elif command == 'TRANSFER':
            family_2, summa_transfer = summa.split()
            base.setdefault(family_2, 0)
            base[family] -= int(summa_transfer)
            base[family_2] += int(summa_transfer)

    print(command, family, summa)
print(base)


