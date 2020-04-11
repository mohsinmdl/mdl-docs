
public class ShapeFactory {
	
	

	public Shape getShape(String shapetype){
		
		if (shapetype == null) {
			return null;
		}
		else if ( shapetype.equalsIgnoreCase("circle") ) {
			return new Circle();
		}
		else if ( shapetype.equalsIgnoreCase("rectangle") ) {
			return new Rectangle();
		}
		else if ( shapetype.equalsIgnoreCase("Square") ) {
			return new Square();
		}
		
		return null;
		
	}

	
}
