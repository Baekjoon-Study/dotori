#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int A;

	scanf("%d", &A);

	if (90 <= A && A <= 100)
		printf("A");
	else if (80 <= A && A <= 89)
		printf("B");
	else if (70 <= A && A <= 79)
		printf("C");
	else if (60 <= A && A <= 69)
		printf("D");
	else if (0 <= A && A <= 59)
		printf("F");

	return 0;
}
