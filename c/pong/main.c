#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdbool.h>

// Screen size
const int width = 800;
const int height = 600;

// Loop variable
bool running = true;

// Ball
const int ball_size = 20;
SDL_Rect ball = {
    .x = width/2-ball_size/2,
    .y = height/2-ball_size/2,
    .w = ball_size,
    .h = ball_size,
};

int main (int argc, char *argv[]) {
    // Init SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        printf("Failed to initialize SDL!\n");
        printf("%s\n", SDL_GetError());
    }

    // Create window and renderer
    SDL_Window *window = SDL_CreateWindow("Pong", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    // Main loop
    while (running) {
        // Event checker
        SDL_Event e;
        while (SDL_PollEvent(&e)) {
            switch (e.type) {
                case SDL_QUIT:
                    running = false;
                    break;
            }
            
        }


        ball.x += 1;
        ball.y += 1;

        // Clear window
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        // Blitters ;)
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &ball);

        SDL_Delay(1000/120);
        SDL_RenderPresent(renderer);
    }

    exit(0);
    SDL_Quit();
    return 0;
}
