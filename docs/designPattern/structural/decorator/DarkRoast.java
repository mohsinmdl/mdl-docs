/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 8, 2019
*/

public class DarkRoast extends Beverage {
	
	public DarkRoast() {
		description = this.getClass().getName() +  " Coffe";
	}
	
	@Override
	public double cost() {
		
		return 3.0;
	}

}

