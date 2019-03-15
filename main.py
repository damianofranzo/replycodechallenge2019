from file_io import readFile, write_file_paths
from path import Path
def simple_sol(cust, mapp, param, out_name):
    sorted_cust = sorted(cust, key=lambda x: x.reward) # reverse = True
    final_paths = []
    for i in range(param['R']):
        row_off, col_off = 1, 1
        # UP, DOWN, RIGHT, LEFT
        row, col = sorted_cust[i].row, sorted_cust[i].col
        out = ""
        # Down
        if row + 1 < param['M'] and mapp[row + 1][col].walkable == True:
            row_off = row + 1
            col_off = col
            out += "U"
        # Left
        elif col - 1 >= 0 and mapp[row][col - 1].walkable == True:
            row_off = row
            col_off = col - 1
            out += "R"
        # Up
        elif row - 1 >= 0 and mapp[row - 1][col].walkable == True:
            row_off = row -1
            col_off = col
            out += "D"
        # Right
        elif col + 1 < param['N'] and mapp[row][col + 1].walkable == True:
            row_off = row
            col_off = col + 1
            out += "L"
        # Inverse conversion
        path = Path(col_off, row_off, col, row, out)
        final_paths.append(path)


    write_file_paths(out_name, final_paths)



def exec():

    cust1, map1, param1 = readFile('./input/1_victoria_lake.txt')
    cust2, map2, param2 = readFile('./input/2_himalayas.txt')
    cust3, map3, param3 = readFile('./input/3_budapest.txt')
    cust4, map4, param4 = readFile('./input/4_manhattan.txt')
    cust5, map5, param5 = readFile('./input/5_oceania.txt')

    simple_sol(cust1, map1, param1, "./output/1.txt")
    simple_sol(cust2, map2, param2, "./output/2.txt")
    simple_sol(cust3, map3, param3, "./output/3.txt")
    simple_sol(cust4, map4, param4, "./output/4.txt")
    simple_sol(cust5, map5, param5, "./output/5.txt")


if __name__=="__main__":
    exec()
