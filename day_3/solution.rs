use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec::Vec;

fn main() {
    let mut bits = HashMap::new();

    for i in 0..12 {
        bits.insert(i, vec![0, 0]);
    }

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(binary) = line {
                for (i, b) in binary.chars().enumerate() {
                    match bits.get(&i) {
                        Some(_) => match b {
                            '0' => (*bits.get_mut(&i).unwrap())[0] += 1,
                            '1' => (*bits.get_mut(&i).unwrap())[1] += 1,
                            _ => panic!("invalid symbol"),
                        },
                        _ => panic!("we should never get here"),
                    }
                }
            }
        }
    }

    solve(&bits);
}

fn binary_to_decimal(binary_str: &str) -> usize {
    let base: usize = 2;
    let mut result = 0;
    for (i, bit) in binary_str.chars().rev().enumerate() {
        match bit {
            '1' => result += base.pow(i as u32),
            _ => (),
        }
    }
    return result;
}

fn solve(bits: &HashMap<usize, Vec<usize>>) {
    let mut gamma = String::from("");
    let mut epsilon = String::from("");
    for i in 0..12 {
        let bits_count = bits.get(&i).unwrap();
        let zero_count = bits_count[0];
        let one_count = bits_count[1];

        if one_count > zero_count {
            gamma.push('1');
            epsilon.push('0');
        } else {
            gamma.push('0');
            epsilon.push('1');
        }
    }

    let dec_gamma = binary_to_decimal(&gamma);
    let dec_epsilon = binary_to_decimal(&epsilon);
    println!("gamma: {} | {}", gamma, dec_gamma);
    println!("epsilon: {} | {}", epsilon, dec_epsilon);
    println!("Solution is: {}", dec_gamma * dec_epsilon);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).unwrap();
    Ok(io::BufReader::new(file).lines())
}
