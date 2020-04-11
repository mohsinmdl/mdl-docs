/*
 * 
 * Muhammad Mohsin Mahmood
 * SP16-BSE-060
 * 
 * */
public abstract class AbstractFactory {
	
	public abstract VideoPlayer getVideoPlayer(String type);
	public abstract AudioPlayer getAudioPlayer(String type);

}
