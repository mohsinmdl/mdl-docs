/*
 * 
 * Muhammad Mohsin Mahmood
 * SP16-BSE-060
 * 
 * */
public class FactoryProducer {

	public static AbstractFactory getFactory(String type) {

		if (type == null) {
			return null;
		} else if (type.equalsIgnoreCase("AudioPlayerFactory")) {
			return new AudioPlayerFactory();
		}else if (type.equalsIgnoreCase("VideoPlayerFactory")) {
			return new VideoPlayerFactory();
		}
		return null;

	}

}
