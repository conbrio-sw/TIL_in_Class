functional interface



람다 식 생각

```java
//PriorityQueue<Integer> pqueueInt = new PriorityQueue<>((i1, i2)-> i1-i2); // natural ordering
PriorityQueue<Integer> pqueueInt = new PriorityQueue<>((i1, i2)-> i2-i1); // reverse ordering
```

```java
static class Node implements Comparable<Node>{
		int y, x;
		public Node(int y, int x) {
			this.y = y;
			this.x = x;
		}
		@Override
		public String toString() {
			return "Node [y=" + y + ", x=" + x + "]";
		}
		@Override
		public int compareTo(Node o) {
			
			return o.x - this.x;
		}
	}

	{
			PriorityQueue<Node> pqueue = new PriorityQueue<>();
			pqueue.add(new Node(3,7));
			pqueue.add(new Node(2,5));
			pqueue.add(new Node(5,2));
			pqueue.add(new Node(7,1));
			pqueue.add(new Node(4,6));
			while(!pqueue.isEmpty()) {
				System.out.println(pqueue.poll());
			}
		}
```

```java
PriorityQueue<Node> pqueue = new PriorityQueue<>(
					(n1, n2)-> n1.y == n2.y? n1.x - n2.x : n1.y - n2.y 
					);
// n1.y = n2.y 이면 n1.x n2.x 비교
// 아니면 n1.y, n2, y 비교
```





- 반복해서 출력 (나머지 연산자...) 순환 연산

```java
char [] input = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
		int n = input.length;
		{
			for(int i = 0; i < 2*n; i++) {
				System.out.println(input[i%n]);
			}
		}
```

