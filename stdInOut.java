import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class stdInOut {

	public static void main(String[] args) {
		String query = args[0];
		while (!StdIn.isEmpty())
		{
			String s = StdIn.readLine();
			if (s.contains(query)) StdOut.println(s);
		}
		
		/////////////////////////////
		String input = StdIn.readAll();
		String[] words = input.split("\\s+");
	}
}
