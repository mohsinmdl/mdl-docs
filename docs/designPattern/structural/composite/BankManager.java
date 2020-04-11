import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/*
*
* @author: 			Muhammad Mohsin Mahmood
* email:			mohsinmahmoodmdl@gmail.com
* Registration#: 	SP16-BSE-060
* Date: 			Apr 24, 2019
*/

public class BankManager extends Employee {
	int id;
	String name;
	double salary;

	public BankManager(int id, String name, double salary) {
		this.id = id;
		this.name = name;
		this.salary = salary;
	}

	List<Employee> employeelist = new ArrayList<>();

	@Override
	public void add(Employee employee) {

		employeelist.add(employee);
	}

	@Override
	public void remove(Employee employee) {

		employeelist.remove(employee);
	}

	@Override
	public Employee getChild(int i) {

		return employeelist.get(i);
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
		
		Iterator<Employee> it = employeelist.iterator();
		while(it.hasNext()){
			Employee emp = (Employee) it.next();
			emp.print();
		}
		
	}

}
