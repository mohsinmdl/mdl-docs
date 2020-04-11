
public class FactoryDemo {

	public static void main(String[] args) {
		
		ShapeFactory factory = new ShapeFactory();
		Shape circle = factory.getShape("Circle");
		circle.draw();
		
		Shape rectangle = factory.getShape("rectangle");
		rectangle.draw();
		
		
	}

}
