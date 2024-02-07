import chess


def evaluate_board(board):
    # Define piece_values at the start of the function to ensure it is accessible throughout
    piece_values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}

    if board.is_checkmate():
        if board.turn:
            return -9999  # Black wins, bad for white
        else:
            return 9999   # White wins, bad for black
    if board.is_stalemate():
        return 0  # Draw is neutral
    if board.is_insufficient_material():
        return 0  # Draw due to insufficient material is neutral

    # Calculate score based on material value
    score = 0
    for piece_type in piece_values:
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    # Adjust score for the current player's perspective
    return score if board.turn == chess.WHITE else -score



def minimax(board, depth, is_maximizing_player):
    # Your minimax function here
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval
    pass


def select_best_move(board, depth):
    # Use the minimax function to select the best move
    best_move = None
    best_value = float('-inf') if board.turn == chess.WHITE else float('inf')

    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, board.turn == chess.BLACK)
        board.pop()

        if board.turn == chess.WHITE and board_value > best_value:
            best_value = board_value
            best_move = move
        elif board.turn == chess.BLACK and board_value < best_value:
            best_value = board_value
            best_move = move

    return best_move
    pass
