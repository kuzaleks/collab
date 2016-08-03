// header with prototypes of functions that we will use in tests

// for of tests point A
double linearEquation(double x)
{
    return (x - 1.0);  // root == 1
}

double quadraticEquation(double x)
{
    return (x * x - 4.0);  // root == 2
}

double cubicEquation(double x)
{
    return (x * x * x - 27.0);  // root == 3
}


// for of tests point B
double linearEquation(double x, float argument)
{
    return (x - 1.0) + argument * 0;  // root == 1
}

double quadraticEquation(double x, float argument)
{
    return (x * x - 4.0);  // root == 2
}

double cubicEquation(double x, float argument)
{
    return (x * x * x - 27.0);  // root == 3
}
