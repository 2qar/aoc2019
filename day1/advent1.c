#include <stdio.h>

int fuelcost(int i) {
	return i / 3 - 2;
}

int fuel(int i) {
	int cost = 0;
	while (fuelcost(i) > 0) {
		cost += fuelcost(i);
		i = fuelcost(i);
	}
	return cost;
}

int main() {
	FILE *f = fopen("advent1.txt", "r");

	int n, m;
	int t = 0;
	while((n = fscanf(f, "%d\n", &m)) > 0)
		t += fuel(m);

	printf("%d\n",t);
	fclose(f);
}
