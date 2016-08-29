// MyTestSuite1.h
#include <cxxtest/TestSuite.h>
#include <string>
#include "src/str.h"

class MyTestSuite1 : public CxxTest::TestSuite
{
public:
    void testGeneral(void)
    {
      TSM_ASSERT_EQUALS("The general case hasn't passed the test!", isEqualFiles("start_general_case.bin", "ready_general_case.bin"), true);
    }

    void testOnlyFirstCource(void)
    {
      TSM_ASSERT_EQUALS("The file with students only first cource didn't pass the test!", isEqualFiles("start_only_first_cource.bin", "ready_only_first_cource.bin"), true);
    }

    void testAllFiveCources(void)
    {
      TSM_ASSERT_EQUALS("The file with students all five cources didn't pass the test!", isEqualFiles("start_all_five_cources.bin", "ready_all_five_cources.bin"), true);
    }

private:
    bool isEqualFiles(const char* name_of_start_file, const char* name_of_ready_file)
    {
      ifstream fout(name_of_start_file, ios::binary);
      ofstream fin("file_to_compare.bin", ios::binary);

      create_young(fin, fout);
      fout.close();
      fin.close();

      Student stud1;
      Student stud2;

      ifstream our_file(name_of_ready_file, ios::binary);
      ifstream user_file("file_to_compare.bin", ios::binary);

      our_file.read((char*)&stud1, sizeof(Student));
      user_file.read((char*)&stud2, sizeof(Student));
        //cout << "__________" << endl;
        //out_struct(stud1);
        //out_struct(stud2);
        //cout << "__________" << endl;

      if(strcmp(stud1.name, stud2.name) ||
               stud1.date.y != stud2.date.y ||
               stud1.date.m != stud2.date.m ||
               stud1.date.d != stud2.date.d ||
               stud1.cource != stud2.cource || 
               stud1.mark != stud2.mark) return false;

      while(!our_file.eof() && !user_file.eof()){
        our_file.read((char*)&stud1, sizeof(Student));
        user_file.read((char*)&stud2, sizeof(Student));
        //cout << "__________" << endl;
        //out_struct(stud1);
        //out_struct(stud2);
        //cout << "__________" << endl;

        if(strcmp(stud1.name, stud2.name) ||
               stud1.date.y != stud2.date.y ||
               stud1.date.m != stud2.date.m ||
               stud1.date.d != stud2.date.d ||
               stud1.cource != stud2.cource || 
               stud1.mark != stud2.mark) return false;
        fout.get();
        if(!fout.eof())
            fout.unget();
      }
      return true;
    }
};