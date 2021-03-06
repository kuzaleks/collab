#include <fstream>
#include <iostream>
#include "src/str.h"


Student input()
{
	cout << "________________" << endl;
	cin.get();
	Student stud;
	cout << "Name: ";  cin.getline(stud.name, MAX);
	cout << "Birthday: ";  cin >> stud.date.d >> stud.date.m >> stud.date.y; 
	cout << "Student's year and mark: ";  cin >> stud.year >> stud.mark;

	return stud;
}

void create(ofstream& fin, int num)
{
	for (int i = 0; i < num; i++){
		Student stud = input();
		fin.write((char*)&stud, sizeof(Student));
	}
}

void outStruct(Student stud)
{
	cout << stud.name << " " << stud.date.d << "." << stud.date.m << "." << stud.date.y << " " << stud.year << " " << stud.mark << endl;
}

void readFile(ifstream& fout)
{
	Student stud;

	fout.read((char*)&stud, sizeof(Student));
	outStruct(stud);
	while (!fout.eof()){
		fout.read((char*)&stud, sizeof(Student));
		outStruct(stud);
		fout.get();
		if(!fout.eof())
			fout.unget();
	}
}

void compare(Student s1, Student& s2)
{
	if (s1.date.y > s2.date.y) s2 = s1;
	else if (s1.date.y == s2.date.y){
		if (s1.date.m > s2.date.m) s2 = s1;
		else if (s1.date.m == s2.date.m){
			if (s1.date.d > s2.date.d) s2 = s1;
		}
	}
}

void createYoung(ofstream& fin, ifstream& fout)
{
	Student stud;
	Student c[5];

	for(int i =0; i < 5; i++){
		c[i].date.y = c[i].date.m = c[i].date.d = 0;
	}

	fout.read((char*)&stud, sizeof(Student));
	compare(stud, c[stud.year - 1]);
	while (!fout.eof()){
		fout.read((char*)&stud, sizeof(Student));
		compare(stud, c[stud.year - 1]);
		fout.get();
		if(!fout.eof())
			fout.unget();
	}

	for (int i = 0; i < 5; i++)
		if (c[i].date.y != 0)
			fin.write((char*)&c[i], sizeof(Student));
}