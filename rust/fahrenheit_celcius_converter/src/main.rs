fn main() {
    let fahrenheit = 32.0;
    let celsius = 0.0;

    let fahrenheit_to_celsius = (fahrenheit - 32.0) / 1.8;
    let celsius_to_fahrenheit = (celsius * 1.8) + 32.0;

    println!("{fahrenheit} Fahrenheit is {fahrenheit_to_celsius} Celsius");
    println!("{celsius} Celsius is {celsius_to_fahrenheit} Fahrenheit");
}
