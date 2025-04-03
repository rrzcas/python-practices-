#its_ex2.2-2.py

PesData = [8, 6, 7, 9, 11, 434, -9 , -500 , 92 ]

for i in range(len(PesData) - 1):
    print('sorting per time ... ')
    newest_min = i
    for j in range(i+1, len(PesData)):
        print(f'Comparing {PesData[j]} with {PesData[newest_min]}')
        if PesData[j]  < PesData[newest_min]: 
            newest_min = j
    print(f'Swapping {PesData[i]} with {PesData[newest_min]}')
    PesData[i], PesData[newest_min] = PesData[newest_min], PesData[i]
    print('sorting per time in inner loop ... ')
    print(f'Updated list: {PesData}\n')

print("Sorted array:", PesData)

