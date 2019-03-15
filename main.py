from file_io import readFile, write_file_paths
from path import Path
from dijkstra import djikstra
from pick_from_map import pick_from_map

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

    cust3, map3, param3 = readFile('./input/3_budapest.txt')

    """
    cust1, map1, param1 = readFile('./input/1_victoria_lake.txt')
    cust4, map4, param4 = readFile('./input/4_manhattan.txt')
    cust5, map5, param5 = readFile('./input/5_oceania.txt')
    """
    heatmaps3 = djikstra(cust3, map3)
    final_paths3 = pick_from_map(heatmaps3, param3)
    write_file_paths("./output/3.txt", final_paths3)
    """
    heatmaps1 = djikstra(cust1, map1)
    final_paths1 = pick_from_map(heatmaps1, param1)
    write_file_paths("./output/1.txt", final_paths1)

    #simple_sol(cust1, map1, param1, "./output/1.txt")
    #simple_sol(cust2, map2, param2, "./output/2.txt")
    #simple_sol(cust3, map3, param3, "./output/3.txt")
    #simple_sol(cust4, map4, param4, "./output/4.txt")
    #simple_sol(cust5, map5, param5, "./output/5.txt")

    """
    #cust1, map1, param1 = readFile('./input/prova.txt')
    heatmaps1 = djikstra(cust3, map3)
    final_paths1 = pick_from_map(heatmaps1, param3)
    write_file_paths("./output/prova.txt", final_paths1)
   

if __name__=="__main__":
    exec()
