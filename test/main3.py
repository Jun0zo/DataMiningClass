def edit_distance(s1, s2):
    row_len = len(s1) + 1
    col_len = len(s2) + 1
    memory = [[-1] * (col_len) for _ in range(row_len)]
    memory[0] = list(range(len(s2)+1))
    for row_idx in range(len(s1)+1):
        memory[row_idx][0] = row_idx
    
    for row_idx in range(1, row_len):
        for col_idx in range(1, col_len):
            if s1[row_idx-1] != s2[col_idx-1]:
                memory[row_idx][col_idx] = min(memory[row_idx-1][col_idx], memory[row_idx][col_idx-1], memory[row_idx-1][col_idx-1]) + 1
            else:
                memory[row_idx][col_idx] =  memory[row_idx-1][col_idx-1]
                
    for m in memory:
        print(m)
        
edit_distance('azced', 'abcdef')