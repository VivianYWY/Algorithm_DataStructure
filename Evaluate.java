import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stack;
public class Evaluate {

	public static void main(String[] args) {
		Stack<String> ops = new Stack<String>();
		Stack<Double> vals = new Stack<Double>();
		while (!StdIn.isEmpty())
		{
			// read the char, and push into stack if it is ops
			String s = StdIn.readString();
			if      (s.equals("("))                 ;
			else if (s.equals("+"))      ops.push(s);
			else if (s.equals("-"))      ops.push(s);
			else if (s.equals("*"))      ops.push(s);
			else if (s.equals("/"))      ops.push(s);
			else if (s.equals("sqrt"))   ops.push(s);
			else if (s.equals(")"))
			{
				// if it is ")", then pop a ops and two vals, calculate and push the result into stack
				String op = ops.pop();
				double v = vals.pop();
				if      (op.equals("+")) v = vals.pop() + v;
				else if (op.equals("-")) v = vals.pop() - v;
				else if (op.equals("*")) v = vals.pop() * v;
				else if (op.equals("/")) v = vals.pop() / v;
				else if (op.equals("sqrt")) v = Math.sqrt(v);
				vals.push(v);
			}
			// if it is neither ops or (), then pop it into stack
			else vals.push(Double.parseDouble(s));
		}
		StdOut.println(vals.pop());

	}

}
