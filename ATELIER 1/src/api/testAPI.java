package api;

public class testAPI {
	private static int x1 = 3;
	private static int x2 = 10;
	private static String n1 = "toto";
	private static String n2 = "titi";

	public static void main(String[] args) {
		System.out.println(Math.PI);
		System.out.println(Math.random());
		System.out.println((int)(Math.random()*(3)+1));
		System.out.println(Math.max(x1, x2));
		System.out.println(n1.compareTo(n2));
		
	}

}
