class Car {
    private String color;
    private String brand;
    private String fuelType;
    private int mileage;
    public Car(String color, String brand, String fuelType, int mileage) {
        this.color = color;
        this.brand = brand;
        this.fuelType = fuelType;
        this.mileage = mileage;
    }

    public void start() {
        System.out.println("The " + color + " " + brand + " is starting.");
    }

    public void stop() {
        System.out.println("The " + color + " " + brand + " is stopping.");
    }

    public void service() {
        System.out.println("The " + color + " " + brand + " requires service.");

    }

    public static void main(String[] args) {
        Car car1 = new Car("Red", "Toyota", "Petrol", 15000);
        Car car2 = new Car("Blue", "Honda", "Diesel", 20000);
        Car car3 = new Car("White", "Tesla", "Electric", 25000);
        car1.start();
        car1.stop();
        car1.service();

        car2.start();
        car2.stop();
        car2.service();

        car3.start();
        car3.stop();
        car3.service();
    }
System.out.println(“t.v.tharun”);
}
