import java.util.Iterator;

public class ResizingArrayStack<Item> implements Iterable<Item> 
{
	private Item[] a = (Item[]) new Object[1]; //stack element
	private int N = 0; // number of element
	public boolean isEmpty() {return N == 0;}
	public int size()        {return N;}
	private void resize(int max)
	{
		//move the stack to a new array with size of max
		Item[] temp = (Item[]) new Object[max];
		for (int i = 0; i < N; i++)
		{
			temp[i] = a[i];
		}
		
		a = temp;
	}
	
	public void push(Item item)
	{
		if (N == a.length) resize(2*a.length);
		a[N++] = item;
	}
	
	public Item pop()
	{
		Item item = a[--N];
		a[N] = null;
		if (N > 0 && N == a.length/4)  resize(a.length/2);
		return item;
	}
	
	public Iterator<Item> iterator()
	{
		return new ReverseArrayIterator();
	}
	
	private class ReverseArrayIterator implements Iterator<Item>
	{
		private int i = N;
		public boolean hasNext() {return i > 0;}
		public Item next()       {return a[--i];}
		public void remove()     {              }
		
	}

}
