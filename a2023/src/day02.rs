use regex::Regex;
use std::collections::HashMap;
use std::fs;

fn part_01(contents: String, example: bool) {
    let limits = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let game_regex = Regex::new(r"Game (\d+): ((?:\d+ (?:red|blue|green)[,;]?\s?)+)").unwrap();
    let color_regex = Regex::new(r"(\d+) (red|blue|green)").unwrap();
    let mut games: HashMap<String, HashMap<String, i32>> = HashMap::new();
    for game_caps in game_regex.captures_iter(contents.as_str()) {
        let game_number = game_caps.get(1).unwrap().as_str().to_string();
        let color_text = game_caps.get(2).unwrap().as_str();

        let mut color_counts: HashMap<String, i32> = HashMap::new();

        for color_caps in color_regex.captures_iter(color_text) {
            let count: i32 = color_caps.get(1).unwrap().as_str().parse().unwrap();
            let color = color_caps.get(2).unwrap().as_str().to_string();
            let curr_cnt = color_counts.entry(color.clone()).or_insert(0);
            if *curr_cnt < count {
                *curr_cnt = count;
            }
        }
        games.insert(game_number, color_counts);
    }
    let sum: i32 = games
        .iter()
        .filter_map(|(game, colors)| {
            if colors.iter().all(|(color, &count)| {
                limits
                    .get(color.as_str())
                    .map_or(false, |&limit| count <= limit)
            }) {
                game.parse::<i32>().ok()
            } else {
                None
            }
        })
        .sum();
    let identifier = if example == true { "example" } else { "" };
    println!("Answer day 2 {}: part 1: {}", identifier, sum);
}

pub fn solve() {
    let contents = fs::read_to_string("./inputs/02_example.txt")
        .expect("Should have been able to read the file");
    part_01(contents, true);
    let contents =
        fs::read_to_string("./inputs/02.txt").expect("Should have been able to read the file");
    part_01(contents, false);
}
