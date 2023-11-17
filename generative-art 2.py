import librosa
import numpy as np
import pygame
import math


# Function 1: Load audio file and extract audio data
def load_audio(file_path):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    return audio_data, sample_rate


# Function 2: Detect beats in the audio data
def detect_beats(audio_data, sample_rate):
    # Here you can implement your preferred beat detection algorithm
    # For now, we'll generate some dummy beat values
    beats = [0.5, 1.2, 1.8, 2.5, 3.1, 3.8, 4.4]
    return beats


# Function 3: Generate visual patterns based on beats
def generate_visuals(beats):
    visual_patterns = []
    for i in range(len(beats)):
        if i > 0:
            # Calculate the beat duration
            duration = beats[i] - beats[i - 1]
            visual_patterns.append(duration)
    return visual_patterns


# Function 4: Play the audio file
def play_sound(sample_rate, file_path):
    try:
        pygame.mixer.init(sample_rate)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except Exception as e:
        print("An error occurred during audio playback:", e)


# Function 5: Display the visual patterns on screen
def display_visuals(visual_patterns):
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Trippy Visualizer")

    # Define variables for visualization
    x_values = np.linspace(0, screen_width, len(visual_patterns))
    y_values = (screen_height / 2) + np.array(visual_patterns) * (screen_height / 2)
    points = np.column_stack((x_values, y_values))

    # Define initial colors
    background_color = (0, 0, 0)  # Black
    line_color = (255, 255, 255)  # White

    # Additional variables for enhanced visuals
    angle = 0
    scale = 1
    scale_direction = 1

    # Main visualization loop
    running = True
    index = 0  # Index to track the current position
    clock = pygame.time.Clock()  # Create a clock object for controlling the frame rate

    try:
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit the loop when the window is closed

            # Fill the background with the current color
            screen.fill(background_color)

            # Check if there are at least 2 points to draw a line
            if len(points) >= 2:
                # Get the current position
                current_position = points[index]

                # Draw a line from the previous position to the current position
                if index > 0:
                    prev_position = points[index - 1]
                    pygame.draw.line(screen, line_color, prev_position, current_position, 2)

                # Update the current position
                index = (index + 1) % len(points)

            # Draw a rotating and scaling circle
            circle_radius = int(abs(math.sin(visual_patterns[index])) * 100) + 10
            circle_color = (int(abs(math.sin(visual_patterns[index])) * 255),
                            int(abs(math.cos(visual_patterns[index])) * 255),
                            int(abs(math.tan(visual_patterns[index])) * 255))
            rotated_circle = pygame.transform.rotate(pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA), angle)
            scaled_circle = pygame.transform.scale(rotated_circle, (int(rotated_circle.get_width() * scale), int(rotated_circle.get_height() * scale)))
            screen.blit(scaled_circle, (screen_width // 2 - scaled_circle.get_width() // 2, screen_height // 2 - scaled_circle.get_height() // 2))
            angle += 1
            scale += 0.01 * scale_direction
            if scale > 2 or scale < 0.5:
                scale_direction *= -1

            # Draw pulsating shapes around the center
            shape_radius = int(abs(math.sin(visual_patterns[index])) * 100) + 10
            num_shapes = 6
            shape_color = (int(abs(math.tan(visual_patterns[index])) * 255),
                           int(abs(math.sin(visual_patterns[index])) * 255),
                           int(abs(math.cos(visual_patterns[index])) * 255))
            for i in range(num_shapes):
                shape_angle = i * (360 / num_shapes) + visual_patterns[index] * 360
                x = screen_width // 2 + int(math.cos(math.radians(shape_angle)) * shape_radius)
                y = screen_height // 2 + int(math.sin(math.radians(shape_angle)) * shape_radius)
                pygame.draw.circle(screen, shape_color, (x, y), shape_radius)

            # Draw rotating lines around the center
            line_length = int(abs(math.cos(visual_patterns[index])) * 50) + 10
            num_lines = 12
            for i in range(num_lines):
                line_angle = i * (360 / num_lines) + visual_patterns[index] * 360
                x1 = screen_width // 2 + int(math.cos(math.radians(line_angle)) * shape_radius)
                y1 = screen_height // 2 + int(math.sin(math.radians(line_angle)) * shape_radius)
                x2 = screen_width // 2 + int(math.cos(math.radians(line_angle)) * (shape_radius + line_length))
                y2 = screen_height // 2 + int(math.sin(math.radians(line_angle)) * (shape_radius + line_length))
                pygame.draw.line(screen, shape_color, (x1, y1), (x2, y2), 2)

            # Update the screen
            pygame.display.flip()

            clock.tick(30)  # Limit the frame rate to 30 FPS

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("An error occurred during visualization:", e)
    finally:
        # Quit Pygame
        pygame.quit()


def display_visuals_2(visual_patterns):
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Trippy Visuals")

    # Define variables for visualization
    x_values = np.linspace(0, screen_width, len(visual_patterns))
    y_values = (screen_height / 2) + np.array(visual_patterns) * (screen_height / 2)
    points = np.column_stack((x_values, y_values))

    # Define initial colors
    background_color = (0, 0, 0)  # Black

    # Additional variables for enhanced visuals
    scale = 1
    scale_direction = 1

    # Main visualization loop
    running = True
    index = 0  # Index to track the current position
    clock = pygame.time.Clock()  # Create a clock object for controlling the frame rate

    try:
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit the loop when the window is closed

            # Fill the background with the current color
            screen.fill(background_color)

            # Check if there are at least 2 points to draw a line
            if len(points) >= 2:
                # Get the current position
                current_position = points[index]

                # Draw a line from the previous position to the current position
                if index > 0:
                    prev_position = points[index - 1]
                    pygame.draw.line(screen, (255, 255, 255), prev_position, current_position, 2)

                # Update the current position
                index = (index + 1) % len(points)

            # Draw pulsating circles
            circle_radius = int(abs(math.sin(visual_patterns[index])) * 100) + 10
            circle_color = (int(abs(math.sin(visual_patterns[index])) * 255),
                            int(abs(math.cos(visual_patterns[index])) * 255),
                            int(abs(math.tan(visual_patterns[index])) * 255))
            num_circles = 10
            for i in range(num_circles):
                angle = (i / num_circles) * 2 * math.pi
                x = screen_width // 2 + int(math.cos(angle) * 200)
                y = screen_height // 2 + int(math.sin(angle) * 200)
                pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

            # Draw rotating squares
            square_size = int(abs(math.sin(visual_patterns[index])) * 100) + 10
            square_color = (int(abs(math.cos(visual_patterns[index])) * 255),
                            int(abs(math.tan(visual_patterns[index])) * 255),
                            int(abs(math.sin(visual_patterns[index])) * 255))
            num_squares = 8
            for i in range(num_squares):
                angle = (i / num_squares) * 2 * math.pi + visual_patterns[index] * 2 * math.pi
                x = screen_width // 2 + int(math.cos(angle) * 300)
                y = screen_height // 2 + int(math.sin(angle) * 300)
                pygame.draw.rect(screen, square_color, (x - square_size // 2, y - square_size // 2, square_size, square_size))

            # Update scaling factor
            scale += 0.01 * scale_direction
            if scale > 2 or scale < 0.5:
                scale_direction *= -1

            # Draw rotating polygons
            polygon_radius = int(abs(math.sin(visual_patterns[index])) * 100) + 10
            num_sides = 6
            polygon_color = (int(abs(math.tan(visual_patterns[index])) * 255),
                             int(abs(math.sin(visual_patterns[index])) * 255),
                             int(abs(math.cos(visual_patterns[index])) * 255))
            for i in range(num_sides):
                angle = (i / num_sides) * 2 * math.pi + visual_patterns[index] * 2 * math.pi
                x = screen_width // 2 + int(math.cos(angle) * 400 * scale)
                y = screen_height // 2 + int(math.sin(angle) * 400 * scale)
                pygame.draw.polygon(screen, polygon_color, [(x + polygon_radius, y),
                                                             (x, y - polygon_radius),
                                                             (x - polygon_radius, y),
                                                             (x, y + polygon_radius)])

            # Update the screen
            pygame.display.flip()

            clock.tick(30)  # Limit the frame rate to 30 FPS

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("An error occurred during visualization:", e)
    finally:
        # Quit Pygame
        pygame.quit()



# Helper function to ask a yes/no question and validate the response
def ask_yes_no_question(question):
    while True:
        answer = input(question + " (Yes/No): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please enter either 'Yes' or 'No'")

def main():
    # Ask the user about their day
    while True:
        edm_day = ask_yes_no_question("Would you like to have a great day filled with EDM beats?")
        if edm_day:
            break
        else:
            print("That's alright. Maybe some other time!")

    # Ask the user about their relaxation preference
    while True:
        edm_concert = ask_yes_no_question("Would you like to experience the energy of an EDM concert?")
        if edm_concert:
            break
        else:
            print("No problem. There are other ways to relax and enjoy.")

    # Ask the user to choose the red pill or the blue pill
    while True:
        pill_choice = input("Would you like to take the red pill or the blue pill? (Type 'red' or 'blue'): ")
        if pill_choice.lower() in ['red', 'blue']:
            break
        print("Invalid choice. Please enter 'red' or 'blue'.")

    print("Great! Let's dive into the world of EDM.")


    # Step 1: Load audio file
    file_path = "mixkit-infected-vibes-157.wav"
    audio_data, sample_rate = load_audio(file_path)

    # Step 2: Detect beats in the audio data
    beats = detect_beats(audio_data, sample_rate)

    # Step 3: Generate visual patterns
    visual_patterns = generate_visuals(beats)

    # Step 4: Play the audio and display the visuals based on pill choice
    play_sound(sample_rate, file_path)

    if pill_choice.lower() == 'red':
        display_visuals(visual_patterns)
    else:
        display_visuals_2(visual_patterns)


# Call the main function
if __name__ == "__main__":
    main()
