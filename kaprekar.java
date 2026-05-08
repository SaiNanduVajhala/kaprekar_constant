import java.util.*;

public class kaprekar {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a 4-digit number: ");
        int num = sc.nextInt();

        while (num != 6174) {

            String s = String.format("%04d", num);

            char[] arr = s.toCharArray();
            Arrays.sort(arr);

            String smallStr = new String(arr);
            String bigStr = new StringBuilder(smallStr).reverse().toString();

            int small = Integer.parseInt(smallStr);
            int big = Integer.parseInt(bigStr);

            num = big - small;

            System.out.println(big + " - " + small + " = " + num);
        }

        System.out.println("Kaprekar Constant reached: 6174");
    }
}