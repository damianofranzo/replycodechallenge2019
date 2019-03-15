from path import Path

def get_best(heatmap):
    row_max, col_max = -1, -1
    max_val = -10000
    for i in range(len(heatmap.map)):
        for j in range(len(heatmap.map[0])):
            if heatmap.map[i][j].prize_up_to > max_val:
                max_val = heatmap.map[i][j].prize_up_to
                row_max, col_max = i, j
    return (row_max, col_max, max_val)


def pick_from_map(heatmaps, param):
    final_paths = []
    possible_places = []
    for hm in heatmaps:
        best_coord = get_best(hm)
        possible_places.append(best_coord)
    sorted_best_cord = sorted(possible_places, key=lambda x: x[2])
    final_places = []
    for i in range(param['R']):
        final_places.append((sorted_best_cord[i][0], sorted_best_cord[i][1]))
    m_inf = float("-inf")
    for hm in heatmaps:
        row_max, col_max, max_val, max_i = -1, -1, m_inf, -1
        row_c, col_c = hm.customer.row, hm.customer.col
        for i in range(param['R']):
            row, col = final_places[i][0], final_places[i][1]
            if hm.map[row][col].prize_up_to > max_val:
                max_val = hm.map[row][col].prize_up_to
                row_max, col_max = row, col
                max_i = i
        if max_val != m_inf:
            row_cur, col_cur = final_places[max_i][0], final_places[max_i][1]
            perc_str = ""
           # if row_cur == hm.customer.row or col_cur == hm.customer.col:
              #  print("They are equal!")
               # print(row_cur, hm.customer.row, col_cur, hm.customer.col)
            while row_cur != hm.customer.row and col_cur != hm.customer.col:
                prec_row, prec_col = row_cur, col_cur
                row_cur, col_cur = hm.map[row_cur][col_cur].row_dad, hm.map[row_cur][col_cur].col_dad
                # print("Before", perc_str)
                # DOWN
                if prec_row == row_cur + 1:
                    perc_str += "U"
                # Left
                elif prec_row == row_cur - 1:
                    perc_str += "D"
                # Up
                elif prec_col == col_cur + 1:
                    perc_str += "L"
                # Right
                elif prec_col == col_cur - 1:
                    perc_str += "R"
                else:
                    print("WTF")
                # print("After", perc_str)
            # Negh

            final_paths.append(Path(final_places[max_i][1], final_places[max_i][0], -1, -1, perc_str))
    return final_paths

