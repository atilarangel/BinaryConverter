print ('Conversor Binário do Atila :3\n')
print ('======================\n')


x = True
while x:
    bin = int(input('Número decimal: \n'))
    show=[]
    while bin % 2 == 0 or bin % 2 == 1:
        if bin % 2 == 0:
            show.append('0')
        elif bin == 1:
            show.append('1')
            break
        elif bin % 2 ==1:
            show.append('1')
        bin = int(bin/2)
    show_i = list.reverse(show)
    show_j = str.join(' ', show)
    print(show_j, '\n')
        

