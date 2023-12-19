import pygame
from tetris import *

def update_graphics(block, next_block, playing_field, player):
    
    window.blit(background_img, (0, 0))
    pygame.draw.rect(window , gray, (off_set_x, off_set_y, playing_field_width, playing_field_height) )
    font = pygame.font.Font("Times New Roman.ttf", 40)
    rendered_text = font.render(" tetrisonator 3000", 1, black, (185, 251, 192))
    window.blit(rendered_text, (width/2-130, 16))

    player.time_since_start = int(time.time()) - int(player.start_time)
    font = pygame.font.Font("Times New Roman.ttf", 20)
    rendered_text_time =  font.render(" time: " + str(player.time_since_start) + " ", 1, black, (185, 251, 192))
    window.blit(rendered_text_time, (playing_field_width+tile_length*2, playing_field_height-80))  
    rendered_text_score = font.render(" score: " + str(player.score) + " ", 1, black, (185, 251, 192))
    window.blit(rendered_text_score, (playing_field_width+tile_length*2, playing_field_height-50))
    
    draw_small_screen(next_block)

    y = off_set_y
    for i in range(20):
        for tile in playing_field.tiles["row"+str(i+1)][y]:
            tile.draw_tile()
        y += tile_length

    for tile in block.tiles:
        if tile.y >= off_set_y:
            tile.draw_tile()

    pygame.draw.line(window , cobalt_blue, (off_set_x-2, off_set_y-3), (playing_field_width+off_set_x+1, off_set_y-3), 4)
    pygame.draw.line(window , cobalt_blue, (off_set_x-2, off_set_y+playing_field_height+1), (playing_field_width+off_set_x+1, off_set_y+playing_field_height+1), 4)
    pygame.draw.line(window , cobalt_blue, (off_set_x-3, off_set_y-3), (off_set_x-3, off_set_y+playing_field_height+1), 4)
    pygame.draw.line(window , cobalt_blue, (playing_field_width+off_set_x+1, off_set_y-3), (playing_field_width+off_set_x+1, off_set_y+playing_field_height+1), 4)

    current_y_horizontal_lines = off_set_y
    current_x_vertical_lines = off_set_x
    for i in range(19): 
        current_y_horizontal_lines += 33
        pygame.draw.line(window , gray, (off_set_x, current_y_horizontal_lines), (playing_field_width+off_set_x-1, current_y_horizontal_lines))
    for j in range(9): 
        current_x_vertical_lines += 33        
        pygame.draw.line(window , gray, (current_x_vertical_lines-1, off_set_y), (current_x_vertical_lines-1, playing_field_height+off_set_y))

    pygame.display.update()

    rendered_text = font.render(" tetrisonator 3000", 1, black, (185, 251, 192))
    window.blit(rendered_text, (width/2-100, 16))
    pygame.display.update()

def draw_small_screen(next_block):
    
    pygame.draw.rect(window , black, (playing_field_width+tile_length*2, height/2-20, 6*tile_length, 6*tile_length) )

    pygame.draw.line(window , cobalt_blue, (playing_field_width+tile_length*2-2, height/2-20-2), ((6*tile_length)+(playing_field_width+tile_length*2), (height/2-20-2)), 3)
    pygame.draw.line(window , cobalt_blue, (playing_field_width+tile_length*2-2, height/2-20+(6*tile_length)), ((6*tile_length)+(playing_field_width+tile_length*2), height/2-20+(6*tile_length)), 3)
    pygame.draw.line(window , cobalt_blue, (playing_field_width+tile_length*2-2, height/2-20-2), (playing_field_width+tile_length*2-2, height/2-20+(6*tile_length)), 3)
    pygame.draw.line(window , cobalt_blue, ((6*tile_length)+(playing_field_width+tile_length*2), height/2-20-2), ((6*tile_length)+(playing_field_width+tile_length*2), height/2-20+(6*tile_length)), 3)
        
    font = pygame.font.Font("Times New Roman.ttf", 32)
    rendered_text = font.render(" next fig ", 1, black, cobalt_blue)
    window.blit(rendered_text, (playing_field_width+tile_length*2,  height/2-70))
    
    temp_block = Block(next_block.shape, next_block.color)  
    temp_block.tiles = [Tile(playing_field_width+tile_length*2+2*tile_length, height/2-20+4*tile_length, next_block.color), Tile(0, 0, next_block.color), Tile(0, 0, next_block.color), Tile(0, 0, next_block.color)]
    temp_block.complete_block()

    for tile in temp_block.tiles:
        tile.draw_tile()

    current_y_horizontal_lines = height/2-20
    current_x_vertical_lines = playing_field_width+tile_length*2
    for i in range(5): 
        current_y_horizontal_lines += 33
        pygame.draw.line(window , gray, (playing_field_width+tile_length*2, current_y_horizontal_lines), (height/2 + (6*tile_length) + 19, current_y_horizontal_lines))
    for j in range(5): 
        current_x_vertical_lines += 33        
        pygame.draw.line(window , gray, (current_x_vertical_lines-1, height/2-20), (current_x_vertical_lines-1, height/2-20+(6*tile_length)-2))

