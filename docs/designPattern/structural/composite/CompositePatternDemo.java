/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 24, 2019
*/

public class CompositePatternDemo {
	public static void main(String[] args) {

		Employee manager = new BankManager(101, "BankManager", 80000.00);
		Employee cash1 = new Cashier(202, "Cashier1", 20000.00);
		Employee cash2 = new Cashier(203, "Cashier2", 20000.00);
		Employee accountant = new Accountant(204, "Accountant", 42000.00);

		manager.add(cash1);
		manager.add(cash2);
		manager.add(accountant);

		manager.print();

	}
}
