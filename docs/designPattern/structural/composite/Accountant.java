

/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 24, 2019
*/

public class Accountant extends Employee {
	int id;
	String name;
	double salary;

	public Accountant(int id, String name, double salary) {
		this.id = id;
		this.name = name;
		this.salary = salary;
	}

	@Override
	public int getId() {

		return this.id;
	}

	@Override
	public String getName() {

		return this.name;
	}

	@Override
	public double getSalary() {

		return this.salary;
	}

	@Override
	public void print() {

		System.out.println("======================================");
		System.out.println("Id = " + getId());
		System.out.println("Name = " + getName());
		System.out.println("Salaray = " + getSalary());
		System.out.println("======================================");

	}
	
	
}
