import xmltodict
from cchess import *
def convert_game(onefile,feature_list):
    doc = xmltodict.parse(open(onefile,encoding='utf-8').read())
    fen = doc['ChineseChessRecord']["Head"]["FEN"]
    pgnfile = doc['ChineseChessRecord']["Head"]["From"]
    moves = [i["@value"] for i in  doc['ChineseChessRecord']['MoveList']["Move"] if i["@value"] != '00-00']
    bb = BaseChessBoard(fen)
    red = False
    for i in moves:
        red = not red
        x1,y1,x2,y2 = int(i[0]),int(i[1]),int(i[3]),int(i[4])
        #print("{} {}".format(i,"红" if red else "黑"))
        
        boardarr = bb.get_board_arr()
        
        # chess picker features
        picker_x = []
        picker_y = []
        if red:
            for one in feature_list['red']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
            for one in feature_list['black']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
        else:
            for one in feature_list['black']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
            for one in feature_list['red']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
        picker_x = np.asarray(picker_x)
        target = np.zeros((10,9))
        target[y1,x1] = 1
        picker_y = target
        
        # chess mover features
        mover_x = []
        mover_y = []
        mover_x = np.concatenate((picker_x,target.reshape((1,10,9))))
        mover_y = np.zeros((10,9))
        mover_y[y2,x2] = 1
        if red:
            yield picker_x,picker_y,mover_x,mover_y
        else:
            yield picker_x[:,::-1,:],picker_y[::-1,:],mover_x[:,::-1,:],mover_y[::-1,:]
        moveresult = bb.move(Pos(x1,y1),Pos(x2,y2))
        assert(moveresult != None)
        
def convert_value(onefile,feature_list):
    doc = xmltodict.parse(open(onefile,encoding='utf-8').read())
    fen = doc['ChineseChessRecord']["Head"]["FEN"]
    pgnfile = doc['ChineseChessRecord']["Head"]["From"]
    moves = [i["@value"] for i in  doc['ChineseChessRecord']['MoveList']["Move"] if i["@value"] != '00-00']
    bb = BaseChessBoard(fen)
    red = False
    for i in moves:
        red = not red
        x1,y1,x2,y2 = int(i[0]),int(i[1]),int(i[3]),int(i[4])
        #print("{} {}".format(i,"红" if red else "黑"))
        
        boardarr = bb.get_board_arr()
        
        # chess picker features
        picker_x = []
        picker_y = []
        if red:
            for one in feature_list['red']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
            for one in feature_list['black']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
        else:
            for one in feature_list['black']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
            for one in feature_list['red']:
                picker_x.append(np.asarray(boardarr == one,dtype=np.uint8))
        picker_x = np.asarray(picker_x)

        
        picker_y = target
        

        if red:
            yield picker_x,
        else:
            yield picker_x[:,::-1,:],
        assert(moveresult != None)