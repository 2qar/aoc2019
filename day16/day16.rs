use std::char::from_digit;

const INPUT: &str = "59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608";

fn main() -> () {
    let input: Vec<u8> = INPUT.chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();

    let output = fft(input, 100);
    let mut out_string = String::with_capacity(output.len());
    for d in output {
        out_string.push(from_digit(d as u32, 10).unwrap());
    }
    println!("1: {}", &out_string[..8]);
}

// Generates the repeating [0, 1, 0, -1] pattern
fn pattern(digits: usize, repeat: usize) -> Vec<i8> {
    let mut pattern: Vec<i8> = vec![0, 1, 0, -1];

    pattern = pattern.into_iter()
        .map(|n| vec![n; repeat])
        .flatten()
        .collect();

    let mut i = 0;
    while pattern.len() < digits + 1 {
        pattern.push(pattern[i]);
        i += 1;
    }

    pattern.remove(0);
    while pattern.len() > digits {
        pattern.pop();
    }

    pattern
}

// Calculates the new digit for digit n.
fn phase_iter(num: &Vec<u8>, pos: usize) -> u8 {
    let pattern = pattern(num.capacity(), pos);

    //println!("nums: {:?}", num);
    //println!("pattern: {:?}", pattern);

    let x = num.iter().zip(pattern.iter())
        .map(|(n, p)| *n as i64 * *p as i64)
        .fold(0, |acc, x| acc + x)
        .abs() % 10;
    x as u8
}

fn phase(n: Vec<u8>) -> Vec<u8> {
    let mut new_n: Vec<u8> = Vec::with_capacity(n.capacity());
    for i in 0..n.capacity() {
        new_n.push(phase_iter(&n, i + 1));
    }

    new_n
}

fn fft(mut n: Vec<u8>, phases: usize) -> Vec<u8> {
    for _ in 0..phases {
        n = phase(n);
    }
    n
}
