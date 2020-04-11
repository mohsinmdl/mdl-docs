package facadePattern;

public class HomeTheater {

	private Amplifier amp;
	private DVDPlayer dvdPlayer;
	private Light light;
	private Popcorn popcorn;
	private Projecter projecter;

	public HomeTheater() {

		this.amp = new Amplifier();
		this.dvdPlayer = new DVDPlayer();
		this.light = new Light();
		this.popcorn = new Popcorn();
		this.projecter = new Projecter();

	}

	public void watchMovie() {

		popcorn.load();
		popcorn.on();
		
		projecter.lower();

		amp.on();
		amp.medium();
		amp.inputDVD();

		dvdPlayer.on();
		dvdPlayer.load();
		dvdPlayer.sorround();

		projecter.on();
		projecter.inputDVD();
		projecter.wideScreen();

		light.dim();

		dvdPlayer.start();

	}

}
