alist = []
for line in open('C:/Users/86188/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'):
    if line[0] == '>':
        lineL = line.split(' ')
        if alist:
            print(''.join(alist))
            alist = []
        name = lineL[0]
        print(name)
    else:
        alist.append(line.strip())
        print(''.join(alist))


       
            