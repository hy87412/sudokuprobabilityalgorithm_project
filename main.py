
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

