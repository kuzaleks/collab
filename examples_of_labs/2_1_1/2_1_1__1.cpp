#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    int k = 2;
    //std::cin >> k;

    int numberOf[10] = {0};
    for (; n > 0; n /= 10) {
        switch (n % 10) {
        case 0:
            ++numberOf[0];
            break;
        case 1:
            ++numberOf[1];
            break;
        case 2:
            ++numberOf[2];
            break;
        case 3:
            ++numberOf[3];
            break;
        case 4:
            ++numberOf[4];
            break;
        case 5:
            ++numberOf[5];
            break;
        case 6:
            ++numberOf[6];
            break;
        case 7:
            ++numberOf[7];
            break;
        case 8:
            ++numberOf[8];
            break;
        default:
            ++numberOf[9];
            break;
        }
    }

    int numberOfequalsDigits = 0;
    for (int i = 0; i < 10; ++i)
        if (numberOf[i] > 1)
            numberOfequalsDigits += numberOf[i];

    if (numberOfequalsDigits == k)
        std::cout << "True";
    else
        std::cout << "False";

    return 0;
}
