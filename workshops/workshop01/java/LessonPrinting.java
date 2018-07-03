/**
 * File Name: LessonPrinting.java
 * Author: Lawrence (Drew) Whisenant
 * Date Created: 02 July 2018
 * Data Last Modified: 02 July 2018
 * Java Version: 8
 */

/*
  Topics:
    0. Running Java
    1. Comments
    2. Printing and Strings
*/

/*
  0. Running Java
  
  Note that Java is more complicated than what is presented here.
  In Java, all of your code must exist inside classes (you'll see more about what a class is later).
  In general, every file contains one class, and the file must be named:
    ClassName.java
  Where ClassName is the name of the class. The class name cannot contain spaces.
  
  For now, for a class to run, it needs to have a main method (you'll see main methods in this lesson).
  
  Classes are grouped together in packages. You can have 1 or more classes inside a package.
  You'll see more about what a package is later.
  
  Your IDE (Eclipse, IntelliJ, Android Studio, etc.) can handle making packages and .java files for you.
  To run a program in your IDE, press the play button.
  
  You can also run a single Java class from the command line by issuing two commands in the right directory:
    javac ClassName.java
    java ClassName
*/

/*
  1. Comments
  
  In programming, a comment is anything in a code file that is not meant to be executed.
  They allow you to make notes about code or to write code without running it.
  
  In Java, you can comment out a line by starting the line with two forward slashes (//)
  For lesson files, delete the // symbol to run a line, and add it back next time you run the file.
  
  You can also comment out multiple lines or a section of text with this set of symbols:
    /* Comment goes here */
    /* Or
       Spread
       It
       Out
    */
*/
  
// This is how a class looks.
// For now, start all classes with public class and the name of the class.
// There will be a set of curly braces after the name.
public class LessonPrinting {
  // Everything about the class goes between the braces.
  
  // This is what the main method looks like.
  // For now, all your classes should have exactly one of these.
  // The main method should always look like: public static void main(int argc, String[] argv)
  //   followed by a set of curly braces after the last parentheses.
  public static void main(int argc, String[] argv) {
    // Everything about the main method between the braces.
    
    /*
      2. Printing
      When learning to program, one of the first things you need to know
        is how to print information to the screen.
      This is one way you have to get information about what your program 
        as it runs.

      In Java, this done with a set of methods (or functions) called "print," "println," and "printf".
      A method (or function) is some code that you can run by knowing what it's called
        without knowing (possibly) what it does or how it does it.
    */
    
    // Simply put, the prints take some information and write it to the screen.
    // print and printf can print information to the screen, and println does the same thing, but it also ends the line.
    // Uncomment each line to see the difference
    // System.out.print(538);
    // System.out.println(538);
    
    // The print methods "live" in something called out, which lives inside something called System.
    // Notice that each line of code ends with a semicolon.
    // In Java, you run a command or instruction, called a statement, and end it with a semicolon
    //   like how you can end a thought with a period, exclamation point, or question mark.
    
    // You can call println with no arguments to print a single blank line to the screen.
    // System.out.println();
    
    // These lines print a number with a decimal in it on the screen.
    // System.out.print(3.14159);
    // System.out.println(3.14159);
    
    // In programming, we generally refer to text data as a string.
    // A string is written as "string."
    
    // This line prints my name.
    // System.out.print("Drew");
    
    // So do these.
    // System.out.println("Drew");
    // System.out.printf("Drew");
    
    // Again, notice that only println starts a new line.
    
    // This line prints a string with quotes.
    // System.out.println("A quote looks like this:\"");
    
    // This line prints an apostrophe.
    // System.out.println("An apostrophe looks like this:\'");
    
    // We generally call ' a single quote and " a double quote.
    
    // The back slashes indicate a special character.
    // A single quote: \'
    // A double quote: \"
    // A tab: \t
    // A new line: \n
    // The backslash is a signal to say "I don't really want the next letter, I want a special character."
    
    // You can use \n to get the same behavior for print, printf, and println.
    // System.out.print("This ends with a new line!\n");
    // System.out.printf("This ends with a new line!\n");
    // System.out.println("This ends with a new line!");
    
    // print and println can take any kind of argument:
    //   strings, numbers, etc.
    // printf can only take strings, but the strings can have numbers inside them.

    // You can learn more about System.out.print() from the documentation.
    // https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#print(java.lang.String)
    
    // You can learn more about System.out.println() from the documentation.
    // https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#println()
    
    // You can learn more about System.out.printf() from the documentation.
    // https://docs.oracle.com/javase/7/docs/api/java/io/PrintStream.html#printf(java.lang.String,%20java.lang.Object...)    
  }
}
