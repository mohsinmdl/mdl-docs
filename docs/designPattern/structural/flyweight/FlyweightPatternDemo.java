import java.util.Random;

/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Mar 28, 2019
*/

public class FlyweightPatternDemo {

	public static final String color[] = { "Red", "Green", "Blue", "White", "Black" };
	static Random rand = new Random();

	public static void main(String[] args) {
		
		for (int i = 0; i < 20; i++) {
			
			Circle circle = (Circle) ShapeFactory.getShape(getColor());
			circle.setXcoor(getRandX());
			circle.setYCoor(getRandY());
			circle.draw();
		}
		
	}

	private static String getColor() {

		return color[rand.nextInt(color.length)];
	}

	private static int getRandX() {

		return rand.nextInt(100);
	}

	private static int getRandY() {

		return rand.nextInt(100);
	}

}
