/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Mar 29, 2019
* Task Description: Consider a Word text editor where a user can type alphabet and takes one byte in momory . 
					Implemet flyweight patter to use memory efficeiently for storage of characters. 
					Alphabets are A,B,C,D,E
*/

package LabTask;

import java.util.Random;

public class FlyweightDemo {

	private static char alpha[] = { 'A', 'B', 'C', 'D', 'E' };

	public static void main(String[] args) {

		for (int i = 0; i < 100; i++) 
			AlphabetGenerator.getChar( getRandomAlpha() );
		

	}

	private static char getRandomAlpha() {

		Random rand = new Random();
		return alpha[rand.nextInt(5)];

	}

}
