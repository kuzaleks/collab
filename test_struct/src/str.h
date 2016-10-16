#include <fstream>
#include <iostream>

using namespace std;


const int MAX = 74;


struct Birthday
{
	int d, m, y;
};

struct Student
{
	char name[MAX];
	Birthday date;
	int year;
	double mark;
};

Student input();

void create(ofstream& fin, int num);

void outStruct(Student stud);

void readFile(ifstream& fout);

void compare(Student s1, Student& s2);

void createYoung(ofstream& fin, ifstream& fout);