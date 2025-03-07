// Base class for addition
class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}

// Derived class for subtraction
class SubCalculator extends Calculator {
    public int subtract(int a, int b) {
        return a - b;
    }
}

// Further derived class for multiplication
class MultiCalculator extends SubCalculator {
    public int multiply(int a, int b) {
        return a * b;
    }
}

// Further derived class for division
class FinalCalculator extends MultiCalculator {
    public double divide(int a, int b) {
        if (b != 0) {
            return (double) a / b;
        } else {
            System.out.println("Error: Division by zero!");
            return Double.NaN; // Return "Not a Number" when dividing by zero
        }
    }
}

// Main class to demonstrate functionality
class Main {
    public static void main(String[] args) {
        FinalCalculator cal = new FinalCalculator();

        // Input values
        int a = 15;
        int b = 3;

        // Display results of operations
        System.out.println("Addition: " + cal.add(a, b));
        System.out.println("Subtraction: " + cal.subtract(a, b));
        System.out.println("Multiplication: " + cal.multiply(a, b));
        System.out.println("Division: " + cal.divide(a, b));
    }
}
