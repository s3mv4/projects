const numbersEl = document.getElementById("numbers-el")
const outcomeEl = document.getElementById("outcome-el")
const inputEl = document.getElementById("input-el")
const calculateBtn = document.getElementById("calculate-btn")
let squareNumbers = []
let outcomeSquareNumbers = []
let outcome = null

const squareNumbersFromLocalStorage = JSON.parse(localStorage.getItem("squareNumbers"))

if(squareNumbersFromLocalStorage) {
    squareNumbers = squareNumbersFromLocalStorage
    render()
}

function generateSquareNumbers(limit) {
    squareNumbers = []
    let number = 1
    for (let i = 0; i < limit; i = squareNumbers[squareNumbers.length - 1]) {
        squareNumbers.push(number * number)
        number += 1     
    }
    squareNumbers.pop()
    localStorage.setItem("squareNumbers", JSON.stringify(squareNumbers))
    render()
}

function render() {
    numbersEl.textContent = ""
    for (let i = 0; i < squareNumbers.length; i++) {
        if (i != squareNumbers.length - 1) {
            numbersEl.textContent += `${squareNumbers[i]}, `
        } else {
            numbersEl.textContent += squareNumbers[i]
        }
    }
}

calculateBtn.addEventListener("click", function() {
    generateSquareNumbers(inputEl.value)
    for (let i = 1; i < squareNumbers.length + 2; i++) {
        if (i * i == inputEl.value) {
            outcome = i
        }
    }
    if (outcome) {
        outcomeEl.textContent = ""
        outcomeEl.textContent = `The square root of ${inputEl.value} is: `
        outcomeEl.textContent += outcome
        outcome = null
    } else {
        outcomeSquareNumbers = []
        for (i = squareNumbers.length; i > 0; i--) {
            if (inputEl.value / squareNumbers[i] % 1 == 0) {
                outcomeSquareNumbers.push(inputEl.value / squareNumbers[i])
            }
        }
        console.log(outcomeSquareNumbers)
        let num1 = 0
        if (Math.sqrt(inputEl.value / outcomeSquareNumbers[0]) % 1 == 0) {
            num1 = Math.sqrt(inputEl.value / outcomeSquareNumbers[0])
        } else {
            num1 = inputEl.value / outcomeSquareNumbers[0]
        }
        let num2 = 0
        if (Math.sqrt(outcomeSquareNumbers[0]) % 1 == 0) {
            num2 = Math.sqrt(outcomeSquareNumbers[0])
        } else {
            num2 = outcomeSquareNumbers[0]
        }
        outcomeEl.textContent = ""
        if (num1 != NaN && num2 != undefined) {
            outcomeEl.textContent = `The square root of ${inputEl.value} is: `
            outcomeEl.textContent += `${num1}√${num2}`
        } else {
            outcomeEl.textContent = `The square root of ${inputEl.value} does not exist`
        }
    }
    inputEl.value = ""
})
