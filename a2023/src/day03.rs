use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn part_01(contents: String, example: bool) {
    let grid = parse_grid(&contents);
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

fn part_02(contents: String, example: bool) {
    let grid = parse_grid(&contents);
    let filtered_grid = grid.iter().filter(|(_, &c)| c == '*').map(|(coord, _)| coord);
    let number_regex = Regex::new(r"\d+").unwrap();
    let mut sum = 0;
    for coord in filtered_grid {
        let mut adjacent_numbers = Vec::new();
        for (i, line) in contents.lines().enumerate() {
            for mat in number_regex.find_iter(line) {
                let number_str = mat.as_str();
                let start_col = mat.start() as i32;
                let end_col = mat.end() as i32 - 1;
                for j in start_col..=end_col {
                    if is_adjacent(coord, &(i as i32, j)) {
                        adjacent_numbers.push(number_str.parse::<i32>().unwrap());
                        break;
                    }
                }
            }
        }
        if adjacent_numbers.len() == 2 {
            sum += adjacent_numbers[0] * adjacent_numbers[1];
        }
    }

    let identifier = if example { "example" } else { "" };
    println!("Answer day 3 {}: part 2: {}", identifier, sum);
}

fn parse_grid(contents: &String) -> HashMap<(i32, i32), char> {
    let mut grid = HashMap::new();
    let mut i: i32 = 0;
    for line in contents.lines() {
        for (j, c) in line.chars().enumerate() {
            grid.insert((i, j as i32), c);
        }
        i += 1;
    }
    grid
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

fn is_adjacent(coord1: &(i32, i32), coord2: &(i32, i32)) -> bool {
    let dx = (coord1.0 - coord2.0).abs();
    let dy = (coord1.1 - coord2.1).abs();
    dx <= 1 && dy <= 1
}

pub fn solve() {
    let sample_1 = fs::read_to_string("./inputs/03_example.txt")
        .expect("Should have been able to read the file");
    let input_1 =
        fs::read_to_string("./inputs/03.txt").expect("Should have been able to read the file");
        part_01(sample_1.clone(), true);
        part_01(input_1.clone(), false);
        part_02(sample_1.clone(), true);
        part_02(input_1.clone(), false);
}
