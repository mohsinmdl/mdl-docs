/*
 * 
 * Muhammad Mohsin Mahmood
 * SP16-BSE-060
 * 
 * */
public class AudioPlayerFactory extends AbstractFactory {

	public AudioPlayer getAudioPlayer(String type) {
		if (type == null) {
			return null;
		} else if (type.equalsIgnoreCase("MP3Player")) {
			return new MP3Player();
		} else if (type.equalsIgnoreCase("JetAudioHDPlayer")) {
			return new JetAudioHDPlayer();
		} else if (type.equalsIgnoreCase("WinAmpPlayer")) {
			return new WinAmpPlayer();
		}

		return null;
	}

	public VideoPlayer getVideoPlayer(String type) {
		// TODO Auto-generated method stub
		return null;
	}

}
