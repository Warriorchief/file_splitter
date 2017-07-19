def get_spots(filename):
    with open(filename,'r') as f:
        spots=[]
        for lineno,line in enumerate(f,start=1):
            if line.startswith('<?xml'):   #OR WHATEVER OTHER MARKET TO SPLIT ON
                spots.append(lineno)
        f.close()
    with open(filename,'r') as f:
        lines=[line for line in f]
        count=len(lines)
        spots.append(count+1)
        f.close()
    return spots
    

def main(filename):
    spots=get_spots(filename)
    print 'spots is:',spots
    i=1
    with open(filename,'r') as f:
        n=0
        while n<len(spots)-1:
            with open('PATENT-'+str(n)+'.xml','w') as g:
                while i<spots[n+1]:
                    g.write(f.readline())
                    i+=1
                g.close()
            n+=1
        f.close()


main('tester.txt')
