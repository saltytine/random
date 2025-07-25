// Riddle:
// I’m strict but fair, no bugs inside,
// Ownership rules you can’t override.
// Borrow me once, then borrow twice,
// But break my rules and pay the price.
// To solve this riddle, here’s your task:
//
// Write a Rust program that reads a string from the user,
// reverses it safely without cloning the entire string,
// and prints the reversed result only if the string length is even.
//
// What am I?

use std::io::{self, Write};

fn main() {
    print!("Enter a string: ");
    io::stdout().flush().unwrap();

    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    if input.ends_with('\n') {
        input.pop();
        if input.ends_with('\r') {
            input.pop();
        }
    }

    let trimmed = input.trim();

    if trimmed.len() % 2 == 0 {
        let reversed: String = trimmed.chars().rev().collect();
        println!("Reversed (even length): {}", reversed);
    } else {
        println!("The string length is odd. Nothing printed.");
    }
}
