public class Car implements Cloneable {

	private Person owner;

	public Car() {

	}

	public void setOwner(String name) {
		Person owner = new Person(name);
		this.owner = owner;
	}

	public Person getOwner() {
		return owner;
	}

	
	public Object clone() {
		try {
			Car car = (Car) super.clone();
			return car;
		} catch (CloneNotSupportedException e) {
			throw new AssertionError();
		}
	}
	
	
}
