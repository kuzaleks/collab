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
      TSM_ASSERT_EQUALS("The file with students only first year didn't pass the test!", isEqualFiles("start_only_first_cource.bin", "ready_only_first_cource.bin"), true);
    }

    void testAllFiveCources(void)
    {
      TSM_ASSERT_EQUALS("The file with students all five cources didn't pass the test!", isEqualFiles("start_all_five_cources.bin", "ready_all_five_cources.bin"), true);
    }

private:
    bool isEqualFiles(const char* nameOfStartFile, const char* nameOfReadyFile)
    {
      ifstream fout(nameOfStartFile, ios::binary);
      ofstream fin("file_to_compare.bin", ios::binary);

      createYoung(fin, fout);
      fout.close();
      fin.close();

      Student stud1;
      Student stud2;

      ifstream ourFile(nameOfReadyFile, ios::binary);
      ifstream userFile("file_to_compare.bin", ios::binary);

      ourFile.read((char*)&stud1, sizeof(Student));
      userFile.read((char*)&stud2, sizeof(Student));

      if(strcmp(stud1.name, stud2.name) ||
               stud1.date.y != stud2.date.y ||
               stud1.date.m != stud2.date.m ||
               stud1.date.d != stud2.date.d ||
               stud1.year != stud2.year || 
               stud1.mark != stud2.mark) return false;

      while(!ourFile.eof() && !userFile.eof()){
        ourFile.read((char*)&stud1, sizeof(Student));
        userFile.read((char*)&stud2, sizeof(Student));

        if(strcmp(stud1.name, stud2.name) ||
               stud1.date.y != stud2.date.y ||
               stud1.date.m != stud2.date.m ||
               stud1.date.d != stud2.date.d ||
               stud1.year != stud2.year || 
               stud1.mark != stud2.mark) return false;
        fout.get();
        if(!fout.eof())
            fout.unget();
      }
      return true;
    }
};