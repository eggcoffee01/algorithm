#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int arr[1000001] = { 1, 1 };


int main() {
	int start, end, temp;
	scanf("%d %d", &start, &end);

	/*¹Ø¿¡ Æ÷¹®À» ¹Ù²ã¾ß ÇÔ*/
		for (int i = 2; i <= end; i++) {
			if (arr[i] == 0) {
				temp = 0;
				for (int j = 2; j < i; j++) {
					if (i % j == 0) {
						temp++;
						break;
					}
				}
				if (temp == 0) {
					for (int k = i + i; k <= end; k += i) {
						if (arr[k] != 1)
							arr[k] = 1;
					}
				}
			}
		}

	for (int i = start; i <= end; i++) {
		if (arr[i] == 0) {
			printf("%d\n", i);
		}
	}
	return 0;

}