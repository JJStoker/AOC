use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn part_01(contents: String, example: bool) {
    let mut sum = 0;
    let identifier = if example { "example" } else { "" };
    println!("Answer day 4 {}: part 1: {}", identifier, sum);
}

pub fn solve() {
    let sample_1 = fs::read_to_string("./inputs/04_example.txt")
        .expect("Should have been able to read the file");
    let input_1 =
        fs::read_to_string("./inputs/04.txt").expect("Should have been able to read the file");
        part_01(sample_1.clone(), true);
        part_01(input_1.clone(), false);
}
