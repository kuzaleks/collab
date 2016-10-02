// header with prototypes of student's functions that we will test or use in tests

double functionA(double x);
double functionB(double x, float argumentS);

double rootOfEquation(double (*function)(double), float boundaryA, float boundaryB, double accuracyE, int &k_iter);
double rootOfEquation(double (*function)(double, float), float boundaryA, float boundaryB, float argumentS, double accuracyE, int &k_iter);
