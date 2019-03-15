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
            col, row, reward=fd.readline().split()
            row, col, reward = int(row),int(col),int(reward)
            customers.append(customer.Customer(row,col,reward))
        for i in range(M):
            l=list(fd.readline())
            map_list=[]
            for j in range(len(l)):
                c=cell.Cell(l[j])
                map_list.append(c)
            map.append(map_list)
    param = {}
    param['N'] = N
    param['M'] = M
    param['C'] = C
    param['R'] = R


    return customers,map, param

def writeFile(file_name, coor, path, is_string=False):
    with open(file_name,'w') as fd:
       string=''
       for i in range(len(path)):
           x_1,y_1,x_2,y_2,p=path[i].split()
           string= string + str(x_1) + " " + str(y_1) + " " + str(x_2) + " " + str(y_2) + " " + p
           fd.write(string + " \n")
    return


def write_file_paths(file_name, path_list):
    with open(file_name,'w') as fd:
       for p in path_list[:-1]:
           x, y = p.office_x, p.office_y
           out = str(x) + " " + str(y) + " " + p.path + "\n"
           fd.write(out)
       x, y = path_list[-1].office_x,  path_list[-1].office_y
       out = str(x) + " " + str(y) + " " + path_list[-1].path
       fd.write(out)
