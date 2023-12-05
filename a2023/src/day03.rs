use regex::{Regex};
use std::collections::HashMap;
use std::fs;

fn part_01(contents: String, example: bool) {
    let mut grid: HashMap<(i32, i32), char> = HashMap::new();
    let mut i: i32 = 0;
    for line in contents.lines() {
        for (j, c) in line.chars().enumerate() {
            grid.insert((i, j as i32), c);
        }
        i += 1;
    }

    let number_regex = Regex::new(r"\d+").unwrap();
    let mut sum = 0;

    for (i, line) in contents.lines().enumerate() {
        for mat in number_regex.find_iter(line) {
            let number_str = mat.as_str();
            let number: i32 = number_str.parse().unwrap();
            let start_col = mat.start() as i32;
            let end_col = mat.end() as i32 - 1;

            let mut adjacent = false;
            for j in start_col..=end_col {
                if is_adjacent_to_symbol(&grid, (i as i32, j)) {
                    adjacent = true;
                    break;
                }
            }

            if adjacent {
                sum += number;
            }
        }
    }

    let identifier = if example { "example" } else { "" };
    println!("Answer day 3 {}: part 1: {}", identifier, sum);
}

fn is_adjacent_to_symbol(grid: &HashMap<(i32, i32), char>, coord: (i32, i32)) -> bool {
    let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1),
    ];

    directions.iter().any(|&(dx, dy)| {
        let nx = coord.0 + dx;
        let ny = coord.1 + dy;

        if let Some(&nc) = grid.get(&(nx, ny)) {
            nc != '.' && !nc.is_digit(10)
        } else {
            false
        }
    })
}

pub fn solve() {
    let sample_1 = fs::read_to_string("./inputs/03_example.txt")
        .expect("Should have been able to read the file");
    let input_1 =
        fs::read_to_string("./inputs/03.txt").expect("Should have been able to read the file");
    part_01(sample_1.clone(), true);
    part_01(input_1.clone(), false);
}
