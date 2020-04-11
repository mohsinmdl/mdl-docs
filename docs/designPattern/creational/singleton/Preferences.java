// Singleton Class


public class Preferences {

	private static Preferences uniqueIns;

	private String name;
	private String contact;
	private String email;
	private double cgpa;

	private Preferences() {
	}

	public static Preferences getInstance() {

		if (uniqueIns == null)
			uniqueIns = new Preferences();

		return uniqueIns;
	}

	// Setter methods

	
	public void show(){
		
		System.out.println("Name: " + uniqueIns.getName());
		System.out.println("Email: " + uniqueIns.getEmail());
		System.out.println("Contact: " + uniqueIns.getContact());
		System.out.println("CGPA: " + uniqueIns.getCgpa());
		
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setContact(String contact) {
		this.contact = contact;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public void setCgpa(double cgpa) {
		this.cgpa = cgpa;
	}

	// Getter methods

	public String getName() {
		return name;
	}

	public String getContact() {
		return contact;
	}

	public String getEmail() {
		return email;
	}

	public double getCgpa() {
		return cgpa;
	}
	
	

}
