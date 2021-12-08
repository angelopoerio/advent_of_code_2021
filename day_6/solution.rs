use std::fs;

fn solve(mut timers: Vec<i32>, days: &usize) -> usize {
    let mut lanternfish_to_add = 0;

    if *days == 0 {
        return timers.len();
    }

    for timer in &mut timers {
        if *timer == 0 {
            *timer = 6;
            lanternfish_to_add += 1;
        } else {
            *timer -= 1;
        }
    }

    for _ in 0..lanternfish_to_add {
        timers.push(8);
    }

    solve(timers, &(days - 1))
}

fn main() {
    let content = fs::read_to_string("input.txt").unwrap();
    let timers: Vec<i32> = content
        .split(",")
        .filter(|s| !s.to_string().starts_with("\n"))
        .map(|s| s.to_string().trim().parse::<i32>().unwrap())
        .collect();
    println!("Solution is {}", solve(timers, &80));
}
