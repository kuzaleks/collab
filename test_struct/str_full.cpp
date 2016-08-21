//#include <stdio.h>
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

Student Input()
{
	cout << "________________" << endl;
	cin.get();
	Student stud;
	cout << "Name: ";  cin.getline(stud.name, MAX);
	cout << "Birthday: ";  cin >> stud.date.d >> stud.date.m >> stud.date.y; 
	cout << "Student's cource and mark: ";  cin >> stud.cource >> stud.mark;

	return stud;
}

void create(ofstream& fin, int num)
{
	for (int i = 0; i < num; i++){
		Student stud = Input();
		fin.write((char*)&stud, sizeof(Student));
	}
}

void out_struct(Student stud)
{
	cout << stud.name << " " << stud.date.d << "." << stud.date.m << "." << stud.date.y << " " << stud.cource << " " << stud.mark << endl;
}

void read_file(ifstream& fout)
{
	Student stud;

	fout.read((char*)&stud, sizeof(Student));
	out_struct(stud);
	while (!fout.eof()){
		fout.read((char*)&stud, sizeof(Student));
		out_struct(stud);
		fout.get();// берем символ
		if(!fout.eof())// если он не был последним
			fout.unget();// возвращаем его на место
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

void create_young(ofstream& fin, ifstream& fout)
{
	Student stud;
	Student c[5];

	for(int i =0; i < 5; i++){
		c[i].date.y = c[i].date.m = c[i].date.d = 0;
	}

	fout.read((char*)&stud, sizeof(Student));
	compare(stud, c[stud.cource - 1]);
	/*fout.get();// берем символ
	if(!fout.eof())// если он не был последним
		fout.unget();// возвращаем его на место*/
	
	while (!fout.eof()){
		fout.read((char*)&stud, sizeof(Student));
		compare(stud, c[stud.cource - 1]);
		fout.get();// берем символ
		if(!fout.eof())// если он не был последним
			fout.unget();// возвращаем его на место	
	}

	int k = 0;
	for (int i = 0; i < 5; i++)
		if (c[i].date.y != 0){
			fin.write((char*)&c[i], sizeof(Student));
			k++;
		}
	cout << k << endl;
}



int main()
{/*
	int num_stud;
	cout << "Num of students: "; cin >> num_stud;

	ofstream fin("base_of_stud.bin", ios::binary);

	create(fin, num_stud);
	fin.close();

	ifstream fout("base_of_stud.bin", ios::binary);
	ofstream fin1("base_of_ys.bin", ios::binary);

	read_file(fout);
	fout.close();

	cout << "_____________" << endl;


	ifstream fout2("base_of_stud.bin", ios::binary);
	create_young(fin1, fout2);

	fout.close();
	fin1.close();

	ifstream fout1("base_of_ys.bin", ios::binary);
	read_file(fout1);


	return 0;*/

	int num_stud;
	cout << "Num of students: "; cin >> num_stud;

	ofstream fin("only_first_cource.bin", ios::binary);

	create(fin, num_stud);
	fin.close();

	ifstream fout("only_first_cource.bin", ios::binary);
	ofstream fin1("ready_first_cource.bin", ios::binary);

	read_file(fout);
	fout.close();

	cout << "_____________" << endl;


	ifstream fout2("only_first_cource.bin", ios::binary);
	create_young(fin1, fout2);

	fout.close();
	fin1.close();

	ifstream fout1("ready_first_cource.bin", ios::binary);
	read_file(fout1);


	return 0;
}

