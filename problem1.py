#Euler chalange 1, Author Jaxxorio
# Chalange:
# find the sum of all multiples of 3 and 5 bellow 1000.

#upper limit var = upper (this should be 1000 but for tests will be 10)
def main():
    print "startup"
    upper = 10
    mtplestep = 0
    soloution = 0
    inc = 3
    print 'entering comp()'
    
    soloution = soloution + comp(3,0,upper,5)
    print soloution
  #  soloution = soloution + comp(5,0,upper,3)
    print soloution
    
def comp(inc,mtplestep,upper,other):
    ret = 0
    while (mtplestep < upper):
        ret = ret + mtplestep
        print ret , mtplestep , inc
        mtplestep = mtplestep + inc
        if (inc % other == 0) == true:
            mtplestep
            
            
            
    else:
        return ret
        
    
    
main()
