import curses
from curses import wrapper

class Menu:
    def __init__(self, stdscr, title, items):
        self.stdscr = stdscr
        self.title = title
        self.items = items
        self.terms = {}

    def writeWord(self, y, x, word):
        self.stdscr.addstr(y, x, word[0], curses.A_UNDERLINE)
        self.stdscr.addstr(y, x+1, word[1:])

    def makeMenu(self):
        self.stdscr.clear()
        self.stdscr.addstr(3, 10, self.title)
        i = 5

        for item in self.items:
            self.writeWord(i, 10, item)
            i +=1

        self.stdscr.refresh()
        key = self.stdscr.getkey()
        self.handleChoice(key)

    def handleChoice(self, key):
        match key:
            case "a":
                self.addCard()
            case "t":
                self.test()
            case "q":
                quit()

        self.makeMenu()


    def addCard(self):
        self.stdscr.clear()
        self.stdscr.addstr(0,0, 'What Term would you want to add?')
        self.stdscr.refresh()
        term = self.stdscr.getstr(1,0, 16)
        self.stdscr.clear()
        self.stdscr.addstr(0,0, f'What is the definition of {term}')
        self.stdscr.refresh()
        definition = self.stdscr.getstr(1,0, 64)
        self.terms[term] = definition
        self.makeMenu()

    def test(self):
        score = 0
        total = len(self.terms)
        for term in self.terms:
            self.stdscr.clear()
            self.stdscr.addstr(0,0, f'What is the definition of {term}')
            self.stdscr.addstr(1,0, '(press any key to see answer)')
            self.stdscr.refresh()
            self.stdscr.getkey()

            self.stdscr.clear()
            self.stdscr.addstr(0,0, f'the definition of {term} was: {self.terms[term]}')
            self.stdscr.addstr(1,0, f'{self.terms[term]}')
            self.stdscr.addstr(2,0, 'Was your answer correct? (y/n)')
            self.stdscr.refresh()
            answer = self.stdscr.getkey()
            if answer == "y":
                score += 1

        self.stdscr.clear()
        self.stdscr.addstr(0,0, f'You had {score} correct answers out of {total} ({score*100/total}%)')
        self.stdscr.addstr(1,0, '(press any key to go back to the main menu)')
        self.stdscr.refresh()
        self.stdscr.getkey()



def main(stdscr):
    title = 'What do you want to do?'
    items = [ 'Add Card', 'Test Myself', 'Quit' ]
    mainMenu = Menu(stdscr, title, items)
    mainMenu.makeMenu()

wrapper(main)
