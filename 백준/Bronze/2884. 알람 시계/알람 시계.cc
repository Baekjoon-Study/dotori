#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(){
	int H, M, k	;

	scanf("%d %d", &H, &M);

	if ((45 <= M) && (M <= 59)) {
		M = M - 45;
		printf("%d %d", H, M);
	}
	else if ((0 <= M) && (M <= 44)) {
		M = M + 60 - 45;
		k = H-1;
		if (H == 0) {
			k = 23;
		}
		printf("%d %d", k, M);
	}

	return 0;
}