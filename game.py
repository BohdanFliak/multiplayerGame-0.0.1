class Game:
    def __init__(self, id):
        self.pWent = [False, False]
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.time = 0
        self.start_time = 0
        self.player = [None, None, None]
        self.player_ready = [False, False, False]
        self.lobby = False
        self.versus = [None, None]
        self.player_lobby = [None, None, None]
        self.bots = None
        self.wave = -1
        self.winner = None
        self.hearts = [3, 3, 3]
        self.f_win = None
        self.spectator = [False, False, False]

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, data):
        if self.player[player] == None:
            self.player[player] = data
        #if self.lobby is True and self.ready is True:
        if data == 'r':
            self.player_ready[player]=True
        if data != 'r':
            self.player_lobby[player] = data


    def connected(self):
        return self.ready

    def bothWent(self):
        return self.pWent[0] and self.pWent[1]


    def resetWent(self):
        self.pWent[0] = False
        self.pWent[1] = False