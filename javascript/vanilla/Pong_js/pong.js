const canvas = document.getElementById('pong');
const ctx = canvas.getContext('2d');

const paddle1_size = [25, 125];
let paddle1_pos = [0, canvas.height/2-paddle1_size[1]/2];
let paddle1_vel = 0;
let p1_score = 0;

const paddle2_size = [25, 125]
let paddle2_pos = [canvas.width-paddle2_size[0], canvas.height/2-paddle1_size[1]/2];
let paddle2_vel = 0
let p2_score = 0

const ball_size = 25
let ball_pos = [canvas.width/2-ball_size/2, canvas.height/2-ball_size/2];
let ball_vel = [5, 5];

let current_time = 0
let score_time = 0

let winner = 0

let game_active = false

let ping = new Audio('ping.mp3');

let pong = new Audio('pong.mp3')

let HEEHEEHEEHAW = new Audio('HEEHEEHEEHAW.mp3');

let random_sound = [Math.floor(Math.random() * 2)]


document.addEventListener('keydown', function(event) {
    if(event.keyCode == 87 && game_active == true) { // w
        paddle1_vel = -5;
    }; 
    if(event.keyCode == 83 && game_active == true) { // s
        paddle1_vel = 5;
    };
    if(event.keyCode == 38 && game_active == true) { // up arrow
        paddle2_vel = -5;
    };
    if(event.keyCode == 40 && game_active == true) { // down arrow
        paddle2_vel = 5;
    };
    if(event.keyCode == 32 && game_active == false) { // space
        paddle1_pos = [0, canvas.height/2-paddle1_size[1]/2];
        paddle1_vel = 0;
        p1_score = 0;
        paddle2_pos = [canvas.width-paddle2_size[0], canvas.height/2-paddle1_size[1]/2];
        paddle2_vel = 0
        p2_score = 0;
        ball_pos = [canvas.width/2-ball_size/2, canvas.height/2-ball_size/2];
        ball_vel = [5, 5];
        score_time = parseInt(current_time)
        game_active = true;
    };
    if(event.keyCode == 27 && game_active == true) {
        game_active = false
        score_time = 0
        winner = 0
    };
    
});

    document.addEventListener('keyup', function(event) {
        if(event.keyCode == 87 && game_active == true) { // w
            paddle1_vel = 0;
        } 
        if(event.keyCode == 83 && game_active == true) { // s
            paddle1_vel = 0;
        }
        if(event.keyCode == 38 && game_active == true) { // up arrow
            paddle2_vel = 0;
        }
        if(event.keyCode == 40 && game_active == true) { // down arrow
            paddle2_vel = 0;
        }
    });

function draw_rect(x, y, w, h, rgb) {
    ctx.beginPath();
    ctx.rect(x, y, w, h);
    ctx.fillStyle = rgb;
    ctx.fill();
    ctx.closePath();

};

function draw_text(text, x, y, size) {
    ctx.font = `${size}px Arial`;
    ctx.fillStyle = 'rgb(255, 255, 255)';
    ctx.fillText(text, x, y);
};

function ball_restart(){
    ball_pos = [canvas.width/2-ball_size/2, canvas.height/2-ball_size/2];

    if(parseInt(current_time - score_time) < 1000){
        draw_text('3', canvas.width/2-10, canvas.height/2-50, 40)
    };
    if((parseInt(current_time - score_time) > 1000) && (parseInt(current_time - score_time) < 2000)){
        draw_text('2', canvas.width/2-10, canvas.height/2-50, 40)
    };
    if((parseInt(current_time - score_time) > 2000) && (parseInt(current_time - score_time) < 3000)){
        draw_text('1', canvas.width/2-10, canvas.height/2-50, 40)
    };
    if(parseInt(current_time - score_time) < 3000) {
        ball_vel = [0, 0];
    } else {
        score_time = 0
        let velocities = [-5, 5]
        let random_vel_x = velocities[Math.floor(Math.random() * velocities.length)]
        let random_vel_y = velocities[Math.floor(Math.random() * velocities.length)]
        ball_vel = [random_vel_x, random_vel_y]
    };
};

