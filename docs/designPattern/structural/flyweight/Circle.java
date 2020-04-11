/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Mar 28, 2019
*/

public class Circle implements Shape {
	private String name = null;
	private int xcoor = 0;
	private int ycoor = 0;

	public Circle(String name) {
		super();
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getXcoor() {
		return xcoor;
	}

	public void setXcoor(int xcoor) {
		this.xcoor = xcoor;
	}

	public int getYcoor() {
		return ycoor;
	}

	public void setYCoor(int ycoor) {
		this.ycoor = ycoor;
	}

	public void draw() {
		System.out.println("Drawing a Circle having " + this.name + " Color at X: " + this.xcoor + " Y :" + this.ycoor
				+ " Coordinates");
	}

}
