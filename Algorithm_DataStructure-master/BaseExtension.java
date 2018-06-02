
public class BaseExtension {

	public static void main(String[] args) {
		String s = args[0];
		int dot = s.indexOf(".");
		String base = s.substring(0, dot);
		String extension = s.substring(dot + 1, s.length());
	}

}
