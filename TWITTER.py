import csv

f=input('Enter file: ')
fh=f
      
with open(fh, mode='r',  encoding='utf-8') as file:
    csvfh=csv.reader(file)
    rowlist=list()
    next(csvfh)
    
    for row in csvfh:
        rowlist.append(row)
    
    postlist=list()
    
    totimp=0
    toteng=0
    for item in rowlist:
        link=item[1].strip('"')
        time=item[3][0:16].strip('"')
        imp=float(item[4].strip('"'))
        totimp+=imp
        eng=float(item[5].strip('"'))
        toteng+=eng
        bareitem=f'{time} | {link} | {imp} | {eng}'
        postlist.append(bareitem)
    
    engavg=(toteng/totimp)*100
    
    #for line in postlist:
        #post=line
    
    #print('Total impressions:',int(totimp))
    #print('Total engagments:',int(toteng))
    #print('Average engagment rate:',engavg)
    
with open('Monthdata.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f'Total impressions: {(int(totimp))}')
    output_file.write('\n')
    output_file.write(f'Total engagments: {(int(toteng))}')
    output_file.write('\n')
    output_file.write(f'Average engagment rate: {engavg}%')
    output_file.write('\n')
    output_file.write('\n')
    output_file.write('Tweets:')
    output_file.write('\n')
    output_file.write('\n'.join(postlist))
