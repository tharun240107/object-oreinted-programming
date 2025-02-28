
  class MyClass {
    static int count = 0;
    final double PI = 3.14159;

    public MyClass() {
        count++;
    }

    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
        MyClass obj3 = new MyClass();

        System.out.println("Count: " + count);

    }
}

