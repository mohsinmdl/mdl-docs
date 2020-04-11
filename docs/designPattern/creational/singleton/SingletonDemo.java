
public class SingletonDemo {

	public static void main(String[] args) {

		
		Settings settings = new Settings();
		settings.showSettings();

		System.out.println("\nHome: Settings");
		System.out.println("================");
		Home home = new Home();
		home.showSettings();

		System.out.println("\nContact: Settings");
		System.out.println("================");
		Contact contact = new Contact();
		contact.showSettings();

	}
}
