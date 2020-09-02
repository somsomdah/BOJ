import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class _10815_NumberCards {

	static int findNumber(int[] list, int p, int q, int k) {

		if (p < q) {

			int t = (int) (p + q) / 2;
			int tv = list[t];

			if (tv == k) {
				return 1;
			} else if (k < tv) {
				return findNumber(list, p, t, k);
			} else {
				return findNumber(list, t + 1, q, k);
			}

		} else {

			return 0;
		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		String[] str1 = br.readLine().split(" ");
		
		int[] cardList = new int[n];
		for (int i = 0; i < n; i++) 
			cardList[i] = Integer.parseInt(str1[i]);
		Arrays.sort(cardList);

		int m = Integer.parseInt(br.readLine());
		String[] str2 = br.readLine().split(" ");


		for (int i=0;i<str2.length;i++) {
			int k=Integer.parseInt(str2[i]);
			System.out.print(findNumber(cardList, 0, cardList.length, k)+" ");
		}

		
		br.close();

	}

}
