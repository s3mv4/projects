const txt = document.getElementById("txt")
let randomNum = Math.floor(Math.random() * 2)
let randomNumArr = []
for (let i = 0; i < 4592; i++) {
    txt.textContent += `${randomNum} `
    randomNumArr.push(randomNum)
    randomNum = Math.floor(Math.random() * 2)
}
for (let i = 0; i < txt.textContent.length/2; i++) {
    if (txt.textContent[i] != ' ')
        console.log(`${i}: ${txt.textContent[i]}`)
}1