const canvas = document.getElementById("crusherer")
const ctx = canvas.getContext("2d")

const crusherSize = [100, 250]
const crusherPos = [canvas.width/4*3-crusherSize[0]/2, 0]

let bullets = []
let canShoot = true

let items = []
let itemsDelay = 50
let itemDelay = 200
let itemDelayMin = 150
let itemDelayMax = 450
let itemRgb = "rgb(255, 0, 0)"
let itemVel = 3

let score = 0

let timer = {
    minutes: 1,
    seconds: 0
}

let gameActive = false

const voom = new Audio("voom.mp3")
const pwchr = new Audio("pwchr.mp3")
const rood = new Audio("rood.mp3")
const blauw = new Audio("blauw.mp3")
const oranje = new Audio("oranje.mp3")
const groen = new Audio("groen.mp3")
const HEEHEEHEEHAW = new Audio("HEEHEEHEEHAW.mp3")

class Bullet {
    constructor(items, rgb) {
        this.size = [10, 10]
        this.pos = [canvas.width/4*3-this.size[0]/2, 250]
        this.vel = 7
        this.rgb = rgb
        this.items = items
    }
    update(ctx) {
        ctx.beginPath()
        ctx.rect(this.pos[0], this.pos[1], this.size[0], this.size[1])
        ctx.fillStyle = this.rgb
        ctx.fill()
        ctx.closePath()
        this.pos[1] += this.vel
        if (this.pos[1] >= canvas.height) {
            // HEEHEEHEEHAW.play()
            bullets.shift()
            score -= 1
            if (itemVel > 3) {
                itemVel -= itemVel / 17
                if (itemVel < 3) {
                    itemVel = 3
                }
            } else {
                itemVel = 3
            }
            if (itemDelayMin < 150) {
                itemDelayMin += itemDelayMin / 15
                if (itemDelayMin > 150) {
                    itemDelayMin = 150
                } 
                itemDelayMax = itemDelayMin * 3 
            } else {
                itemDelayMin = 150
                itemDelayMax = itemDelayMin * 3
            }
            if (itemDelay < 200) {
                itemDelay += itemDelay / 15
                if (itemDelay > 200) {
                    itemDelay = 200
                } 
            } else {
                itemDelay = 200
            }
        }
        this.items.forEach((item, index) => {
            if(this.pos[0] < item.pos[0] + item.size[0]){
                if(this.pos[0] + this.size[0] > item.pos[0]){
                    if(this.pos[1] < item.pos[1] + item.size[1]){
                        if(this.pos[1] + this.size[1] > item.pos[1]){
                            if(this.rgb === item.rgb) {
                                pwchr.play()
                                items.splice(index, 1)
                                bullets.shift()
                                score += 1
                                if (itemVel < 8.9) {
                                    itemVel += itemVel / 16
                                    if (itemVel > 8.9) {
                                        itemVel = 8.9
                                    }
                                } else {
                                    itemVel = 8.9
                                }
                                if (itemDelayMin > 47) {
                                    itemDelayMin -= itemDelayMin / 16
                                    if (itemDelayMin < 47) {
                                        itemDelayMin = 47
                                    } 
                                    itemDelayMax = itemDelayMin * 3
                                } else {
                                    itemDelayMin = 47
                                    itemDelayMax = itemDelayMin * 3
                                }
                                if (itemDelay > 63) {
                                    itemDelay -= itemDelay / 16
                                    if (itemDelay < 63) {
                                        itemDelay = 63
                                    } 
                                } else {
                                    itemDelay = 63
                                }
                                
                            } else {
                                // HEEHEEHEEHAW.play()
                                bullets.shift()
                                score -= 1
                                if (itemVel > 3) {
                                    itemVel -= itemVel / 17
                                    if (itemVel < 3) {
                                        itemVel = 3
                                    }
                                } else {
                                    itemVel = 3
                                }
                                if (itemDelayMin < 150) {
                                    itemDelayMin += itemDelayMin / 15
                                    if (itemDelayMin > 150) {
                                        itemDelayMin = 150
                                    } 
                                    itemDelayMax = itemDelayMin * 3 
                                } else {
                                    itemDelayMin = 150
                                    itemDelayMax = itemDelayMin * 3
                                }
                                if (itemDelay < 200) {
                                    itemDelay += itemDelay / 15
                                    if (itemDelay > 200) {
                                        itemDelay = 200
                                    } 
                                } else {
                                    itemDelay = 200
                                }
                            }
                        }
                    }
                
                } 
            }
        })
    }
}

