use std::fs::File;
use std::io::{self, Read, Write};

fn main() -> io::Result<()> {
    // Step : Read the value of n from input.txt
    let mut input_file = File::open("input.txt")?;
    let mut input = String::new();
    input_file.read_to_string(&mut input)?;

    let n: usize = input.trim().parse().expect("Please enter a valid number");

    let mut output = String::new();

    // Generate the upper part of the diamond
    for i in 1..=n {
        if i % 2 == 1 { // Only for odd numbers
            let spaces = (n - i) / 2;
            let stars = i;
            output.push_str(&format!("{}{}\n", " ".repeat(spaces), "*".repeat(stars)));
        }
    }

    // Generate the lower part of the diamond
    for i in (1..n).rev() {
        if i % 2 == 1 { // Only for odd numbers
            let spaces = (n - i) / 2;
            let stars = i;
            output.push_str(&format!("{}{}\n", " ".repeat(spaces), "*".repeat(stars)));
        }
    }

    let mut output_file = File::create("output.txt")?;
    output_file.write_all(output.as_bytes())?;

    // Return Ok if everything is successful
    Ok(())
}
