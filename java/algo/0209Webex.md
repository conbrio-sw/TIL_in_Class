- 스트링 빌더를 쓰면 (시스템 아웃이 많을 경우) 보다 실행속도 측면에서 이득을 많이 볼 수 있다.

  - IO를 많이 왔다갔다하면 시간이 많이 걸리기 때문
  - 단 시스템 아웃이 적다면 메모리에 저장을 해야하는 스트링 빌더가 불리할 수 있다.

  ```java
  StringBuilder sb = new StringBuilder();
  sb.append(stack.peek()[0] + " "); // 이것보다
  sb.append(stack.peek()[0]).append(" "); // 이게 더 빠르다.
  // 끄트머리 지우기
  if(!isEmpty()) sb.setLength(sb.length()-2); // 맨 뒤에 2글자 지워주기
  sb.append("]");
  return sb.toString();
  ```

- 실제 개발하면 DB 쪽에서 (백엔드, 프론트엔드와 비교시) 속도가 느리다.
  - 전문가가 뭐 넘겨주는데(튜닝) 기가 막히다고 한다...
  - 프론트 엔드에서 문제가 생기는 경우
    - 익스플로러에서 HTML 썼을 때...
  - 백 엔드에서 문제가 생기는 경우
    - String.concat 문제 (스트링 객체 2개 생성)
    - 다수 클라이언트 연결 시 느려짐 (+ 있으면...)
    - 근데 현업에서는 나대지 말자.
  - 다 해결했는데 느리다?
    - 하드웨어를 늘려달라고 하자.

### 조합, 부분집합

```java
public class comb {
	static int COUNT = 0;
	static int[] src = { 1, 2, 3, 4, 5 };
	static int[] tgt = new int[3];

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		comb(0, 0);
		System.out.println(COUNT);
	}
	public static void comb(int tgtIdx, int start) {
		// 기저조건
		if (tgtIdx == tgt.length) {
			// complete code
			System.out.println(Arrays.toString(tgt));
			COUNT++;
			return;
		}
		if(start == src.length) return;
		tgt[tgtIdx] = src[start];
		comb(tgtIdx + 1, start + 1); //start증가, tgt 증가 ==> 현재 start를 tgt가 받아들이고 다음으로 간다.
		comb(tgtIdx, start + 1);	// start증가, tgt 증가x ==> 현재 start를 받아들이지 않고 start를 증가
	}
}
// 신박한 조합 풀이
```

```java
import java.util.ArrayList;
import java.util.Arrays;
// 0~9 까지의 숫자를 2개의 그룹으로 나눈뒤
// 두 그룹의 원소의 수가 3보다 크거나 같은 경우만 출력(두 그룹 모두 출력)
public class Comb2 {
	static int COUNT = 0;
	static int[] src = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // 제일 중요
	
	static boolean[] isSelected = new boolean[src.length];
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		subset(0);
		System.out.println(COUNT);
	}
	public static void subset(int srcIdx) {
		// 기저조건
		if (srcIdx == src.length) {
			complete();
			return;
		}
		// 선택하고 간다
		isSelected[srcIdx] = true;
		subset(srcIdx+1);
		// 선택안하고 간다
		isSelected[srcIdx] = false;
		subset(srcIdx+1);
	}
	public static void complete() {
		ArrayList<Integer> groupA = new ArrayList<Integer>();
		ArrayList<Integer> groupB = new ArrayList<Integer>();
		for(int i = 0; i < src.length; i++) {
			if(isSelected[i]) groupA.add(src[i]);
			else groupB.add(src[i]);
		}
		if(groupA.size() >= 3 && groupB.size() >= 3) {
			COUNT++;
			System.out.println("=================================");
			for (int n : groupB) {
				System.out.print(n + " ");
			}
			System.out.println();
			for (int n : groupA) {
				System.out.print(n + " ");
			}
			System.out.println();
			System.out.println();
		}
	}
}
// 부분집합 2개 고르기
```



### DFS

- 가지치기
- 기저조건
- 트리구조 만들기