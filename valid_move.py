def valid_moves(chessboard, pos):
    valid_moves = []
    string = str(chessboard[pos])
    clr = int(string[0]) * 100
    typ = int(string[1]) * 10
    ind = int(string[2])
    
    if typ == 10: # Pawn
        sign = 1 if clr == 200 else -1
        check = ind
        check += 8*6 if clr == 100 else 8
        if pos == check:
           valid_moves.append((pos+16) * sign) 
        val = pos + 8 * sign
        if val >= 1 and val <= 64:
            valid_moves.append(val)
        for i in (7,9):
            val = pos + i * sign
            if str(cb[val])[0]*100 != clr and val >= 1 and val <= 64:
                valid_moves.append(val)

    if typ == 20: # Bishop
        row_pos = (pos % 8) - 1
        for i in range(row_pos):
            val = pos + (7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(row_pos):
            val = pos + (-9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            val = pos + (9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            val = pos + (-7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break

    if typ == 30: # Knight
        for i in (-17, 17, -15, 15, -10, 10, -6, 6):
            val = pos+i
            if val >= 1 and val <= 64:
                valid_moves.append(val)

    if typ == 40: # Rook
        row_pos = (pos%8) - 1
        col_pos = int((pos-1) / 8)
        for i in range(row_pos):
            valid_moves.append(pos - (i+1))
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            valid_moves.append(pos - ((i+1) * -1))
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(col_pos):
            valid_moves.append(pos - (i+1) * -8)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-col_pos):
            valid_moves.append(pos - (i+1) * 8)
            if str(cb[val])[0]*100 != clr:
                break

    if typ == 50: # Queen
        
        row_pos = (pos%8) - 1
        col_pos = int((pos-1) / 8)

        #bishop like moves
        for i in range(row_pos):
            val = pos + (7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(row_pos):
            val = pos + (-9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            val = pos + (9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            val = pos + (-7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
            if str(cb[val])[0]*100 != clr:
                break

        # rook like moves
        for i in range(row_pos):
            valid_moves.append(pos + (i+1))
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-row_pos):
            valid_moves.append(pos + ((i+1) * -1))
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(col_pos):
            valid_moves.append(pos + (((i+1) * 8) * -1))
            if str(cb[val])[0]*100 != clr:
                break
        for i in range(7-col_pos):
            valid_moves.append(pos + ((i+1) * 8))
            if str(cb[val])[0]*100 != clr:
                break

    if typ == 60: # King
        for i in (-9, -8, -7, -1, 1, 7, 8, 9):
            val = pos + i
            if val <= 64 and val >= 1:
                 valid_moves.append(val)
    

    for i in valid_moves:
        if str(chessboard[i])[0] == clr/100:
            valid_moves.remove(i)

    return valid_moves

def validate_move(chessboard, pos, move):
    moves = valid_moves(chessboard, pos)
    if move in moves:
        return True
    else:
        return False

