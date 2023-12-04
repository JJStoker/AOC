use std::collections::HashMap;
use std::fs;

fn part_01(contents: String, example: bool) {
    let answer = contents
        .lines()
        .map(|line| {
            line.chars()
                .filter(|c| c.is_digit(10))
                .next()
                .into_iter()
                .chain(line.chars().filter(|c| c.is_digit(10)).last())
                .collect::<String>()
                .parse::<i32>()
                .unwrap_or(0)
        })
        .sum::<i32>();
    let identifier = if example == true { "example" } else { "" };
    println!("Answer day 1 {}: part 1: {}", identifier, answer);
}

fn part_02(contents: String, example: bool) {
    let digit_map = HashMap::from([
        ("zero", "0"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);

    let mut sum = 0;

    for line in contents.lines() {
        let mut number_str = String::new();
        let mut i = 0;

        while i < line.len() {
            if line.chars().nth(i).unwrap_or(' ').is_numeric() {
                number_str.push(line[i..].chars().next().unwrap())
            } else {
                for (word, number) in &digit_map {
                    if line[i..].starts_with(word) {
                        number_str.push_str(number);
                    }
                }
            }
            i += 1;
        }
        sum += number_str.chars()
            .next()
            .into_iter()
            .chain(number_str.chars().last())
            .collect::<String>()
            .parse::<i32>()
            .unwrap_or(0);
    }
    let identifier = if example == true { "example" } else { "" };
    println!("Answer day 1 {}: part 2: {}", identifier, sum);
}

pub fn solve() {
    let contents = fs::read_to_string("./inputs/01_example.txt")
        .expect("Should have been able to read the file");
    part_01(contents, true);
    let contents =
        fs::read_to_string("./inputs/01.txt").expect("Should have been able to read the file");
    part_01(contents, false);
    let contents = fs::read_to_string("./inputs/01_example_2.txt")
        .expect("Should have been able to read the file");
    part_02(contents, true);
    let contents =
        fs::read_to_string("./inputs/01.txt").expect("Should have been able to read the file");
    part_02(contents, false);
}
