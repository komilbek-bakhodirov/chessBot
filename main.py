from chess_logic import select_best_move
import chess


def main():
    board = chess.Board()
    print(board)
    move = select_best_move(board, 3)  # Adjust the depth as needed
    if move:
        board.push(move)
    print(board)


if __name__ == "__main__":
    main()
