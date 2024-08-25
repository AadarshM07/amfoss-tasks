use std::io;

fn main() {
    println!("Enter n value: ");
    
    // Read user input
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    
    // input as an integer
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    // Generate the upper part o
    for i in 1..=n {
        if i % 2 == 1 { // Only for odd numbers
            let spaces = (n - i) / 2;
            let stars = i;
            println!("{}{}", " ".repeat(spaces), "*".repeat(stars));
        }
    }

    // Generate the lower part 
    for i in (1..n).rev() {
        if i % 2 == 1 { // Only for odd numbers
            let spaces = (n - i) / 2;
            let stars = i;
            println!("{}{}", " ".repeat(spaces), "*".repeat(stars));
        }
    }
}
