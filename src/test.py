from asciimatics.screen import Screen

def draw_map(screen):
    # Define the map as a list of strings
    map_data = [
        "#########",
        "#.......#",
        "#...#...#",
        "#.......#",
        "#########"
    ]

    # Draw the map on the screen
    for y, row in enumerate(map_data):
        screen.print_at(row, 0, y)

    # Refresh to show the changes
    screen.refresh()

    # Wait for input before exiting
    screen.wait_for_input(10.0)
    
Screen.wrapper(draw_map)