#include <SDL2/SDL.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

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
int ball_velx = -1;
int ball_vely = 1;
void ball_collisions(void);

// Paddles
const int paddle_width = 20;
const int paddle_height = 100;
void paddle_movement(void);

// Paddle 1
SDL_Rect paddle1 = {
    .x = 0,
    .y = height/2-paddle_height/2,
    .w = paddle_width,
    .h = paddle_height,
};
int paddle1_vel = 0;

// Paddle 2
SDL_Rect paddle2 = {
    .x = width-paddle_width,
    .y = height/2-paddle_height/2,
    .w = paddle_width,
    .h = paddle_height,
};
int paddle2_vel = 0;

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
            if (e.type == SDL_QUIT) {
                running = false;
            }
            if (e.type == SDL_KEYDOWN) {
                switch (e.key.keysym.sym) {
                    case SDLK_COMMA:
                        paddle1_vel = -1;
                        break;
                    case SDLK_o:
                        paddle1_vel = 1;
                        break;
                    case SDLK_UP:
                        paddle2_vel = -1;
                        break;
                    case SDLK_DOWN:
                        paddle2_vel = 1;
                        break;
                }
            }
            if (e.type == SDL_KEYUP) {
                switch (e.key.keysym.sym) {
                    case SDLK_COMMA:
                        paddle1_vel = 0;
                        break;
                    case SDLK_o:
                        paddle1_vel = 0;
                        break;
                    case SDLK_UP:
                        paddle2_vel = 0;
                        break;
                    case SDLK_DOWN:
                        paddle2_vel = 0;
                        break;
                }
            }
        }

        ball_collisions();

        paddle_movement();

        // Clear window
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        // Blitters ;)
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &ball);
        SDL_RenderFillRect(renderer, &paddle1);
        SDL_RenderFillRect(renderer, &paddle2);

        SDL_Delay(1000/240);
        SDL_RenderPresent(renderer);
    }

    exit(0);
    SDL_Quit();
    return 0;
}

void ball_collisions(void) {
    ball.x += ball_velx;
    ball.y += ball_vely;

    // Paddle collisions
    if (ball.x + ball_velx <= paddle1.x + paddle_width &&
            ball.x + ball_size + ball_velx >= paddle1.x &&
            ball.y + ball_vely <= paddle1.y + paddle_height &&
            ball.y + ball_size + ball_vely >= paddle1.y) {
        if (ball_velx < 0) {
            if (abs(ball.x - (paddle1.x + paddle_width)) < 10) {
                ball_velx *= -1;
            } else if (abs((ball.y + ball_size) - paddle1.y) < 10 &&
                    ball_vely > 0) {
                ball_vely *= -1;
            } else if (abs(ball.y - (paddle1.y + paddle_height)) < 10 &&
                    ball_vely < 0) {
                ball_vely *= -1;
            }
        }
    } else if (ball.x + ball_velx <= paddle2.x + paddle_width &&
            ball.x + ball_size + ball_velx >= paddle2.x &&
            ball.y + ball_vely <= paddle2.y + paddle_height &&
            ball.y + ball_size + ball_vely >= paddle2.y) {
        if (ball_velx > 0) {
            if (abs((ball.x + ball_size) - paddle2.x) < 10) {
                ball_velx *= -1;
            } else if (abs((ball.y + ball_size) - paddle2.y) < 10 &&
                    ball_vely > 0) {
                ball_vely *= -1;
            } else if (abs(ball.y - (paddle2.y + paddle_height)) < 10 &&
                    ball_vely < 0) {
                ball_vely *= -1;
            }
        }
    }

    // Wall collisions
    if (ball.x + ball_size + ball_velx >= width || 
            ball.x + ball_velx <= 0) {
        ball.x = width/2-ball_size/2;
        ball.y = height/2-ball_size/2;
    } else if (ball.y + ball_size + ball_vely >= height || 
            ball.y + ball_vely <= 0) {
        ball_vely *= -1;
    }
}

void paddle_movement(void) {
    paddle1.y += paddle1_vel;
    paddle2.y += paddle2_vel;
}
