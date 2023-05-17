use rand::Rng;
use std::io;

fn main() {
    println!("Rock, paper and scissors!");

    let rps: [&str; 3] = ["rock", "paper", "scissors"];

    loop {
        println!("Please input your choice.");

        let mut choice = String::new();

        io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line");

        if !rps.contains(&choice.as_str().trim()) {
            println!("Input error: choice can be 'rock', 'paper' or 'scissors'.");
            continue;
        }

        let computer_choice = rps[rand::thread_rng().gen_range(0..rps.len())];

        println!("Comuters choice: {computer_choice}");

        if computer_choice == choice.as_str().trim() {
            println!("Tie! Try again!");
            continue;
        } else if (computer_choice == "rock" && choice.as_str().trim() == "paper")
            || (computer_choice == "paper" && choice.as_str().trim() == "scissors")
            || (computer_choice == "scissors" && choice.as_str().trim() == "rock")
        {
            println!("You win!");
        } else if (computer_choice == "rock" && choice.as_str().trim() == "scissors")
            || (computer_choice == "paper" && choice.as_str().trim() == "rock")
            || (computer_choice == "scissors" && choice.as_str().trim() == "paper")
        {
            println!("You lose!");
        }

        break;
    }
}