function ball_collisions() {
    // border
    if(ball_pos[0]+ball_size >= canvas.width) {
        HEEHEEHEEHAW.play();
        p1_score += 1
        score_time = parseInt(current_time)
        
        
    };
    if(ball_pos[0] <= 0) {
        HEEHEEHEEHAW.play();
        p2_score += 1
        score_time = parseInt(current_time)
    };
    if(ball_pos[1]+ball_size >= canvas.height) {
        random_sound = [Math.floor(Math.random() * 2)]
        if(random_sound == 1){
            ping.play();
        } else{
            pong.play()
        };
        ball_vel[1] *= -1;
    };
    if(ball_pos[1] <= 0) {
        random_sound = [Math.floor(Math.random() * 2)]
        if(random_sound == 1){
            ping.play();
        } else{
            pong.play()
        };
        ball_vel[1] *= -1;
    };

    // player 1

    if(ball_pos[0] < (paddle1_pos[0] + paddle1_size[0])) {
        if((ball_pos[1] + ball_size) > paddle1_pos[1]) {
            if(ball_pos[1] < (paddle1_pos[1] + paddle1_size[1])) {
                if(ball_vel[0] < 0) {
                    if(Math.abs(ball_pos[0] - (paddle1_pos[0] + paddle1_size[0])) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[0] *= -1;
                        if((ball_vel[0] < 10) && (ball_vel[0] > -10)){
                            if((ball_vel[1] < 10) && (ball_vel[1] > -10))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                    if(Math.abs((ball_pos[1] + ball_size) - paddle1_pos[1]) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[1] *= -1;
                        if((ball_vel[0] < 10) && (ball_vel[0] > -10)){
                            if((ball_vel[1] < 10) && (ball_vel[1] > -10))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                    if(Math.abs(ball_pos[1] - (paddle1_pos[1] + paddle1_size[1])) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[1] *= -1;
                        if((ball_vel[0] < 10) && (ball_vel[0] > -10)){
                            if((ball_vel[1] < 10) && (ball_vel[1] > -10))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                };
            };
        };
    };

    // player 2

    if((ball_pos[0] + ball_size) > paddle2_pos[0]) {
        if((ball_pos[1] + ball_size) > paddle2_pos[1]) {
            if(ball_pos[1] < (paddle2_pos[1] + paddle2_size[1])) {
                if(ball_vel[0] > 0) {
                    if(Math.abs((ball_pos[0] + ball_size) - paddle2_pos[0]) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[0] *= -1
                        if((ball_vel[0] < 10) && (ball_vel[0] > -10)){
                            if((ball_vel[1] < 10) && (ball_vel[1] > -10))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                    if(Math.abs((ball_pos[1] + ball_size) - paddle2_pos[1]) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[1] *= -1
                        if((ball_vel[0] < 10) && (ball_vel[0] > -10)){
                            if((ball_vel[1] < 10) && (ball_vel[1] > -10))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                    if(Math.abs(ball_pos[1] - (paddle2_pos[1] + paddle2_size[1])) < 10) {
                        random_sound = [Math.floor(Math.random() * 2)]
                        if(random_sound == 1){
                            ping.play();
                        } else{
                            pong.play()
                        };
                        ball_vel[1] *= -1
                        if((ball_vel[0] < 8) && (ball_vel[0] > -8)){
                            if((ball_vel[1] < 8) && (ball_vel[1] > -8))
                                if(ball_vel[0] > 0) {    
                                    ball_vel[0] += 1;
                                };
                                if(ball_vel[0] < 0) {    
                                    ball_vel[0] -= 1;
                                };
                                if(ball_vel[1] > 0) {    
                                    ball_vel[1] += 1;
                                };
                                if(ball_vel[1] < 0) {    
                                    ball_vel[1] -= 1;
                                };
                        };
                    };
                };
            };
        };
    };

};



function update() {
    current_time += 1/0.06

    if(game_active == true){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        draw_rect(paddle1_pos[0], paddle1_pos[1], paddle1_size[0], paddle1_size[1], 'rgb(255,255,255)');
        draw_rect(paddle2_pos[0], paddle2_pos[1], paddle2_size[0], paddle2_size[1], 'rgb(255,255,255)');
        draw_rect(ball_pos[0], ball_pos[1], ball_size, ball_size, 'rgb(255,255,255)');
        draw_text(p1_score, 100, 50, 40);
        draw_text(p2_score, canvas.width-100-40, 50, 40);

        // ball movement
        ball_pos[0] += ball_vel[0];
        ball_pos[1] += ball_vel[1];

        // paddle movement
        paddle1_pos[1] += paddle1_vel;
        paddle2_pos[1] += paddle2_vel;

        if(p1_score >= 5){
            game_active = false
            score_time = 0
            winner = 'player 1'
        };
        if(p2_score >= 5){
            game_active = false
            score_time = 0
            winner = 'player 2'
        };

        // paddle borders
        if(paddle1_pos[1] < 0) {
            paddle1_pos[1] = 0;
            paddle1_vel = 0;
        };
        if(paddle1_pos[1] + paddle1_size[1] > canvas.height) {
            paddle1_pos[1] = canvas.height - paddle1_size[1];
            paddle1_vel = 0;
        };
        if(paddle2_pos[1] < 0) {
            paddle2_pos[1] = 0;
            paddle2_vel = 0;
        };
        if(paddle2_pos[1] + paddle2_size[1] > canvas.height) {
            paddle2_pos[1] = canvas.height - paddle2_size[1];
            paddle2_vel = 0;
        };

        if(score_time != 0){
            ball_restart()
        };

        ball_collisions();
    } else{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        draw_text('PONG', canvas.width/2-175, canvas.height/2-50, 125)
        draw_text('press space to start', canvas.width/2-200, canvas.height/2+100, 50)
        if(winner != 0){
            draw_text(winner + ' has won', canvas.width/2-175, canvas.height/2+200, 50)
        };
    }
};
setInterval(update, 1000/60)
