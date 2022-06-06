# to check checkmate

def check_checkmate(cb, pieces, clr):
    checkmate = [False, False, False, False, False, False, False, False, False]
    for ind,offset in enumerate((0, 1, -1, 8, -8, 7, -7, 9,-9)):
        notclr = 100 if clr 200 else 200
        king  = pieces[clr+61] + offset
        
        # black = 200 white = 100

        #pawn check
        sign = 1 if clr == 200 else -1
        for i in (7,9):
            if str(cb[king+i*sign])[:2] != (notclr+10)/10:
                checkmate[ind] = True
                break

        if checkmate[ind]:
            break

        #diagonal check(bishop and queen)
        row_pos = (king%8) - 1
        for k,v in enumerate(7, -9, 9, -7):
            looper = row_pos if 2>k else 7-row_pos
            skip = False
            for i in range(looper):
                index = king+(v*i)
                if index >= 1 and index <= 64: 
                    piece = str(cb[index])
                    if piece[0]*100 == clr:
                        break
                    elif piece[:2] == (notclr+20)/10 or piece[:2] == (notclr+50)/10:
                        checkmate[ind] = True
                        skip = not skip
                        break
            if skip:
                break

        if checkmate[ind]:
            break

        #vertical check up
        col_pos = int((king-1)/8)
        for i in range(col_pos):
            piece = str(cb[pos - (i+1) * -8])
            if piece[0]*100 == clr:
                break
            elif piece[:2] == (notclr+40)/10 or piece[:2] == notclr/10 + 5:
                checkmate[ind] = True
                break
        
        if checkmate[ind]:
            break
        
        #vertical check down
        for i in range(7-col_pos):
            piece = str(cb[pos - (i+1) * 8])
            if piece[0]*100 == clr:
                break
            elif piece[:2] == (notclr+40)/10 or piece[:2] == notclr/10 + 5:
                checkmate[ind] = True
                break
        
        if checkmate[ind]:
            break

        #horizontal right
        for i in range(row_pos):
            piece = str(cb[pos - (i+1)])
            if piece[0]*100 == clr:
                break
            elif piece[:2] == (notclr+40)/10 or piece[:2] == notclr/10 + 5:
                checkmate[ind] = True
                break
        
        if checkmate[ind]:
            break
        
        #horizontal left
        for i in range(7-row_pos):
            piece = str(cb[pos - (i+1) * -1])
            if piece[0]*100 == clr:
                break
            elif piece[:2] == (notclr+40)/10 or piece[:2] == notclr/10 + 5:
                checkmate[ind] = True
                break
        
        if checkmate[ind]:
            break

        #knight check
        for i in (-17, 17, -15, 15, -10, 10, -6, 6):
            val = king+i
            if val >= 1 and val <= 64:
                if str(cb[val])[:2] == notclr/10+3:
                    checkmate[ind] = True
