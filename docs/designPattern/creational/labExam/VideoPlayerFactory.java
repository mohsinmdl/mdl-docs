/*
 * 
 * Muhammad Mohsin Mahmood
 * SP16-BSE-060
 * 
 * */
public class VideoPlayerFactory extends AbstractFactory {

	public VideoPlayer getVideoPlayer(String type) {
		if (type == null) {
			return null;
		} else if (type.equalsIgnoreCase("VLCMediaPlayer")) {
			return new VLCMediaPlayer();
		} else if (type.equalsIgnoreCase("WindowsMediaPlayer")) {
			return new WindowsMediaPlayer();
		} else if (type.equalsIgnoreCase("AdobeFlashPlayer")) {
			return new AdobeFlashPlayer();
		}

		return null;
	}

	public AudioPlayer getAudioPlayer(String type) {
		// TODO Auto-generated method stub
		return null;
	}


}
