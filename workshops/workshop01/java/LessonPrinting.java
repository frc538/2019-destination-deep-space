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

      In Java, this done with a set of methods (or functions) called "print" and "println".
      A method (or function) is some code that you can run by knowing what it's called
        without knowing (possibly) what it does or how it does it.
    */
    
    // Simply put, print and println take some information and write it to the screen.

  }
}
