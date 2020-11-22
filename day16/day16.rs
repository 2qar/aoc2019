use std::char::from_digit;

const INPUT: &str = "59791871295565763701016897619826042828489762561088671462844257824181773959378451545496856546977738269316476252007337723213764111739273853838263490797537518598068506295920453784323102711076199873965167380615581655722603274071905196479183784242751952907811639233611953974790911995969892452680719302157414006993581489851373437232026983879051072177169134936382717591977532100847960279215345839529957631823999672462823375150436036034669895698554251454360619461187935247975515899240563842707592332912229870540467459067349550810656761293464130493621641378182308112022182608407992098591711589507803865093164025433086372658152474941776320203179747991102193608";
const PATTERN: [i8; 4] = [0, 1, 0, -1];

fn main() -> () {
    let input: Vec<u8> = INPUT.chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();

    let real_input: Vec<u8> = input.repeat(10_000);

    let mut pow = 7;
    let offset: usize = input[0..8].iter()
        .fold(0, |mut sum, d| {
            sum += *d as usize * 10_usize.pow(pow);
            if pow > 0 {
                pow -= 1;
            }
            sum
        });

    println!("1: {}", answer(input).get(0..8).unwrap());
    //println!("2: {}", answer(real_input).get(offset..(offset + 8)).unwrap());
}

fn phase_iter(n: &Vec<u8>, repeats: usize) -> u8 {
    let mut sum: i32 = 0;
    let mut r = repeats - 1;
    let mut i = 0;
    for digit in n {
        if r == 0 {
            r = repeats;
            i += 1;
        }
        if i == PATTERN.len() {
            i = 0;
        }

        match PATTERN[i] {
            1 => sum += *digit as i32,
            -1 => sum -= *digit as i32,
            _ => (),
        }

        r -= 1;
    }

    (sum.abs() % 10) as u8
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

fn answer(n: Vec<u8>) -> String {
    let output = fft(n, 100);
    let mut out_string = String::with_capacity(output.len());
    for d in output {
        out_string.push(from_digit(d as u32, 10).unwrap());
    }
    out_string
}
