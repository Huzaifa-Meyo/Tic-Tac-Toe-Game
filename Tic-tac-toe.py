#Tic tac toe game

board = [' ' for x in range(10)]

game = False

def insertLetter(letter, pos):
    #inserts X into the board on the selected position
    board[pos] = letter

def spaceFree(pos): 
    #checks if the space is free
    return board[pos] == ' '

def printBoard(): 
    #prints the tic-tac-toe board
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | '+ board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | '+ board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | '+ board[9])
    print('   |   |')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place \'X\' (1-9): ')
        try:
            move= int(move)
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    insertLetter('X', move)
                else: 
                    print('sorry, this space is occupied!')
            else:
                print('Please insert a number within the range!')
        except:
            print('PLease type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen)>0:
        move = selectRandom(cornerOpen)
        return move 

    if 5 in possibleMoves:
        move = 5 
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)

    return move       

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome To Tic Tac Toe Game!')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard()
        else:
            print('O\'s win this time...')
            
            break
        
        if not(isWinner(board,'X')):
            move = compMove()
            if move == 0:
                print("Game tied!")
                
            else:
                insertLetter('O', move)
                print('computer placed an \'O\' in postion', move,':')
                printBoard()
        else:
            print('Good job!!, X\'s win')
            
            break

    if isBoardFull(board):
        print('Tie Game!')

if game == False:
    main()
    game = True

while game == True:
        answer = input('Do yo want to play again? (Y/N): ')
        if answer.lower() == 'y' or answer.lower == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        else:
            break

