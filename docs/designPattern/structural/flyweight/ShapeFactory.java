import java.util.HashMap;

/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Mar 28, 2019
*/

public class ShapeFactory {

	private static final HashMap<String, Shape> shapeMap = new HashMap<>();

	public static Shape getShape(String color) {

		Circle circle = (Circle) shapeMap.get(color);

		if (circle == null) {
			circle = new Circle(color);
			shapeMap.put(color, circle);
			System.out.println("Creating Circle of Color : " + color);
		}
		return circle;

	}

}
