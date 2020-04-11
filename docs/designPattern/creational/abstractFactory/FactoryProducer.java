
public class FactoryProducer {
	
	public static AbstractFactory getFactory(String type){
		
		if (type == null) {
			return null;
		}
		else if (type.equalsIgnoreCase("Shape")) {
			return new ShapeFactory();
		}else if (type.equalsIgnoreCase("Color")) {
			return new ColorFactory();
		}
		
		return null;
		
	}

}
