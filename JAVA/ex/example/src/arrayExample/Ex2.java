package arrayExample;

//�ߺ��� ��Ҹ� ������ �� ���ο� �迭�� ��ȯ�ϴ� �޼ҵ带 �ۼ��Ͻÿ�.
//�ߺ� ���ŵ� �� ��ҿ��� �⺻ �� 0���� ����
//int[] arr = {5, 10, 9, 27, 2, 8, 10, 4, 27, 1};

import java.util.Arrays;

public class Ex2 {
	public static void main(String[] args) {
		
		int[] arr = {5, 10, 9, 27, 2, 8, 10, 4, 27, 1};
		// �ߺ��� ������ ���� ������ �迭, �ߺ��� ���ŵ� Ƚ��
		int[] temp = new int[10];
		int count = 0;
		
		// �ߺ� ���� ��
		System.out.println(Arrays.toString(arr));
		
		// for���� �̿��� �ߺ� ����
		// arr[i]�� temp[j]�� ���� ���ٸ� �ߺ��̹Ƿ� 0���� ��ȯ
		for (int i = 0; i < arr.length; i++) {
			boolean flag = false;
			for (int j = 0; j < arr.length; j++) {		
				if (arr[i] == temp[j]) {
					flag = true;
					temp[count++] = 0;
				}
			}
			// �ߺ��� �ƴϸ� temp �迭�� ���� ����
			if(!flag) {
				temp[count++] = arr[i];
			}
		}

		// �ߺ��� ������ �迭�� result �迭�� ����
		int[] result = new int[count];
		for (int i = 0; i < result.length; i++) {
			result[i] = temp[i];
		}
		
		// ��� �� ���
		System.out.println(Arrays.toString(result));
		
	}
}