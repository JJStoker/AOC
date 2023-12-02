use std::fs;

fn part_01(contents: String) {
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
                .unwrap()
        })
        .sum::<i32>();
    println!("Answer day 1: part 1: {}", answer);
}

pub fn solve(file_path: &String) {
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    part_01(contents);
}
