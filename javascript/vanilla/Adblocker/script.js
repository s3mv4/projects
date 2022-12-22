const html = document.querySelector("html")
html.innerHTML = ""
let i = 0

function update() {
    if (i % 2 === 0) {
        html.innerHTML = "<body style='background-color:white;'></body>"
    } else {
        html.innerHTML = "<body style='background-color:black;'></body>"
    }
    i += 1
}

setInterval(update, 100)