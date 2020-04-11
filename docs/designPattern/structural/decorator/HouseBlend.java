/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 8, 2019
*/

public class HouseBlend extends Beverage {

	public HouseBlend() {
		description = this.getClass().getName() +  " Coffe";
	}
	
	@Override
	public double cost() {
		
		return 2.0;
	}

}

