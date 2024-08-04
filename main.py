
#스도쿠 맵 받아오기
# sudokuboard = []
# for i in range(9):
#     sudokuboard.append(list(input()))

#스도쿠 맵 프리셋
sudokuboard = [[5,6,'','','',7,'','',''],
                ['',9,'',6,8,3,'','',4],
                ['',4,'','',1,5,'',8,7],
                [6,'','','','',2,'',7,9],
                ['',3,'','','','',1,'',2],
                ['','','',7,6,4,'',3,''],
                [9,2,'',8,'',1,'','',''],
                [4,'',3,2,5,6,'','',1],
                [8,'','','',4,9,'',2,'']]

#비공간 좌표 수집
emptypos = []
for row in range(9):
    for col in range(9):
        if sudokuboard[row][col] == '':
            emptypos.append([row,col])

#행(row)검사 함수
def checkrow(selectrow):
    inlist = []
    for col in range(9):
        if sudokuboard[selectrow][col] != ' ':
            inlist.append(sudokuboard[selectrow][col])
    outlist = []
    for i in range(1,10,1):
        if i not in inlist:
            outlist.append(i)
    return outlist

#열(col)검사 함수
def checkcol(selectcol):
    inlist = []
    for row in range(9):
        if sudokuboard[row][selectcol] != ' ':
            inlist.append(sudokuboard[row][selectcol])
    outlist = []
    for i in range(1,10,1):
        if i not in inlist:
            outlist.append(i)
    return outlist

#구역(area)검사 함수
def checkarea(selectarea):
    if selectarea == 0:
        movex = -3
        movey = -3
    elif selectarea == 1:
        movex = 0
        movey = -3
    elif selectarea == 2:
        movex = 3
        movey = -3
    elif selectarea == 3:
        movex = -3
        movey = 0
    elif selectarea == 4:
        movex = 0
        movey = 0
    elif selectarea == 5:
        movex = 3
        movey = 0
    elif selectarea == 6:
        movex = -3
        movey = 3
    elif selectarea == 7:
        movex = 0
        movey = 3
    elif selectarea == 8:
        movex = 3
        movey = 3
    inlist = []
    for row in range(3):
        for col in range(3):
            if sudokuboard[3+movey+row][3+movex+col] != ' ':
                inlist.append(sudokuboard[3+movey+row][3+movex+col])
    outlist = []
    for i in range(1,10,1):
        if i not in inlist:
            outlist.append(i)
    return outlist
# #테스트용
# for i in range(9):
#     print(checkarea(i))
# for i in range(9):
#     print(checkarea(i))
# for i in range(9):
#     print(checkarea(i))