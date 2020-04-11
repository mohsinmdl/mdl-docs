
public class Settings {
	
	Preferences settings = Preferences.getInstance();

	public Settings() {

		settings.setCgpa(3.14);
		settings.setContact("03336363636");
		settings.setEmail("mohsinmahmoodmdl@gmail.com");
		settings.setName("Muhammad Mohsin Mahmood");
	}

	public void showSettings() {

		settings.show();
	}

}
