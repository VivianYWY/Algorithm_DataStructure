import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class tobe_not_tobe {

	public static void main(String[] args) {
		// the test text is "to be or not to - be - - that - - - is"
		FixedCapacityStack<String> s;
		s = new FixedCapacityStack<String>(100);
		while (!StdIn.isEmpty())
		{
			String item = StdIn.readString();
			if (!item.equals("-"))
				s.push(item);
			else if (!s.isEmpty())
				StdOut.print(s.pop() + " ");
		}
		StdOut.println("(" + s.size() + "left on stack)");

	}

}
