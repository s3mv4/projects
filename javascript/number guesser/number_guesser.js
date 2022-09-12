var number = Math.floor(Math.random() * 100);

var guessed = false;

console.log(number);

var guess = window.prompt('Guess the random number between 0 and 99: ');

while(guessed === false) {
  if (guess < number) {
    guess = window.prompt('Too low, try again: ');
    continue;
  } 
  if (guess > number) {
    guess = window.prompt('Too high, try again: ');
    continue;
  }
  if (guess == number) {
    alert('You guessed the number');
    guessed = true;
    break;
  }
  if (guess == 'quit') {
    break;
  } 
}