const canvas = document.querySelector('canvas')
const ctx = canvas.getContext('2d')

const gravity = 0.5
let animationFrame = 1

canvas.width = innerWidth
canvas.height = innerHeight

console.log(location.port)

class Player {
    constructor() {
        this.position = {
            x: 0,
            y: 0
        }
        this.velocity = {
            x: 0,
            y: 0
        }
        this.width = 20
        this.height = 20
    }
    
    draw() {
        ctx.fillStyle = 'red'
        ctx.fillRect(this.position.x, this.position.y, this.width, this.height)
    }

    update() {
        this.draw()
        if (this.position.y + this.height + this.velocity.y < canvas.height) {
            this.position.y += this.velocity.y
        } else {
            this.position.y = canvas.height - this.height
            this.velocity.y = 1
        }
        if (this.position.y + this.velocity.y < 0) {
            this.position.y = 0
            this.velocity.y = 1
        }
        if (this.position.x + this.velocity.x < 0) {
            this.position.x = 0
            this.velocity.x = 0
        }
        if (this.position.x + this.width + this.velocity.x > canvas.width) {
            this.position.x = canvas.width - this.width
            this.velocity.x = 0
        }
        this.position.x += this.velocity.x
        this.velocity.y += gravity
    }
}

const player = new Player()
const keys = {
    left: false,
    up: false,
    right: false,
    bottom: false
}


function update() {
    requestAnimationFrame(update)
    canvas.width = innerWidth
    canvas.height = innerHeight
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    player.update()
    
    if (keys.right) {
        player.velocity.x = 5
    } else if (keys.left){
        player.velocity.x = -5
    } else {
        player.velocity.x = 0
    }

    if (keys.up) {
        player.velocity.y = -15
    }
}

update()

addEventListener('keydown', ({keyCode}) => {
    switch (keyCode) {
        case 65: // A
            keys.left = true
            break
        case 87: // W
            keys.up = true
            break
        case 68: // D
            keys.right = true 
            break
        case 83: // S
            keys.down = true
            break
    }
})

addEventListener('keyup', ({keyCode}) => {
    switch (keyCode) {
        case 65: // A
            keys.left = false
            break
        case 87: // W
            keys.up = false
            break
        case 68: // D
            keys.right = false
            break
        case 83: // S
            keys.down = false
            break
    }
})