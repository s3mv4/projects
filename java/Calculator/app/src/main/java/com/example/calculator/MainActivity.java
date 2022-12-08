package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import org.mariuszgromada.math.mxparser.*;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    private void updateDisplay(char c) {
        TextView display = findViewById(R.id.display);
        display.setText(String.format("%s%s", display.getText().toString(), c));
    }

    private void backspace() {
        TextView display = findViewById(R.id.display);
        if (!display.getText().toString().isEmpty()) {
            display.setText(String.format("%s", display.getText().toString().substring(0, display.getText().toString().length() - 1)));
        } else {
            display.setText(String.format("%s", display.getText().toString()));
        }
    }

    private void calculate() {
        TextView display = findViewById(R.id.display);
        String strtocalc = display.getText().toString();
        strtocalc = strtocalc.replaceAll("[^0123456789().+*/-]", "");
        Expression exp = new Expression(strtocalc);
        String result = String.valueOf(exp.calculate());

        display.setText(result);
    }

    private void clr() {
        TextView display = findViewById(R.id.display);
        display.setText("");
    }

    public void zero(View view) {
        updateDisplay('0');
    }

    public void one(View view) {
        updateDisplay('1');
    }

    public void two(View view) {
        updateDisplay('2');
    }

    public void three(View view) {
        updateDisplay('3');
    }

    public void four(View view) {
        updateDisplay('4');
    }

    public void five(View view) {
        updateDisplay('5');
    }

    public void six(View view) {
        updateDisplay('6');
    }

    public void seven(View view) {
        updateDisplay('7');
    }

    public void eight(View view) {
        updateDisplay('8');
    }

    public void nine(View view) {
        updateDisplay('9');
    }

    public void backspace(View view) {
        backspace();
    }

    public void equals(View view) {
        calculate();
    }

    public void clr(View view) {
        clr();
    }

    public void dot(View view) {
        updateDisplay('.');
    }

    public void left_brace(View view) {
        updateDisplay('(');
    }

    public void right_brace(View view) {
        updateDisplay(')');
    }

    public void add(View view) {
        updateDisplay('+');
    }

    public void subtract(View view) {
        updateDisplay('-');
    }

    public void divide(View view) {
        updateDisplay('/');
    }

    public void multiply(View view) {
        updateDisplay('*');
    }

}