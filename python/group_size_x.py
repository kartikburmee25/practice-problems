def hasGroupsSizeX(deck):
        deck.sort()
        count_list=[]
        c1=1
        for i in range(len(deck)-1):
            while(deck[i]==deck[i+1]):
                c1+=1
                i+=1
            if c1<2:
                return False
            count_list.append(c1)
            c1=1
        
        for x in count_list:
            print(x)
            
        count_list.sort()
        for i in range(len(count_list)-1):
            if count_list[i+1]%count_list[i]==0:
                continue
            else:
                return False
        return True
        

l=[1,1,1,2,1,2,4,4,4,4,3,3,3,3]

hasGroupsSizeX(l)