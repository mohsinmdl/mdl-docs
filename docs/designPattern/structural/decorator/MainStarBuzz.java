/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 8, 2019
*/

public class MainStarBuzz {
	public static void main(String[] args) {
		
		HouseBlend obj = new HouseBlend();
		Mocha moc = new Mocha(obj);
		
		System.out.println(obj.getDescription());
		System.out.println(obj.cost());
	
		System.out.println(moc.getDescription());
		System.out.println(moc.cost());
		
		Beverage coffe = new DarkRoast();
		coffe = new Mocha(coffe);
		coffe = new Soy(coffe);
		
		System.out.println(coffe.getDescription());
		System.out.println(coffe.cost());
	

		
		
		

	}
}
