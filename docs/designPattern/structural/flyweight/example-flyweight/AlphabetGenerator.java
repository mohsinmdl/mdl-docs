/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Mar 29, 2019

*/

package LabTask;

import java.util.HashMap;

public class AlphabetGenerator {

	private static final HashMap<Character, Character> charmap = new HashMap<>();

	public static char getChar(char ch) {

		Character retch = charmap.get(ch);

		if (retch == null) {

			retch = ch;
			charmap.put(ch, ch);

			System.out.println("Char '" + ch + "' is added to the Hashmap");
		} else 
			System.out.println(retch);
		
		return retch;
	}

}
