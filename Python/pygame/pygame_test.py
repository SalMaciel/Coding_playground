# Import module
import pygame

# Define a main function
def main():

    # Initialize the pygame
    pygame.init()
    # Load and set the logo
    logo = pygame.image.load("images/logo-32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # Create a surface on screen 240 x 180
    screen = pygame.display.set_mode((240,180))
    
    # First blit, load image
    image = pygame.image.load("images/01_image.png")
    
    # blit image to screen
    screen.blit(image, (50,50))
    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()

    # Define a variable to control the main loop
    running = True
    
    # Main loop
    while running:
        # Event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit main loop
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()