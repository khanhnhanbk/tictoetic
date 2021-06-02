"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""
import pygame
from pygame.locals import *
import sys
import math
import time

from pygame.transform import smoothscale
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
import os

pygame.init()

RED = (239, 71, 111)
YELLOW = (255, 209, 102)
GREEN = (6, 214, 160)
BLUE = (0, 0, 178)
BLACK = (0, 0, 0)


HEIGHT = 450
WIDTH = 400


FramePerSec = pygame.time.Clock()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


def drawText(win, letter: str, pos):
    if letter == "X":
        color = RED
    else:
        color = BLUE
    font = pygame.font.SysFont(None, 90)
    img = font.render(letter, True, color)
    img_rect = img.get_rect(
        center=pygame.Rect(50 + pos[0] * 100, 100 + pos[1] * 100, 100, 100).center
    )
    win.blit(img, img_rect)


poses = []


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    def resetGame(self):
        self.board = [" "] * 9
        self.current_winner = None

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    x_win = 0
    o_win = 0
    tie = 0
    letter = "X"
    pygame.draw.rect(win, BLACK, (0, 0, WIDTH, HEIGHT))
    pygame.draw.rect(win, GREEN, (50, 100, 300, 300), 3, 30)
    pygame.draw.line(win, GREEN, (150, 100), (150, 400), 3)
    pygame.draw.line(win, GREEN, (250, 100), (250, 400), 3)
    pygame.draw.line(win, GREEN, (50, 200), (350, 200), 3)
    pygame.draw.line(win, GREEN, (50, 300), (350, 300), 3)

    for i in range(9):
        if game.board[i] != " ":
            drawText(win, game.board[i], (i % 3, i // 3))

    pygame.display.update()
    os.system("clear")
    while game.empty_squares():
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                print(event)
                pos = ((event.pos[0] - 50) // 100, (event.pos[1] - 100) // 100)
                if (pos[0] in range(3)) and (pos[1] in range(3)) and not (pos in poses):
                    poses.append(pos)

        pos = (0, 0)

        if letter == "O":
            pos = o_player.get_move(game)
        else:
            pos = x_player.get_move(game)
        # print(pos)
        game.make_move(pos, letter)

        pygame.draw.rect(win, BLACK, (0, 0, WIDTH, HEIGHT))
        pygame.draw.rect(win, GREEN, (50, 100, 300, 300), 3, 30)
        pygame.draw.line(win, GREEN, (150, 100), (150, 400), 3)
        pygame.draw.line(win, GREEN, (250, 100), (250, 400), 3)
        pygame.draw.line(win, GREEN, (50, 200), (350, 200), 3)
        pygame.draw.line(win, GREEN, (50, 300), (350, 300), 3)

        for i in range(9):
            if game.board[i] != " ":
                drawText(win, game.board[i], (i % 3, i // 3))

        pygame.display.update()
        os.system("clear")
        print((x_win, tie, o_win))
        if game.current_winner:
            if print_game:
                # print(letter + ' wins!')
                if letter == "X":
                    x_win += 1
                else:
                    o_win += 1
                font = pygame.font.SysFont(None, 90)
                img = font.render(letter + ' WIN', True, YELLOW)
                img_rect = img.get_rect(
                center=pygame.Rect(0 ,0, 400, 100).center)
                win.blit(img, img_rect)
                pygame.display.update()
                pygame.time.delay(1000)
                game.resetGame()
                pygame.draw.rect(win, BLACK, (0, 0, WIDTH, HEIGHT))
                pygame.draw.rect(win, GREEN, (50, 100, 300, 300), 3, 30)
                pygame.draw.line(win, GREEN, (150, 100), (150, 400), 3)
                pygame.draw.line(win, GREEN, (250, 100), (250, 400), 3)
                pygame.draw.line(win, GREEN, (50, 200), (350, 200), 3)
                pygame.draw.line(win, GREEN, (50, 300), (350, 300), 3)

                for i in range(9):
                    if game.board[i] != " ":
                        drawText(win, game.board[i], (i % 3, i // 3))

                pygame.display.update()
        letter = "O" if letter == "X" else "X"  # switches player
        # for x in square:
        #     print(x)
        #     time.sleep(.8)

        if not game.empty_squares():
            # print('It\'s a tie!')
            tie += 1
            font = pygame.font.SysFont(None, 90)
            img = font.render('TIE', True, YELLOW)
            img_rect = img.get_rect(
                center=pygame.Rect(
                    0 ,0, 400, 100
                ).center
            )
            win.blit(img, img_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            game.resetGame()

    # if print_game:
    #     game.print_board_nums()

    # letter = 'X'
    # while game.empty_squares():
    #     if letter == 'O':
    #         square = o_player.get_move(game)
    #     else:
    #         square = x_player.get_move(game)
    #     if game.make_move(square, letter):

    #         if print_game:
    #             print(letter + ' makes a move to square {}'.format(square))
    #             game.print_board()
    #             print('')

    #         if game.current_winner:
    #             if print_game:
    #                 print(letter + ' wins!')
    #             return letter  # ends the loop and exits the game
    #         letter = 'O' if letter == 'X' else 'X'  # switches player

    #     time.sleep(.8)


if __name__ == "__main__":

    x_player = HumanPlayer("X")
    o_player = SmartComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
