#---Connect Four Python TUI Edition---
#Programmed by David Feng
#Last updated in July 2018
#Contact me on Github: fengshuo2004
#Contact me via email: fengshuo2004@163.com


#SETUP
import time
c4history = open("c4history.txt","a")


#FUNCTIONS
#function for drawing the rows
def drawrow(param):
    text = ""
    for x in range(0, int(rowsize)):
        if (param[x] == "w"):
            if(mode == "0"):
                text = text + "│○"
            else: text = text + "│ ○"
        elif (param[x] == "b"):
            if(mode == "0"):
                text = text + "│●"
            else: text = text + "│ ●"
        elif (param[x] == "n"):
            if(mode == "0"):
                text = text + "│  "
            else: text = text + "│   "
    text = text + "│"
    print (text)

#function for drawing the top
def drawtop():
    text = ""
    for x in range(0, int(rowsize)):
        if (x < 10):
            if(mode == "0"):
                text = text + "  "  + str(x + 1) + " "
            else: text = text + "  "  + str(x + 1) + " "  
        elif (mode == "0"):
            text = text + " "  + str(x + 1) + " "
        else: text = text + " "  + str(x + 1) + " "
    print (text)
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(mode == "0"):
                text = text + "┌─"
            else: text = text + "┌───"
        elif (mode == "0"):
                text = text + "┬─"
        else: text = text + "┬───"

    text = text + "┐"
    print (text)

#function for drawing the seperation lines
def drawsep():
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(mode == "0"):
                text = text + "├─"
            else: text = text + "├───"
        elif (mode == "0"):
                text = text + "┼─"
        else: text = text + "┼───"

    text = text + "┤"
    print (text)

#function for drawing the bottom
def drawbottom():
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(mode == "0"):
                text = text + "└─"
            else: text = text + "└───"
        elif (mode == "0"):
                text = text + "┴─"
        else: text = text + "┴───"
    text = text + "┘"
    print (text)

#update the board
def updateboard():
    drawtop()
    for x in range(0, int(columnsize)):
        drawrow(board[x])
        if (x != int(columnsize) - 1):
            drawsep()
    drawbottom()

#update the list
def updatelist(player, column):
    if (column.isdigit()):
        if ((int(column) > 0) and (int(column) <= (int(columnsize) + 1))):
            try:
                column = str(int(column) - 1)
                for x in range(int(columnsize)):
                    if (board[x][int(column)] != "n"):
                        break
                    placedcol = x
                board[placedcol] = board[placedcol][:int(column)] + player + board[placedcol][int(column) + 1:]   
            except UnboundLocalError:
                return "FULLCOLUMNERROR"
        else: return "OUTOFRANGEERROR"
    else: return "INPUTERROR"

#check for horizontal win case
def checkhori(row,column):
    if (board[row][column] == "w"):
        if ((board[row][column + 1] == "w") and (board[row][column + 2] == "w") and (board[row][column + 3] == "w")):
            return True
        else: return False
    if (board[row][column] == "b"):
        if ((board[row][column + 1] == "b") and (board[row][column + 2] == "b") and (board[row][column + 3] == "b")):
            return True
        else: return False

#check for vertical win case
def checkvert(row,column):
    if (board[row][column] == "w"):
        if ((board[row + 1][column] == "w") and (board[row + 2][column] == "w") and (board[row + 3][column] == "w")):
            return True
        else: return False
    if (board[row][column] == "b"):
        if ((board[row + 1][column] == "b") and (board[row + 2][column] == "b") and (board[row + 3][column] == "b")):
            return True
        else: return False

#check for left diagonal win case
def checkldiag(row,column):
    if (board[row][column] == "w"):
        if ((board[row + 1][column - 1] == "w") and (board[row + 2][column - 2] == "w") and (board[row + 3][column - 3] == "w")):
            return True
        else: return False
    if (board[row][column] == "b"):
        if ((board[row + 1][column - 1] == "b") and (board[row + 2][column - 2] == "b") and (board[row + 3][column - 3] == "b")):
            return True
        else: return False

#check for right diagonal win case
def checkrdiag(row,column):
    if (board[row][column] == "w"):
        if ((board[row + 1][column + 1] == "w") and (board[row + 2][column + 2] == "w") and (board[row + 3][column + 3] == "w")):
            return True
        else: return False
    if (board[row][column] == "b"):
        if ((board[row + 1][column + 1] == "b") and (board[row + 2][column + 2] == "b") and (board[row + 3][column + 3] == "b")):
            return True
        else: return False

#check if a player have won, skip the ones that might cause list index out of range
def checkvictory():
    result = []
    for y in range(0,int(columnsize)):
        for x in range(0,int(rowsize)):
            if (board[y][x] != "n"):
                if (x < (int(columnsize) - 3)):
                    resulttemp = checkhori(y,x)
                    result.append(resulttemp)
                    if (y < (int(columnsize) - 3)):
                        resulttemp = checkrdiag(y,x)
                        result.append(resulttemp)
                if (y < (int(columnsize) - 3)):
                    resulttemp = checkvert(y,x)
                    result.append(resulttemp)
                    if (x > 2):
                        resulttemp = checkldiag(y,x)
                        result.append(resulttemp)
    if (True in result):
        return True
    else: return False

#c4history.txt writing functions
#function for writing the rows
def writerow(param):
    text = ""
    for x in range(0, int(rowsize)):
        if (param[x] == "w"):
            if(txtmode == "0"):
                text = text + "│○"
            else: text = text + "│ ○"
        elif (param[x] == "b"):
            if(txtmode == "0"):
                text = text + "│●"
            else: text = text + "│ ●"
        elif (param[x] == "n"):
            if(txtmode == "0"):
                text = text + "│  "
            else: text = text + "│   "
    text = text + "│"
    c4history.write(text + "\n")

