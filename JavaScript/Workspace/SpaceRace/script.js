const canvas = document.getElementById('space_race')
const ctx = canvas.getContext('2d')

const player1_size = [25, 25]
let player1_pos = [canvas.width/4-player1_size[0], canvas.height-player1_size[1]]
let player1_vel = 0
let p1_score = 0

const player2_size = [25, 25]
let player2_pos = [(canvas.width/4)*3-player2_size[0], canvas.height-player2_size[1]]
let player2_vel = 0
let p2_score = 0

const timer_size = [5, 200]
let timer_pos = [canvas.width/2-timer_size[0], canvas.height-timer_size[1]]
let timer_vel = 0.05

let winner = 0

let asteroids = []

let asteroids_called = 0

let asteroid_delay = 10

let current_time = 0

let current_time_pause = 0

let game_active = false

let ga_zo_door = new Audio('ga_zo_door.mp3')
let goed_zeg = new Audio('goed_zeg.mp3')
let klik_start = new Audio('klik_start.mp3')
let nog_spelen = new Audio('nog_spelen.mp3')
let oeps = new Audio('oeps.mp3')
let superr = new Audio('superr.mp3')

let sounds_played = 0

class Asteroid {
    constructor(index){
        this.size = [5, 5]
        this.del_delay = 5
        this.index = index
        if (asteroids_called % 2 == 0){
            this.pos = [0-this.size[0], Math.floor(Math.random() * canvas.height-canvas.height/8)]
            this.vel = 1
        } else {
            this.pos = [canvas.width, Math.floor(Math.random() * canvas.height-canvas.height/8)]
            this.vel = -1
        }
    }
    update(ctx){
        if(game_active == true){
            ctx.beginPath()
            ctx.rect(this.pos[0], this.pos[1], this.size[0], this.size[1])
            ctx.fillStyle = 'rgb(255,255,255)'
            ctx.fill()
            ctx.closePath()
            this.pos[0] += this.vel
            if(this.pos[0] < player1_pos[0] + player1_size[0]){
                if(this.pos[0] + this.size[0] > player1_pos[0]){
                    if(this.pos[1] < player1_pos[1] + player1_size[1]){
                        if(this.pos[1] + this.size[1] > player1_pos[1]){
                            oeps.play()
                            player1_pos = [canvas.width/4-player1_size[0], canvas.height-player1_size[1]]
                        }
                    }
                
                } 
            }
            if(this.pos[0] < player2_pos[0] + player2_size[0]){
                if(this.pos[0] + this.size[0] > player2_pos[0]){
                    if(this.pos[1] < player2_pos[1] + player2_size[1]){
                        if(this.pos[1] + this.size[1] > player2_pos[1]){
                            oeps.play()
                            player2_pos = [(canvas.width/4)*3-player2_size[0], canvas.height-player2_size[1]]
                        }
                    }
                
                } 
            }
        }
    }
}



document.addEventListener('keydown', function(event) {
    if(event.keyCode == 38 && game_active == true) { // up arrow
        player2_vel = -2
    }
    if(event.keyCode == 87 && game_active == true) { // w
        player1_vel = -2
    }
    if(event.keyCode == 32 && game_active == false) { // space
        player1_pos = [canvas.width/4-player1_size[0], canvas.height-player1_size[1]]
        player1_vel = 0
        p1_score = 0    
        player2_pos = [(canvas.width/4)*3-player2_size[0], canvas.height-player2_size[1]]
        player2_vel = 0
        p2_score = 0
        timer_pos = [canvas.width/2-timer_size[0], canvas.height-timer_size[1]]
        timer_vel = 0.05
        asteroids = []
        asteroid_delay = 10
        asteroids_called = 0
        winner = 0
        game_active = true
    }
    if(event.keyCode == 27 && game_active == true) { // esc
        game_active = false
    }
})

document.addEventListener('keyup', function(event) {
    if(event.keyCode == 38 && game_active == true) { // up arrow
        player2_vel = 0;
    }
    if(event.keyCode == 87 && game_active == true) { // w
        player1_vel = 0;
    }
})

function draw_rect(x, y, w, h) {
    ctx.beginPath()
    ctx.rect(x, y, w, h)
    ctx.fillStyle = 'rgb(255,255,255)'
    ctx.fill()
    ctx.closePath()

}

function draw_text(text, x, y, size) {
    ctx.font = `${size}px Arial`
    ctx.fillStyle = 'rgb(255,255,255)'
    ctx.fillText(text, x, y)
}

function update() {
    current_time += 1/0.06
    if(game_active == true){
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        draw_rect(player1_pos[0], player1_pos[1], player1_size[0], player1_size[1])
        draw_rect(player2_pos[0], player2_pos[1], player2_size[0], player2_size[1])
        draw_rect(timer_pos[0], timer_pos[1], timer_size[0], timer_size[1])
        draw_text(p1_score, canvas.width/2-60, canvas.height, 50)
        draw_text(p2_score, canvas.width/2+27.5, canvas.height, 50)
    
        if(asteroid_delay <= 0){
            asteroids_called += 1
            asteroids.push(new Asteroid(asteroids.length))
            asteroid_delay = 10
        }
        asteroid_delay -= 1
        asteroids.forEach((asteroid) => asteroid.update(ctx))

        if(timer_pos[1] >= canvas.height){
            nog_spelen.play()
            current_time_pause = current_time
            if(p1_score - p2_score > 0){
                winner = 'player 1'
            } else if(p1_score - p2_score < 0){
                winner = 'player 2'
            } else {
                winner = 'tie'
            }
            game_active = false
        } 

        if(player1_pos[1] <= 0){
            if(sounds_played % 3 == 1){
                superr.play()
                sounds_played += 1
            } else if(sounds_played % 3 == 2){
                ga_zo_door.play()
                sounds_played += 1
            } else if(sounds_played % 3 == 0){
                goed_zeg.play()
                sounds_played += 1
            }
            player1_pos = [canvas.width/4-player1_size[0], canvas.height-player1_size[1]]
            p1_score += 1
        }
        if(player2_pos[1] <= 0){
            if(sounds_played % 3 == 1){
                superr.play()
                sounds_played += 1
            } else if(sounds_played % 3 == 2){
                ga_zo_door.play()
                sounds_played += 1
            } else if(sounds_played % 3 == 0){
                goed_zeg.play()
                sounds_played += 1
            }
            player2_pos = [(canvas.width/4)*3-player2_size[0], canvas.height-player2_size[1]]
            p2_score += 1
        }

        timer_pos[1] += timer_vel
        player1_pos[1] += player1_vel
        player2_pos[1] += player2_vel
    } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        draw_text('SPACE RACE', canvas.width/2-250, 250, 75)
        draw_text('press space to start', canvas.width/2-175, 400, 40)
        if(winner != 0){
            draw_text(`winner = ${winner}`, canvas.width/2-160, 500, 40)
        }
        if(current_time - current_time_pause > 1000){    
        klik_start.play()
        }
    }
}

setInterval(update, 1000/60)