class Item {
    constructor(vel, rgb) {
        this.size = [100, 30]
        this.pos = [0-this.size[0], canvas.height-this.size[1]]
        this.vel = vel
        this.rgb = rgb
    }
    update(ctx) {
        ctx.beginPath()
        ctx.rect(this.pos[0], this.pos[1], this.size[0], this.size[1])
        ctx.fillStyle = this.rgb
        ctx.fill()
        ctx.closePath()
        this.pos[0] += this.vel
        if (this.pos[0] >= canvas.width) {
            // HEEHEEHEEHAW.play()
            items.shift()
            score -= 1
            if (itemVel > 3) {
                itemVel -= itemVel / 17
                if (itemVel < 3) {
                    itemVel = 3
                }
            } else {
                itemVel = 3
            }
            if (itemDelayMin < 150) {
                itemDelayMin += itemDelayMin / 15
                if (itemDelayMin > 150) {
                    itemDelayMin = 150
                } 
                itemDelayMax = itemDelayMin * 3 
            } else {
                itemDelayMin = 150
                itemDelayMax = itemDelayMin * 3
            }
            if (itemDelay < 200) {
                itemDelay += itemDelay / 15
                if (itemDelay > 200) {
                    itemDelay = 200
                } 
            } else {
                itemDelay = 200
            }
        }
    }
}

function drawRect(x, y, w, h, rgb) {
    ctx.beginPath()
    ctx.rect(x, y, w, h)
    ctx.fillStyle = rgb
    ctx.fill()
    ctx.closePath()

}

function drawText(text, x, y, size, rgb) {
    ctx.font = `${size}px Arial`
    ctx.fillStyle = rgb
    ctx.fillText(text, x, y)
}

function getRandomRgb() {
    let randomNumber = Math.floor(Math.random() * 4)
    if (randomNumber === 1) return "rgb(0, 255, 0)"
    if (randomNumber === 2) return "rgb(255, 165, 0)"
    if (randomNumber === 3) return "rgb(0, 0, 255)"
    return "rgb(255, 0, 0)"
}

document.addEventListener('keydown', function(event) {
    if (gameActive) {
        if(event.keyCode == 38 && canShoot === true) {
            groen.play()
            bullets.push(new Bullet(items, "rgb(0, 255, 0)"))
            
        }
        if(event.keyCode == 37 && canShoot === true) {
            oranje.play()
            bullets.push(new Bullet(items, "rgb(255, 165, 0)"))
            
        }
        if(event.keyCode == 40 && canShoot === true) {
            blauw.play()
            bullets.push(new Bullet(items, "rgb(0, 0, 255)"))
        }
        if(event.keyCode == 39 && canShoot === true) {
            rood.play()
            bullets.push(new Bullet(items, "rgb(255, 0, 0)"))
        }
        if(event.keyCode == 27) {
            gameActive = false
        }
    } else {
        if(event.keyCode == 32) {
            bullets = []
            items = []
            itemsDelay = 50
            itemDelay = 200
            itemDelayMin = 150
            itemDelayMax = 450
            itemVel = 3
            score = 0
            timer = {
                minutes: 1,
                seconds: 0
            }
            gameActive = true
        }
    }
})

document.addEventListener("keydown", function(event) {
    if (event.keyCode == 38 || event.keyCode == 37 || event.keyCode == 40 || event.keyCode == 39) { 
        canShoot = false
    }
})

document.addEventListener("keyup", function(event) {
    if (event.keyCode == 38 || event.keyCode == 37 || event.keyCode == 40 || event.keyCode == 39) { 
        canShoot = true
    }
})

function update() {
    if (gameActive) {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        drawRect(crusherPos[0], crusherPos[1], crusherSize[0], crusherSize[1], "rgb(255, 255, 255)")
        drawText(score, canvas.width/2, 50, 50, "rgb(255, 255, 255)")
        drawText("up", 80, 30, 30, "rgb(0, 255, 0)")
        drawText("left", 10, 80, 30, "rgb(255, 165, 0)")
        drawText("down", 60, 130, 30, "rgb(0, 0, 255)")
        drawText("right", 140, 80, 30, "rgb(255, 0, 0)")
        timerDis = ""
        if (Math.floor(timer.minutes) < 10)  { 
            timerDis += `0${Math.floor(timer.minutes)}:` 
            drawText()
        } else {
            timerDis += `${Math.floor(timer.minutes)}:`
        }
        if (Math.floor(timer.seconds) < 10)  { 
            timerDis += `0${Math.floor(timer.seconds)}` 
            drawText()
        } else {
            timerDis += `${Math.floor(timer.seconds)}`
        }
        drawText(timerDis, canvas.width/2-50, 150, 50, "rgb(255, 255, 255)")

        bullets.forEach((bullet) => bullet.update(ctx))

        if(itemsDelay <= 0){
            itemRgb = getRandomRgb()
            items.push(new Item(itemVel, itemRgb))
            itemsDelay = itemDelay
        }
        itemsDelay -= 1
        items.forEach((item) => item.update(ctx))

        timer.seconds -= 1/60
        if (Math.floor(timer.minutes) === 0 && Math.floor(timer.seconds) === -1) {
            gameActive = false
        }
        if (Math.floor(timer.seconds) === -1) {
            timer.minutes -= 1/60
            timer.seconds = 59
        }
        console.log(`itemVel:${itemVel} itemDelayMin:${itemDelayMin} itemDelay:${itemDelay}`)

    } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        drawText("CRUSHERER", canvas.width/2-330, 200, 100, "rgb(255, 255, 255)")
        drawText("press space to start", canvas.width/2-230, 350, 50, "rgb(255, 255, 255)")
        drawText(score, canvas.width/2, 450, 50, "rgb(255, 255, 255)")

    }
}

setInterval(update, 1000/60)