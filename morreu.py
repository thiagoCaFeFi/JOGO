import curses
import time

def gameOver(cavalo):
    curses.curs_set(0)
    alt, lar = cavalo.getmaxyx()
    
    texto = [
        " __      __                  //\\     __  __                                      ",
        " \\ \\    / /                 |/ \\   |  \\/  |                                      ",
        "  \\ \\  / /    ___     ___    ___    | \\  / |   ___    _ __   _ __    ___   _   _ ",
        "   \\ \\/ /    / _ \\   / __|  / _ \\   | |\\/| |  / _ \\  | '__| | '__|  / _ \\ | | | |",
        "    \\  /    | (_) | | (__  |  __/   | |  | | | (_) | | |    | |    |  __/ | |_| |",
        "     \\/      \\___/   \\___|  \\___|   |_|  |_|  \\___/  |_|    |_|     \\___|  \\__,_|",
        "                                                                                 ",
        "                                                                                 "
    ]
    
    x = lar // 2 - len(texto[0]) // 2
    y = alt // 2
    
    for i, line in enumerate(texto):
        cavalo.addstr(y + i, x, line)
    
    cavalo.refresh()
    time.sleep(3)

def chama(rabo):
    rabo.clear()
    gameOver(rabo)

curses.wrapper(chama)
