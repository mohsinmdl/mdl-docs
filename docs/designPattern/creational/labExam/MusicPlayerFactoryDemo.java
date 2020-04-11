/*
 * 
 * Muhammad Mohsin Mahmood
 * SP16-BSE-060
 * 
 * */

public class MusicPlayerFactoryDemo {
	
	public static void main(String[] args) {
		
		
		//getting Audio Factory 
		AbstractFactory factory = FactoryProducer.getFactory("AudioPlayerFactory");
		
		// getting "MP3Player" audio player
		AudioPlayer mp3Player = factory.getAudioPlayer("MP3Player");
		mp3Player.play();
		
		AudioPlayer jetaudio = factory.getAudioPlayer("JetAudioHDPlayer");
		jetaudio.play();
		
		AudioPlayer winamp = factory.getAudioPlayer("WinAmpPlayer");
		winamp.play();
		
		System.out.println("\n=======================================\n");
		
		//Creating Video Factory 
		AbstractFactory factory2 = FactoryProducer.getFactory("VideoPlayerFactory");
	
		VideoPlayer vlc = factory2.getVideoPlayer("VLCMediaPlayer");
		vlc.play();
		
		VideoPlayer wmp = factory2.getVideoPlayer("WindowsMediaPlayer");
		wmp.play();
		
		VideoPlayer flash = factory2.getVideoPlayer("AdobeFlashPlayer");
		flash.play();
		
		
		
		
		
	}

}
