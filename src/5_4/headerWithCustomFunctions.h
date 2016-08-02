// header with prototypes of student's functions that we will test or use in tests

double functionA(double x);
double functionB(double x, float argumentS);

double rootCalculation(double (*function)(double), float boundaryA, float boundaryB, double accuracyE, int &k_iter);
double rootCalculation(double (*function)(double, double), float boundaryA, float boundaryB, double argumentS, double accuracyE, int &k_iter);
