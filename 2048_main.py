import random as r

def initialize_game():
  grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  rules = "Enter w to shift the board up \n Enter s to shift the board right \n Enter z to shift the board down \n Enter a to shift the board left" 
  for i in range(2):
    add_new_tile(grid)
  print(rules)
  print_grid(grid)
  while keep_playing(grid):
    make_move(grid)
  
def print_grid(grid):
  #print each row of the grid on a new line- https://www.kite.com/python/answers/how-to-print-a-list-of-lists-in-columns-in-python
  list_length = [len(str(element)) for row in grid for element in row]
  col_width = max(list_length)

  for row in grid:
      row = "".join(str(element).ljust(col_width+2) for element in row)
      print(row)

def add_new_tile(grid):
  #choose random position on grid
  x = r.randint(0,3)
  y = r.randint(0,3)
  tile_value = r.randint(0,1)
  tile_added = False
  while tile_added == False:
    for i in range(4):
        for j in range(4):
            if grid[x][y] == 0:
                if tile_value == 0:
                    grid[x][y] = 2
                    tile_added = True
                else:
                    grid[x][y] = 4
                    tile_added = True
            False


def make_move(current_grid):
  move = input("Which direction do you want to shift the board? ")

  if move == "w":
    print("move up")
  elif move == "s":
    move_right(current_grid)
  elif move == "z":
    print("move down")
  elif move == "a":
    print("move left")
  else:
    print("Invalid key. Enter a valid move.")
    make_move(current_grid)

#shifts tiles to the right without combining them
def push_board(grid):
   new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
   done = False
   for x in range(4):
      count = 3
      for y in range(count, -1, -1):
         if grid[x][y] != 0:
            new_grid[x][count] = grid[x][y]
            if y != count:
               done = True
            count -= 1
   return (new_grid, done)

#add together and merge tiles with the same value
def merge(grid):
   score = 0
   done = False
   cells = 4
   for x in range(cells):
      for y in range(cells -1, 0 , -1):
         if grid[x][y] == grid[x][y-1] and grid[x][y] != 0:
            grid[x][y] = grid[x][y] * 2
            score += grid[x][y]
            grid[x][y-1]=0
            done = True
   return (grid, done)

def move_right(current_grid):
  new_grid,done = push_board(current_grid)
  new_grid,done = merge(new_grid)
  new_grid,done = push_board(new_grid)
  add_new_tile(new_grid)
  print_grid(new_grid)
  return new_grid

def keep_playing(grid):
  for x in range(4):
    for y in range(4):
      #User has reached 2048 on a tile
      if(grid[x][y] == 2048):
        print("You win!")
        return False
      #There is at least one empty space on the grid left
      elif(grid[x][y] == 0):
        return True
      else:
        #Merging in one direction will still combine some tiles
        for x in range(3):
          for y in range(3):
            if(grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x][y+1]):
              return True
        for x in range(3):
          if(grid[x][3] == grid[x+1][x]):
            return True
        for y in range(3):
          if(grid[3][y] == grid[3][y+1]):
            return True
        print("No more moves. You lose.")
        return False


initialize_game()



