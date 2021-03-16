import socket
from _thread import *
import pickle
from game import Game
import datetime
import random
server = "localhost"
port = 1080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2)
print("Waiting for a connection, Server Started")
connected = set()
games = {}
idCount = 0
def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                game.time = int(datetime.datetime.today().strftime("%S"))+int(datetime.datetime.today().strftime("%M"))*60+int(datetime.datetime.today().strftime("%H"))*3600
                if game.lobby is True and game.start_time - game.time<0 and game.ready:
                    game.start_time = game.time + 30
                    game.versus[0] = 0
                    game.versus[1] = 1
                    #game.versus[0] = random.randint(0, 2)
                    #game.versus[1] = random.randint(0, 2)
                    #while game.versus[1] == game.versus[0]:
                        #game.versus[1] = random.randint(0, 2)

                    list_players = [0, 1, 2]
                    for cycle_index in range(0, 3):
                        if game.hearts[cycle_index] <= 0:
                            list_players.pop(list_players.index(cycle_index))
                    if len(list_players) > 1:
                        cycle_generation = True
                    else:
                        game.f_win = list_players[0]
                    while cycle_generation:
                        cycle_generation = False
                        game.versus[0] = random.randint(0, 2)
                        game.versus[1] = random.randint(0, 2)
                        generation_done = [False, False]
                        #for cycle_index in game.hearts:
                        if game.hearts[game.versus[0]] > 0:
                            generation_done[0] = True
                        if game.hearts[game.versus[1]] > 0:
                            generation_done[1] = True
                        if not generation_done[0] or not generation_done[1]:
                            cycle_generation = True
                        if game.versus[0] == game.versus[1]:
                            cycle_generation = True
                    game.bots = str(random.randint(game.wave+1, game.wave+4)) + "#" + str(random.randint(2, game.wave + 4))
                    game.wave += 1
                    #print("Wave" + game.wave )#+ str(game.versus[0])+' vs '+str(game.versus[1]) + game.bots)
                if game.f_win != None:
                    # if f_win != None  than
                    game.start_time = game.time + 30
                if game.start_time == game.time:
                    game.winner = None
                    game.lobby = False
                if game.lobby is False and ((game.player_ready[0] is True and game.player_ready[1] is True and game.player_ready[2] is True) or (game.start_time - game.time + 60 < 0)):
                    game.lobby = True
                    game.player_ready[0] = False
                    game.player_ready[1] = False
                    game.player_ready[2] = False
                    if game.winner == None and game.wave >= 0:
                        game.winner = 20
                        game.hearts[game.versus[0]] -= 1
                        game.hearts[game.versus[1]] -= 1
                        #if game.hearts[game.versus[0]] <= 0:
                        #    game.player[game.versus[0]] = ""
                        #if game.hearts[game.versus[1]] <= 0:
                            #game.player[game.versus[1]] = ""
                #if someone first ready, than ready
                #print(game.winner)
                if game.lobby is False and game.winner == None and game.versus[0] != None and game.versus[1] != None:
                    if game.player_ready[game.versus[0]] is True and game.player_ready[game.versus[1]] is False:
                        game.winner = game.versus[0]
                        game.player_ready[game.versus[1]] = True
                        game.hearts[game.versus[1]] -= 1
                        list_players = [0, 1, 2]
                        list_players.pop(list_players.index(game.versus[0]))
                        list_players.pop(list_players.index(game.versus[1]))
                        if game.hearts[list_players[0]] <= 0:
                            game.player_ready[list_players[0]] = True
                            #game.f_win = game.winner
                            #break
                    elif game.player_ready[game.versus[1]] is True and game.player_ready[game.versus[0]] is False:
                        game.winner = game.versus[1]
                        game.player_ready[game.versus[0]] = True
                        game.hearts[game.versus[0]] -= 1
                        list_players = [0, 1, 2]
                        list_players.pop(list_players.index(game.versus[0]))
                        list_players.pop(list_players.index(game.versus[1]))
                        if game.hearts[list_players[0]] <= 0:
                            game.player_ready[list_players[0]] = True
                    #draw add
                if not data:
                    break
                    #game.player_info[p] = 'idle'00
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break
    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//3
    if idCount % 3 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    elif idCount % 3 == 2:
        p = 1
    else:
        p = 2
        games[gameId].ready = True
    start_new_thread(threaded_client, (conn, p, gameId))
