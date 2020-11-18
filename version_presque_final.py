import microbit
import random

def move_conditions(condition_position_x, condition_position_y, list_position,chance_direction_change, last_movement = None, accelerometer = None):
    #the position of the visor can now be inputed in conditon x and y, last movement needs to be none type for the visor to move 
    if int(condition_position_x) == 4 and int(condition_position_y) == 4:
        move_set = 0
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif int(condition_position_x) == 0 and int(condition_position_y) == 4:
        move_set = 1
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif int(condition_position_x) == 0 and int(condition_position_y) == 0:
        move_set = 2
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif int(condition_position_x) == 4 and int(condition_position_y) == 0:
        move_set = 3
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif (0 < int(condition_position_x) < 4) and int(condition_position_y) == 0:
        move_set = 4
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif (0 < int(condition_position_x) < 4) and int(condition_position_y) == 4:
        move_set = 5
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif (0 < int(condition_position_y) < 4) and int(condition_position_x) == 0:
        move_set = 6
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    elif (0 < int(condition_position_y) < 4) and int(condition_position_x) == 4:
        print('here too')
        move_set = 7
        position_checker(list_position, last_movement, chance_direction_change, move_set, accelerometer)
    else:  
        if accelerometer != None:
            direction_generator = accelerometer 
            move_possible(list_position, direction_generator) 
        else:
            direction_generator = randint(0, 4)
        if chance_direction_change == 5:        
            move_possible(list_position, direction_generator)
            last_movement = direction_generator
        else:
            move_possible(list_position, last_movement)   
            last_movement = last_movement 

def move_possible(current_position, direction):
    #if acceleromteter is == to none type function is being used to move visor 

    if  direction == 0:
        current_position = current_position 
    elif direction == 1 and current_position[1] >= 0:
        current_position[1] = current_position[1] - 1
        
    elif direction == 2 and current_position[1] <= 4:
        
        current_position[1] =  int(current_position[1])  + 1
    elif direction == 3 and current_position[0] <= 4:
        
        current_position[0] = int(current_position[0])  + 1
    elif direction == 4 and current_position[0] >= 0:
        
        current_position[0] = int(current_position[0])  - 1
    
    
    return current_position
     
def position_checker(position, last_movement, chance_direction_change, move_set, accelerometer):

    #acceleromter 
    visor_move_list = [[1,0,0,4],[1,0,3,0], [0,2,3,0],[0,2,0,4], [0,2,3,4], [1,0,3,4], [1,2,3,0], [1,2,0,4]]
    direction_generator_corner = randint(0, 2)
    
    direction_generator_wall = randint(0, 3)
    out_of_bound_list = [[2,3],[2,4], [1, 4], [1,3], [1], [2], [4], [3]]
    allowed_moves = [[0, 1, 4],[0,1,3], [0,2,3], [0,2,4], [0,2,3,4], [0,1,3,4], [0,1,2,3], [0,1,2,4]]


    if accelerometer != None:
        print('it works till here')
        accelerometer = accelerometer - 1
        direction_generator = visor_move_list[move_set][accelerometer]
        move_possible(position, direction_generator)

    elif chance_direction_change != 5 and (last_movement not in out_of_bound_list[move_set]):
        direction_generator = last_movement
        move_possible(position, direction_generator)
    else:
        if len(out_of_bound_list[move_set]) == 2: 
              
            move = allowed_moves[move_set][direction_generator_corner]  
           
            move_possible(position, move)
        else:
           
            move_possible(position, allowed_moves[move_set][direction_generator_wall])
    return(position)

'''# definition of functions
..........
..........
..........'''

# settings
target_x = 2
target_y = 2
nb_submarines = 4
submarine_life = 2

# create board and place submarines
dico = []
def dict_submarine_generator(dict_submarine, nb_submarine, submarine_life):
    for element in range(nb_submarine):
        x = randint(0,4)
        y = randint(0,4)
        z = randint(1,4)
        dict_submarine.append({"health" : submarine_life, "position": [x,y], "last_movement" : z})
    return dico  

dict_submarine_generator(dico, 4, 2)

# show where target is right now

for element in range(4):
  display.set_pixel((dico[element]['position'][0]), (dico[element]['position'][1]), 9)

    
# loop until game is over
game_is_over = False

while not game_is_over:
    # loop until an action is chosen (fire or sonar)
    order = None
    while True:
        # check if a button is pressed, the micro:bit is moved, etc.

        'move visor will come in here'

        if button_a.is_pressed():
            order = fire
        elif button_b.is_pressed():
            order = sonar

        
        

        # wait a few milliseconds before checking again
        microbit.sleep(500)
   
    # execute order (fire or sonar)
        if order == fire:
            def fire_btton_a():
            
                for submarine in range(len(dico)):
                
                if position_visor == dico[submarine]['position']:
                    dico[submarine]['health'] = dico[submarine]['health'] - 1
                    if dico[submarine]['health'] == 0:
                        list_dead.append(submarine)
                        
                print(list_dead)

                for number in list_dead:
                
                    if len(list_dead) == 1:
                        dico.remove(dico[list_dead[0]])
                    else:
                        dico.remove(dico[list_dead[0]])
        elif order == sonar:
            for element in range(4):
                display.set_pixel((dico[element]['position'][0]), (dico[element]['position'][1]), 9)
                sleep(2500)
                display.clear()
    
    # wait a few seconds and clear screen
    microbit.sleep(2500)
    microbit.display.clear()
    
    # check if game is not over
    if len(dico) == 0:
        game_is_over = True
    
    if not game_is_over:
	    # update position of submarines
        for element in range(4): 
            #here 4 is going to be replaced with the nb of remaining submarines that are alive
            '''This is the function to set limits and make one mouvement,
            for the direction generator the following applies:
            0 is stay in place
            1 is up
            2 is down
            3 is right
            4 is left
            '''
            sub_name = element   
            list_position = dico[sub_name]["position"]
            last_movement = dico[sub_name]['last_movement']   
            chance_move_freeze = randint(0, 1)     
            chance_direction_change = randint(0, 9)
            direction_generator_corner = randint(0, 2)
            direction_generator_wall = randint(0, 3)

            if chance_move_freeze == 1:
            
                move_conditions(list_position[0], list_position[1], list_position, chance_direction_change, last_movement, None)

	    # update direction of submarines
	    ..........

# tell that the game is over
microbit.display.scroll('You have won!!!', delay=100)
