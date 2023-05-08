fn main() {
    let fib_index = 30;
    println!("The Fibonacci number at index {fib_index} is: {}", fib(fib_index));
}

fn fib(x: i32) -> i32 {
    if x == 0 || x == 1 {
        return x;
    } else {
        return fib(x - 1) + fib(x - 2);
    }
}
