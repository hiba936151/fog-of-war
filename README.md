# Fog of War Chess

Implements an abstract board game based on a chess variant known as Fog of War chess. 

The game starts with the standard chess setup. Pieces move and capture the same way as in standard chess, but there are **no checks, checkmates, castling, en passant, or pawn promotion**. Like in standard chess, pawns can move two spaces forward on their first move, but only one space on subsequent moves. The game ends when a player's king is captured, and that player loses.

Locations on the board will be specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8, as shown in this diagram: ![board](board.png "board")

Special rules for this variant of chess:
Each player sees a different version of the board, where they can only view their **own pieces** and the **squares their pieces can legally move to**. If an opponent’s piece occupies one of these squares, it will be visible, as it can be captured. Hidden squares are clearly indicated to avoid confusion with visible empty squares. The objective is not to checkmate the king but to **capture** it. Players are not informed if their king is in check, and both staying in check or moving into check are legal moves, though they may result in the king being captured and losing the game.
[(https://en.wikipedia.org/wiki/Dark_chess)](https://en.wikipedia.org/wiki/Dark_chess)