def is_game_over(playing_field, player): 
    y = off_set_y
    for i in range(20):
        for tile in playing_field.tiles["row"+str(i+1)][y]:
            if not tile.empty and tile.y <= off_set_y: 
                temp_y = off_set_y
                for j in range(20):
                    for tile in playing_field.tiles["row"+str(j+1)][temp_y]:
                        tile.draw_tile()
                    temp_y += tile_length

                font = pygame.font.Font("Times New Roman.ttf", 48)
                rendered_text = font.render("GAME OVER", 1, ryb_red)
                window.blit(rendered_text, (off_set_x+20, playing_field_height/2))
                pygame.display.update()

                time.sleep(5)   
                introduction(player)
        y += tile_length

def start_game():    
    global best_score
    global longest_time

    rand_index = random.randint(0, 6)
    block = Block(shapes[rand_index], block_colors[rand_index])

    next_rand_index = random.randint(0, 6)
    next_block = Block(shapes[next_rand_index], block_colors[next_rand_index]) 

    playing_field = PlayingField()
    start_time = time.time()
    player = Player(start_time)

    while True:
        update_graphics(block, next_block, playing_field, player)

        (block, next_block, is_new) = block.get_new_block(next_block, playing_field, player)
        if is_new:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.event.clear()

        manage_events(block, next_block, playing_field, player)
        update_graphics(block, next_block, playing_field, player)

        block.block_is_falling(next_block, playing_field, player)
        update_graphics(block, next_block, playing_field, player)
        
        playing_field.destory_full_row(player)
        update_graphics(block, next_block, playing_field, player)

        if player.score > best_score:
            best_score = player.score
        if player.time_since_start > longest_time:
            longest_time = player.time_since_start

        is_game_over(playing_field, player)
        update_graphics(block, next_block, playing_field, player)

        pygame.display.update()
        clock.tick(60)


