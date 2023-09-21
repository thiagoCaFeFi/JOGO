import curses 
import time
import threading
from constantes import NOME_THE_ROGUE

def nome(stdscr, offset):  
    curses.resize_term(40, 160)
    stdscr.clear()
    curses.curs_set(0)
    alt = 40
    larg = 160

    

    for i, linha in enumerate(NOME_THE_ROGUE):
        for j in range(len(linha)):
            stdscr.addstr(alt // 2 + i - 12, larg // 2 - len(linha) // 2 + j + offset, linha[j])
            stdscr.refresh()
            time.sleep(0.001)



    max_row, max_col = stdscr.getmaxyx()
    start_row = max_row - 2  # A posição inicial da linha inferior
    # A posição final da linha inferior
    final_row = max_row - 1
    for start_col in range(max_col):
        # Desenha os personagens
        personagens = "☺ ☻ ▲"
        stdscr.addstr(start_row, start_col, personagens)
        stdscr.refresh()

        # Aguarda um curto período de tempo para criar uma animação
        time.sleep(0.1)

        # Apaga o boneco da posição atual
        stdscr.addstr(start_row, start_col, " ")
        stdscr.refresh()

        stdscr.getch()
        if start_row == final_row:
         break
    
def main(stdscr):
    offset = 0
    animation_thread = threading.Thread(target=nome, args=(stdscr, offset))
    animation_thread.start()

    # Tempo em segundos para exibir a abertura
    time.sleep(5)

if __name__ == "__main__":
    curses.wrapper(main)
