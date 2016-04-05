/**
 * Created by bklo on 3/30/16.
 */

import java.util.Scanner;

public class JavaInput {
    static Scanner userInput = new Scanner(System.in);

    public static void main(String[] args){
        System.out.print("What is your favorite number: ");
        if (userInput.hasNextInt()){
            int numberEntered = userInput.nextInt();
            System.out.println("Your favorite number is " + numberEntered);
        }
        else{
            System.out.println("Please enter an integer next time");
        }
    }
}
