""" 
	Author: Steven Tran
	Date: January 10, 2019
	File Description: This program is a classic snake game coded in Python using
	the curses module to assist in creating new windows and registering key 
	presses as input from the user to count as actions within the game.
	Sources used: YouTube, geeksforgeeks, docs.python, and stackoverflow
"""

import random # Random generation of food on the screen
import curses # Curses library for screen painting and keyboard handling

score = 0

# Initialize the screen
screen = curses.initscr()

# Set the curser to 0 to not show up on the screen
curses.curs_set(0)

# Get width and height of the terminal window
sheight, swidth = screen.getmaxyx()

# Create a application window with the same terminal window dimensions
window = curses.newwin(sheight, swidth, 0, 0)

# Enables keypad input
window.keypad(True)

# Sets the speed of the snake by adjustingthe window refrsh rate
# Bigger number, slower game.
window.timeout(70)

snk_x = swidth / 4
snk_y = sheight / 2

# The snake itself is a list of lists where the second list is coordinates
snake = [
	[snk_y, snk_x],
	[snk_y, snk_x - 1],
	[snk_y, snk_x - 2]
]

# First food location of character PI
food = [sheight/2, swidth/2]
window.addch(food[0], food[1], curses.ACS_PI)

# Set initial direction of the snake to be pointing to the right
key = curses.KEY_RIGHT

# Game loop
while True:
	# Collect user action UP, DOWN, LEFT, RIGHT
	next_key = window.getch()
	key = key if next_key == -1 else next_key

	 # Base cases for when the game should end or you lose
	 #	- The snake reaches the height border
	 #	- The snake reaches the width border
	 #	- The snake turns into itself
	if snake[0][0] in [0, sheight] or snake[0][1] in [0, swidth] or snake[0] in snake[1:]:
		curses.endwin()
		print("END GAME")
		print("SCORE: %d" % (score))
		quit()

	new_head = [snake[0][0], snake[0][1]]	

	if key == curses.KEY_DOWN:
		new_head[0] += 1

	if key == curses.KEY_UP:
		new_head[0] -= 1
	
	if key == curses.KEY_LEFT:
		new_head[1] -= 1		

	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)
	
	# If the head of the snake is at the food...
	if snake[0] == food:
		food = None
		while food is None:
			nf = [
				random.randint(1, sheight - 1),
				random.randint(1, swidth - 1)
			]	

			# if nf not in snake else None
			if nf not in snake:
				food = nf
		
		# Add a food character to the screen PI
		score += 1
		window.addch(food[0], food[1], curses.ACS_PI)
	else:
		tail = snake.pop()
		# Set the trail of the snake to be blank
		window.addch(tail[0], tail[1], ' ')

	window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)			




