# This dictionary involved math operations, so I decided to keep it in a Python file, instead of a JSON file.
SQUARE_SIZE = 50

moves = {    #Row: 1
        'a8': (SQUARE_SIZE*0, SQUARE_SIZE*0),
        'b8': (SQUARE_SIZE*1, SQUARE_SIZE*0),
        'c8': (SQUARE_SIZE*2, SQUARE_SIZE*0),
        'd8': (SQUARE_SIZE*3, SQUARE_SIZE*0),
        'e8': (SQUARE_SIZE*4, SQUARE_SIZE*0),
        'f8': (SQUARE_SIZE*5, SQUARE_SIZE*0),
        'g8': (SQUARE_SIZE*6, SQUARE_SIZE*0),
        'h8': (SQUARE_SIZE*7, SQUARE_SIZE*0),

        #Row: 2
        'a7': (SQUARE_SIZE*0, SQUARE_SIZE*1),
        'b7': (SQUARE_SIZE*1, SQUARE_SIZE*1),
        'c7': (SQUARE_SIZE*2, SQUARE_SIZE*1),
        'd7': (SQUARE_SIZE*3, SQUARE_SIZE*1),
        'e7': (SQUARE_SIZE*4, SQUARE_SIZE*1),
        'f7': (SQUARE_SIZE*5, SQUARE_SIZE*1),
        'g7': (SQUARE_SIZE*6, SQUARE_SIZE*1),
        'h7': (SQUARE_SIZE*7, SQUARE_SIZE*1),

        #Row: 3
        'a6': (SQUARE_SIZE*0, SQUARE_SIZE*2),
        'b6': (SQUARE_SIZE*1, SQUARE_SIZE*2),
        'c6': (SQUARE_SIZE*2, SQUARE_SIZE*2),
        'd6': (SQUARE_SIZE*3, SQUARE_SIZE*2),
        'e6': (SQUARE_SIZE*4, SQUARE_SIZE*2),
        'f6': (SQUARE_SIZE*5, SQUARE_SIZE*2),
        'g6': (SQUARE_SIZE*6, SQUARE_SIZE*2),
        'h6': (SQUARE_SIZE*7, SQUARE_SIZE*2),

        #Row: 4
        'a5': (SQUARE_SIZE*0, SQUARE_SIZE*3),
        'b5': (SQUARE_SIZE*1, SQUARE_SIZE*3),
        'c5': (SQUARE_SIZE*2, SQUARE_SIZE*3),
        'd5': (SQUARE_SIZE*3, SQUARE_SIZE*3),
        'e5': (SQUARE_SIZE*4, SQUARE_SIZE*3),
        'f5': (SQUARE_SIZE*5, SQUARE_SIZE*3),
        'g5': (SQUARE_SIZE*6, SQUARE_SIZE*3),
        'h5': (SQUARE_SIZE*7, SQUARE_SIZE*3),

        #Row: 5
        'a4': (SQUARE_SIZE*0, SQUARE_SIZE*4),
        'b4': (SQUARE_SIZE*1, SQUARE_SIZE*4),
        'c4': (SQUARE_SIZE*2, SQUARE_SIZE*4),
        'd4': (SQUARE_SIZE*3, SQUARE_SIZE*4),
        'e4': (SQUARE_SIZE*4, SQUARE_SIZE*4),
        'f4': (SQUARE_SIZE*5, SQUARE_SIZE*4),
        'g4': (SQUARE_SIZE*6, SQUARE_SIZE*4),
        'h4': (SQUARE_SIZE*7, SQUARE_SIZE*4),

        #Row: 6
        'a3': (SQUARE_SIZE*0, SQUARE_SIZE*5),
        'b3': (SQUARE_SIZE*1, SQUARE_SIZE*5),
        'c3': (SQUARE_SIZE*2, SQUARE_SIZE*5),
        'd3': (SQUARE_SIZE*3, SQUARE_SIZE*5),
        'e3': (SQUARE_SIZE*4, SQUARE_SIZE*5),
        'f3': (SQUARE_SIZE*5, SQUARE_SIZE*5),
        'g3': (SQUARE_SIZE*6, SQUARE_SIZE*5),
        'h3': (SQUARE_SIZE*7, SQUARE_SIZE*5),

        #Row: 7
        'a2': (SQUARE_SIZE*0, SQUARE_SIZE*6),
        'b2': (SQUARE_SIZE*1, SQUARE_SIZE*6),
        'c2': (SQUARE_SIZE*2, SQUARE_SIZE*6),
        'd2': (SQUARE_SIZE*3, SQUARE_SIZE*6),
        'e2': (SQUARE_SIZE*4, SQUARE_SIZE*6),
        'f2': (SQUARE_SIZE*5, SQUARE_SIZE*6),
        'g2': (SQUARE_SIZE*6, SQUARE_SIZE*6),
        'h2': (SQUARE_SIZE*7, SQUARE_SIZE*6),

        #Row: 8
        'a1': (SQUARE_SIZE*0, SQUARE_SIZE*7),
        'b1': (SQUARE_SIZE*1, SQUARE_SIZE*7),
        'c1': (SQUARE_SIZE*2, SQUARE_SIZE*7),
        'd1': (SQUARE_SIZE*3, SQUARE_SIZE*7),
        'e1': (SQUARE_SIZE*4, SQUARE_SIZE*7),
        'f1': (SQUARE_SIZE*5, SQUARE_SIZE*7),
        'g1': (SQUARE_SIZE*6, SQUARE_SIZE*7),
        'h1': (SQUARE_SIZE*7, SQUARE_SIZE*7),
    }

default_positions =  [
    { 'Black':
        {
            'king': 'e8',
            'queen': 'd8',
            'right_rook': 'h8',
            'left_rook': 'a8',
            'right_knight': 'g8',
            'left_knight': 'b8',
            'right_bishop': 'f8',
            'left_bishop': 'c8',

            # from left to right on the chessboard:
            'pawn1': 'a7',
            'pawn2': 'b7',
            'pawn3': 'c7',
            'pawn4': 'd7',
            'pawn5': 'e7',
            'pawn6': 'f7',
            'pawn7': 'g7',
            'pawn8': 'h7',
        }
    }, 
    { 'White': 
        {
            'king': 'e1',
            'queen': 'd1',
            'right_rook': 'h1',
            'left_rook': 'a1',
            'right_knight': 'g1',
            'left_knight': 'b1',
            'right_bishop': 'f1',
            'left_bishop': 'c1',

            # from left to right on the chessboard:
            'pawn1': 'a2',
            'pawn2': 'b2',
            'pawn3': 'c2',
            'pawn4': 'd2',
            'pawn5': 'e2',
            'pawn6': 'f2',
            'pawn7': 'g2',
            'pawn8': 'h2',
        }
    }
    ]

