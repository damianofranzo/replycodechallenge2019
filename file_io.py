import customer
import cell
import path

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

def writeFile(name,path_list):
    with open(name,'w') as fd:
       string=''
       for i in range(len(path_list)):
           x_1,y_1,x_2,y_2,p=path_list[i].split()
           string= string + str(x_1) + " " + str(y_1) + " " + str(x_2) + " " + str(y_2) + " " + p
           fd.write(string + " \n")
    return