def manage_events(block, next_block, playing_field, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.move_left(playing_field)
            elif event.key == pygame.K_RIGHT:
                block.move_right(playing_field)
            elif event.key == pygame.K_UP:
                block.rotate(next_block, playing_field, player)
            if event.key == pygame.K_SPACE:
                block.fall_completely(next_block, playing_field, player)
            if event.key == pygame.K_DOWN:
                block.block_is_falling(next_block, playing_field, player, "faster")

    update_graphics(block, next_block, playing_field, player)


def introduction(player = None):
    button_width = 300
    button_height = 90
    
    start_x_button = width/2-button_width/2
    play_button = Button(blue, orange, -400, height/2, button_width, button_height, 32, black, white, "play")
    instructions_button = Button(cyber_yellow, ryb_red, width+150, height/2+button_height+10, button_width,button_height, 32, black, white, "idk how to play")
    quit_button = Button(green_apple, cobalt_blue, -400, height/2+button_height*2+20, button_width,button_height, 32, black, white, "quit game")
    
    font = pygame.font.Font("Times New Roman.ttf", 54)
    rendered_text = font.render("tetrisonator 3000", 1, black, purple)
    rendered_text_y = height

    while rendered_text_y > 10: 
        window.blit(background_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        rendered_text_y -= 1.5
        window.blit(rendered_text, (width/2-200, rendered_text_y))
        pygame.display.update()
    window.blit(rendered_text, (width/2-200, rendered_text_y))
    pygame.display.update()

    if player:
        font_small = pygame.font.Font("Times New Roman.ttf", 30)
        rendered_current_score = font_small.render(" last score: " + str(player.score) + " ", 1, black, orange)
        rendered_best_score = font_small.render(" best score: " + str(best_score) + " ", 1, black, ryb_red)
        rendered_current_time = font_small.render(" last time: " + str(player.time_since_start) + " ", 1, black, orange)
        rendered_longest_time = font_small.render(" longest time: " + str(longest_time) + " ", 1, black, ryb_red)

        rendered_current_score_y = height
        rendered_best_score_y = height+40
        rendered_current_time_y = height+80
        rendered_longest_time_y = height+120

        while rendered_current_score_y > 150: 
            window.blit(background_img, (0, 0))
            window.blit(rendered_text, (width/2-80, rendered_text_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            rendered_current_score_y -= 1.5
            rendered_best_score_y -= 1.5
            rendered_current_time_y -= 1.5
            rendered_longest_time_y -= 1.5

            window.blit(rendered_current_score, (off_set_x+15, rendered_current_score_y))
            window.blit(rendered_best_score, (off_set_x+15, rendered_best_score_y))
            window.blit(rendered_current_time, (off_set_x+15, rendered_current_time_y))
            window.blit(rendered_longest_time, (off_set_x+15, rendered_longest_time_y))

            pygame.display.update()

    while play_button.x < width/2-button_width/2 or instructions_button.x > width/2-button_width/2:
        window.blit(background_img, (0, 0))
        window.blit(rendered_text, (width/2-80, rendered_text_y))
        if player:
            window.blit(rendered_current_score, (off_set_x+15, rendered_current_score_y))
            window.blit(rendered_best_score, (off_set_x+15, rendered_best_score_y))
            window.blit(rendered_current_time, (off_set_x+15, rendered_current_time_y))
            window.blit(rendered_longest_time, (off_set_x+15, rendered_longest_time_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if play_button.x < width/2-button_width/2:
            play_button.x += 3
            quit_button.x += 3
        if instructions_button.x > width/2-button_width/2 :    
            instructions_button.x -= 3

        play_button.blit(window)
        instructions_button.blit(window)
        quit_button.blit(window)
        pygame.display.update()

    run = True
    while run:
        window.blit(background_img, (0, 0))
        window.blit(rendered_text, (width/2-80, rendered_text_y))
        if player:
            window.blit(rendered_current_score, (off_set_x+15, rendered_current_score_y))
            window.blit(rendered_best_score, (off_set_x+15, rendered_best_score_y))
            window.blit(rendered_current_time, (off_set_x+15, rendered_current_time_y))
            window.blit(rendered_longest_time, (off_set_x+15, rendered_longest_time_y))

        mouse_position = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(mouse_position, event):
                    start_game()
                    run = False
                elif instructions_button.is_clicked(mouse_position, event):
                    instructions(player)
                    run = False
                elif quit_button.is_clicked(mouse_position, event):
                    pygame.quit()
                    sys.exit()
        
        if play_button.is_hovered_over(mouse_position):
            play_button.blit_hovered_over(window)
        else:
            play_button.blit(window, gray)
        if instructions_button.is_hovered_over(mouse_position):
            instructions_button.blit_hovered_over(window)
        else:
            instructions_button.blit(window, gray)
        if quit_button.is_hovered_over(mouse_position):
            quit_button.blit_hovered_over(window)
        else:
            quit_button.blit(window, gray)

        clock.tick(60)
        pygame.display.update()
        font = pygame.font.Font("Times New Roman.ttf", 54)
        rendered_text = font.render("tetrisonator 3000", 1, black, purple)
        window.blit(rendered_text, (width/2-200, rendered_text_y))
        pygame.display.update()


def instructions(player = None):
    button_width = 150
    button_height = 60

    play_button = Button(blue, orange, width-150-10, height-80, button_width, button_height, 32, black, white, "PLAY >>")
    back_button = Button(orange, blue, 10, height-80, button_width, button_height, 32, black, white, "<< BACK")

    run = True
    while run:
        window.blit(instructions_img, (0, 0))
        font = pygame.font.Font("Times New Roman.ttf", 40)
        rendered_text = font.render("tetrisonator 3000", 1, black, green_apple)
        window.blit(rendered_text, (width/2-140, 10))

        mouse_position = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(mouse_position, event):
                    start_game()
                    run = False
                elif back_button.is_clicked(mouse_position, event):
                    introduction(player)
                    run = False

        instructions_label = "instructions" 
        font = pygame.font.Font("Times New Roman.ttf", 40)
        rendered_text = font.render(instructions_label, 1, black, orange)
        window.blit(rendered_text, (width/2 - rendered_text.get_width()/2, 100))
    
         
        instructions1 = "   move right:               right arrow > or (b)"  
        instructions2 = "   move left:                  left arrow < or (a)" 
        instructions3 = "   rotate:                        up arrow ^ or (w)" 
        instructions4 = "   accelerate:                  down arrow or (s)" 
        instructions5 = "   drop:                                 space( )"

        font = pygame.font.Font("Times New Roman.ttf", 20)
        rendered_text1 = font.render(instructions1, 1, black, ryb_red)
        rendered_text2 = font.render(instructions2, 1, black, orange)
        rendered_text3 = font.render(instructions3, 1, black, cyber_yellow)
        rendered_text4 = font.render(instructions4, 1, black, green_apple)
        rendered_text5 = font.render(instructions5, 1, black, blue)

        window.blit(rendered_text1, (100, 200))
        window.blit(rendered_text2, (100, 240))
        window.blit(rendered_text3, (100, 280))
        window.blit(rendered_text4, (100, 320))
        window.blit(rendered_text5, (100, 360))

        if play_button.is_hovered_over(mouse_position):
            play_button.blit_hovered_over(window)
        else:
            play_button.blit(window, gray)
        if back_button.is_hovered_over(mouse_position):
            back_button.blit_hovered_over(window)
        else:
            back_button.blit(window, gray)
        
        clock.tick(60)
        pygame.display.update()
        font = pygame.font.Font("Times New Roman.ttf", 54)
        rendered_text = font.render("tetrisonator 3000", 1, black, green_apple)
        window.blit(rendered_text, (width/2-200, 10))
        pygame.display.update()


if __name__ == "__main__":
    introduction()
    
