import customer
import cell
def readFile(name):
    with open(name) as fd:
        N,M,C,R=fd.readline().split()
        N,M,C,R=int(N),int(M),int(C),int(R)
        customers=[]
        map=[]
        for i in range(C):
            X,Y,reward=fd.readline().split()
            X,Y,reward=int(X),int(Y),int(reward)
            customers.append(customer.Customer(X,Y,reward))
        for i in range(M):
            l=list(fd.readline())
            map_list=[]
            for j in range(len(l)):
                c=cell.Cell(l[j])
                map_list.append(c)
            map.append(map_list)


    return customers,map

def writeFile(name):
    return


