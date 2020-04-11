
public class ColorFactory extends AbstractFactory {

	@Override
	public Color getColor(String type){
		
		if (type ==null) {
			System.out.println("yes i am in");
			return null;
		}
		else if (type.equalsIgnoreCase("Green")) {
			return new Green();
		}
		else if (type.equalsIgnoreCase("Blue")) {
			return new Blue();
		}
		else if (type.equalsIgnoreCase("Red")) {
			return new Red();
		}
		
		
		return null;
		
		
		
	}


	@Override
	public Shape getShape(String shapetype) {
		// TODO Auto-generated method stub
		return null;
	}

	
	

	
	
}
