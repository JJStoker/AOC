use std::env;

pub mod day01;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file_path = &args[1];
    day01::solve(file_path);
}
