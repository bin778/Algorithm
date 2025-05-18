import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int T = s.nextInt();
		int S = s.nextInt();
		s.close();
		
		if (S == 0) {
			if (T >= 12 && T <= 16) {
				System.out.println(320);
			} else {
				System.out.println(280);
			}
		} else {
			System.out.println(280);
		}
	}
}