#function for writing the top
def writetop():
    text = ""
    for x in range(0, int(rowsize)):
        if (x < 10):
            if(txtmode == "0"):
                text = text + "  "  + str(x + 1) + " "
            else: text = text + "  "  + str(x + 1) + " "  
        elif (txtmode == "0"):
            text = text + " "  + str(x + 1) + " "
        else: text = text + " "  + str(x + 1) + " "
    c4history.write(text + "\n")
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(txtmode == "0"):
                text = text + "┌─"
            else: text = text + "┌───"
        elif (txtmode == "0"):
                text = text + "┬─"
        else: text = text + "┬───"

    text = text + "┐"
    c4history.write(text + "\n")

#function for writing the seperation lines
def writesep():
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(txtmode == "0"):
                text = text + "├─"
            else: text = text + "├───"
        elif (txtmode == "0"):
                text = text + "┼─"
        else: text = text + "┼───"

    text = text + "┤"
    c4history.write(text + "\n")

#function for writing the bottom
def writebottom():
    text = ""
    for x in range(0, int(rowsize)):
        if (x == 0):
            if(txtmode == "0"):
                text = text + "└─"
            else: text = text + "└───"
        elif (txtmode == "0"):
                text = text + "┴─"
        else: text = text + "┴───"
    text = text + "┘"
    c4history.write(text + "\n")

#writing the board to c4history.txt
def writeboardtotxt():
    writetop()
    for x in range(0, int(columnsize)):
        writerow(board[x])
        if (x != int(columnsize) - 1):
            writesep()
    writebottom()


        
#MAIN PROGRAM START        
print ("---欢迎来到四子棋Python文字界面版！---\n")

#ask for mode (compatibility) and check for invalid input
while (True):
    mode = input ("请输入屏显模式，0为全角字符集，1为半角字符集：")
    if ((mode == "0") or (mode == "1")):
        break
    else: print ("【错误】输入无效！请以正确格式输入模式。")

#enable/disable save history mode and check for invalid input
while (True):
    txtmode = input ("请输入文本记录模式，0为全角字符集，1为半角字符集，按回车键关闭文本记录功能：")
    if ((txtmode == "0") or (txtmode == "1") or (txtmode -- "")):
        if (txtmode != ""):
            print ("本次游戏的结果将会被记录到同目录文本文件c4history.txt中")
        else: print ("文本记录模式已关闭")
        break
    else: print ("【错误】输入无效！请以正确格式输入模式。")

#ask for board size and check for invalid input
while (True):
    size = input ("请以axb格式输入棋盘大小，7x6棋盘为标准大小：")
    if ((len(size) < 6) and (len(size) > 2) and (size[0] in "0123456789") and (size[1] in "0123456789x") and (size[2] in "0123456789x") and (size[-1] in "0123456789")):
        break
    else: print ("【错误】输入无效！请以正确格式输入棋盘大小。")

#sorting input into rowsize and columnsize
if (size[1] in "0123456789"):
    rowsize = size[0:2]
    if (len(size) == 4):
        columnsize = size[3]
    else: columnsize = size[3:5]
else:
    rowsize = size[0]
    if (len(size) == 4):
        columnsize = size[2:4]
    else: columnsize = size[2]

#board list initialisation
board = []
for x in range(int(columnsize)):
    board.append("n"*int(rowsize))
updateboard()

#START OF THE GAME
moves = 0
while (True):
    while (True):
        answer = input("白方走棋，请输入列的数字：")
        errortype = updatelist("w", answer)
        if (errortype == "INPUTERROR"):
            print ("【错误】输入无效！请以正确格式输入列的数字。")
        elif (errortype == "FULLCOLUMNERROR"):
            print ("【错误】该列已满，请选择其他列。")
        elif (errortype == "OUTOFRANGEERROR"):
            print ("【错误】您输入的列不在棋盘范围内，请输入一个存在的列的数字。")
        else: break
    updateboard()
    win = checkvictory()
    if (win == True):
        wonplayer = "w"
        break
    while (True):
        answer = input("黑方走棋，请输入列的数字：")
        errortype = updatelist("b", answer)
        if (errortype == "INPUTERROR"):
            print ("【错误】输入无效！请以正确格式输入列的数字。")
        elif (errortype == "FULLCOLUMNERROR"):
            print ("【错误】该列已满，请选择其他列。")
        elif (errortype == "OUTOFRANGEERROR"):
            print ("【错误】您输入的列不在棋盘范围内，请输入一个存在的列的数字。")
        else: break
    updateboard()
    moves += 1
    win = checkvictory()
    if (win == True):
        wonplayer = "b"
        break

#A PLAYER HAS WON, WRITE TO HISTORY, END GAME
if (wonplayer == "w"):
    print ("\n---白方胜，游戏结束！---")
    if (txtmode != ""):
        c4history.write("--------------------\n时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "  胜利玩家：白方 获胜步数：" + str(moves + 1) + "\n最终棋局：\n")
        writeboardtotxt()
        c4history.write("--------------------\n")
    c4history.close()
if (wonplayer == "b"):
    print ("\n---黑方胜，游戏结束！---")
    if (txtmode != ""):
        c4history.write("--------------------\n时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "  胜利玩家：黑方 获胜步数：" + str(moves) + "\n最终棋局：\n")
        writeboardtotxt()
        c4history.write("--------------------\n")
    c4history.close()
