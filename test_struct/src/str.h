#include <fstream>
#include <iostream>

using namespace std;


const int MAX = 100;


struct Birthday
{
	int d, m, y;
};

struct Student
{
	char name[MAX];
	Birthday date;
	int cource;
	double mark;
};

Student input();

void create(ofstream& fin, int num);

void out_struct(Student stud);

void read_file(ifstream& fout);

void compare(Student s1, Student& s2);

void create_young(ofstream& fin, ifstream& fout);