/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 8, 2019
*/

public class Mocha extends CondimentDecorator {
	
	Beverage bev;
	public Mocha(Beverage bev) {
		this.bev = bev;
		
	}
	
	
	@Override
	public String getDescription() {
		
		return bev.getDescription() + " + " + this.getClass().getName() ;
	}

	@Override
	public double cost() {
		
		return 0.2 + bev.cost() ;
	}

}

