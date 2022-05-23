import re
handle = open('regex_sum_1419254.txt')

adn=list()

for line in handle:

    x = re.findall('[0-9]+',line)
    #print(x)

    if len(x)>0 :
        for i in x:
            #print(i)

            n = int(i)
            adn.append(n)
            #print(n)

print(sum(adn))
