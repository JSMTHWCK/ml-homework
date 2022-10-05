#helpers for bruteforce and backtrack


def refill(squares,endpoint):
    for i in range(endpoint,len(squares)):
        squares[i] = None
    return squares

def open_spots(squares):
    opens = [i for i in range(1,10)]
    for g in squares:
        if g in opens:
            opens.remove(g)
    return opens
def debug(sq):
    if sq in [[6,1,8,7,5,3,2,9,4],[4,3,8,9,5,1,2,7,6],[8,1,6,3,5,7,4,9,2],[8,3,4,1,5,9,6,7,2]]:
        print(sq)
        z = 1
def is_hopeless(sq):
    for i in range(0,3):
        a = [sq[i*3 +0], sq[i*3 +1], sq[i*3 + 2]]
        if None not in a:
            if a[0] + a[1] + a[2] != 15:
                return True
        b = [sq[i],sq[3+i],sq[6+i]]
        if None not in b:
            if b[0] + b[1] + b[2] != 15:
                return True
    left_diag = [sq[0],sq[4],sq[8]]
    right_diag = [sq[2],sq[4],sq[6]]
    if None not in left_diag:
        if left_diag[0] + left_diag[1] + left_diag[2] != 15:
            return True
    if None not in right_diag:
        if right_diag[0] + right_diag[1] + right_diag[2] != 15:
            return True
    return False
#bruteforce - doesn't check if square is valid until the end
def bruteforce():
    squares = [None for i in range(1,10)]
    digits = [i for i in range(1,10)]
    z = 0
    for a in digits:
        a_in = 1
        squares[a_in - 1] = a
        squares = refill(squares,a_in)
        opens = open_spots(squares)

        for b in opens:
            b_in = 2
            squares = refill(squares,b_in)
            squares[b_in - 1] = b
            opens = open_spots(squares)
            for c in opens:
                c_in = 3
                squares = refill(squares,c_in)
                squares[c_in - 1] = c
                opens = open_spots(squares)

                for d in opens:
                    d_in = 4
                    squares = refill(squares,d_in)
                    squares[d_in - 1] = d
                    opens = open_spots(squares)
                    for e in opens:
                        e_in = 5
                        squares = refill(squares,e_in)
                        squares[e_in -1] = e
                        opens = open_spots(squares)

                        for f in opens:
                            f_in = 6
                            squares = refill(squares,f_in)
                            squares[f_in - 1] = f
                            opens = open_spots(squares)

                            for g in opens:
                                g_in = 7
                                squares = refill(squares,g_in)
                                squares[g_in -1] = g
                                opens = open_spots(squares)

                                for h in opens:
                                    h_in = 8
                                    squares = refill(squares,h_in)
                                    squares[h_in -1] = h
                                    opens = open_spots(squares)

                                    for i in opens:
                                        z+=1
                                        i_in = 9
                                        squares[i_in -1] = i
                                        if is_hopeless(squares) == False:
                                            for i in range(0,3):
                                                print([squares[i*3 + 0],squares[i*3 + 1],squares[i* 3 + 2]])
                                            print('')
                                        #else:
                                         #   print(z)

#backtrack - always checks, stops if isn't
def backtrack():
    squares = [None for i in range(1,10)]
    opens = [i for i in range(1,10)]
    z = 0
    for a in opens:
        a_in = 0
        squares = refill(squares,a_in)
        squares[a_in] = a
        opens = open_spots(squares)
        if is_hopeless(squares):
            continue

        for b in opens:
            b_in = 1
            squares = refill(squares,b_in)
            squares[b_in] = b
            opens = open_spots(squares)
            if is_hopeless(squares):
                continue
            
            for c in opens:
                c_in = 2
                squares = refill(squares,c_in)
                squares[c_in] = c
                opens = open_spots(squares)
                if is_hopeless(squares):
                    continue

                for d in opens:
                    d_in = 3
                    squares = refill(squares,d_in)
                    squares[d_in] = d
                    opens = open_spots(squares)
                    if is_hopeless(squares):
                        continue

                    for e in opens:
                        e_in = 4
                        squares = refill(squares,e_in)
                        squares[e_in] = e
                        opens = open_spots(squares)
                        if is_hopeless(squares):
                            continue

                        for f in opens:
                            f_in = 5
                            squares = refill(squares,f_in)
                            squares[f_in] = f
                            opens = open_spots(squares)
                            if is_hopeless(squares):
                                continue

                            for g in opens:
                                g_in = 6
                                squares = refill(squares,g_in)
                                squares[g_in] = g
                                opens = open_spots(squares)
                                if is_hopeless(squares):
                                    continue
                                
                                for h in opens:
                                    h_in = 7
                                    squares = refill(squares,h_in)
                                    squares[h_in] = h
                                    opens = open_spots(squares)
                                    if is_hopeless(squares):
                                        continue

                                    for i in opens:
                                        i_in = 8
                                        squares[i_in] = i
                                        z =0
                                        if is_hopeless(squares) == False:
                                            for i in range(0,3):
                                                print([squares[i*3 + 0],squares[i*3 + 1],squares[i* 3 + 2]])
                                            print('')
#a = bruteforce()
'''
print('')
print('')
print('')
'''
b = backtrack()
