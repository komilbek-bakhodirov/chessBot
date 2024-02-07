def draw_pieces(screen, board, images, square_size):
    for i in range(8):  # Rows
        for j in range(8):  # Columns
            square = i * 8 + j
            piece = board.piece_at(square)
            if piece:
                # Construct the key for accessing the piece image
                color = 'white' if piece.color else 'black'
                piece_type = piece.symbol().lower()
                if piece_type.isupper():  # White pieces are uppercase
                    piece_type = 'king' if piece_type == 'k' else \
                                'queen' if piece_type == 'q' else \
                                'rook' if piece_type == 'r' else \
                                'bishop' if piece_type == 'b' else \
                                'knight' if piece_type == 'n' else \
                                'pawn'
                else:  # Black pieces
                    piece_type = 'king' if piece_type == 'k' else \
                                'queen' if piece_type == 'q' else \
                                'rook' if piece_type == 'r' else \
                                'bishop' if piece_type == 'b' else \
                                'knight' if piece_type == 'n' else \
                                'pawn'
                key = f"{color}-{piece_type}"

                # Now, use the key to access the image
                piece_image = images.get(key)
                if piece_image:
                    x = j * square_size
                    y = i * square_size
                    screen.blit(piece_image, (x, y))
