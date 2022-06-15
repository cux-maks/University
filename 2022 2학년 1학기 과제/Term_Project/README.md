ΩOhm PC 관리 프로그램

## 필수 기능
#### 1. 회원제로 운영
#### 2. PC방 방문 횟수에 따른 포인트 점수 또는 Advantage 기능 부여

## 추가 기능
#### 1. 시간제 - 남은 시간 확인 및 종료 10분, 5분 전 알림
#### 2. 회원 등급 관리
#### 3. 음식 주분 - 기존 PC방과 동일
#### 4. 손님이 카운터에 문의하기 위한 메신저 기능
#### 5. 제자리 결제(Ex: 시간 충전, 음식 주문 등)
#### 6. 자리이동 및 외출 또는 자리 비움, 예약, 퇴장
#### 7. 회원 가입 및 탈퇴

###### \<PC_Management.cpp\>
```c++
#define _CRT_SECURE_NO_WARNINGS
#define admin_id "ohm_admin"
#define admin_pw "ohm_716_admin"

#include <iostream>
#include <fstream>
#include <vector>
#include <Windows.h>
#include <sstream>
#include <ctime>
#include "member.h"
#include "non_member.h"

using namespace std;

time_t curTime = time(NULL);
struct tm* t = localtime(&curTime);

void Delete_Save_Data(); // 모든 데이터 삭제
void Read_Save_Data(vector<member>& m); // 데이터 불러오기
void Save_Members_Data(vector<member>& m); // 데이터 저장
int Get_Current_Year(); // 현재 년도 불러오기
int Get_Current_Month(); // 현재 월 불러오기
int Get_Current_Day(); // 현재 일 불러오기
int Get_Current_Hour(); // 현재 시 불러오기
int Get_Current_Min(); // 현재 분 불러오기
int Get_Current_Sec(); // 현재 초 불러오기
vector<string> split(string str, char Delimiter); // 특정 문자 기준 string 나누기
member new_Member(); // 신규 회원
n_member new_Non_Member(); // 신규 비회원

int main() {

	vector<member> u;
	vector<n_member> n_u;

	Read_Save_Data(u);

home:

	string id_input, pw_input;
	bool admin_login = 0;
	bool login = 0;
	int login_cnt = 0;
	int state = 0;

	cout << "---------- ΩOhm PC ----------" << endl;
	cout << "1. 로그인" << endl;
	cout << "2. 회원가입" << endl;
	cout << "3. 비회원 이용" << endl;
	cout << "4. 프로그램 종료" << endl;
	cout << ">> ";
	cin >> state;

	if (state == 1) { // 로그인

		do {

			system("cls");

			cout << "---------- ΩOhm PC Login ----------" << endl;
			cout << "ID: ";
			cin >> id_input;
			cout << "PW: ";
			cin >> pw_input;

			if (id_input == admin_id && pw_input == admin_pw) { // 관리자인가?
				cout << "관리자 로그인 성공." << endl;
				login = 1;
				admin_login = 1;
			}
			else {

				if (u.size() == 0) { // 회원 정보의 수가 0일 때 그냥 로그인 실패

					cout << "로그인 실패." << endl;
					login_cnt += 1;
					Sleep(1000);
					system("cls");

				}
				else { // 그게 아니라면 탐색

					for (int i = 0; i < u.size(); i++) {

						if (id_input == u[i].GetId() && pw_input == u[i].GetPw()) { // 있으면 로그인 성공

							cout << "로그인 성공." << endl;
							login = 1;

						}
						else if (i == u.size()) { // 똑같은 유저 없으면 로그인 실패

							cout << "로그인 실패." << endl;
							login_cnt += 1;
							Sleep(1000);
							system("cls");

						}

					}

				}

			}

			if (login_cnt == 5) { // 로그인 5회 실패할 경우 프로그램 종료

				cout << "로그인 5회 실패." << endl;
				cout << "프로그램을 종료합니다." << endl;
				Sleep(500);
				return 0;

			}

		} while (login == 0);
	}
	else if (state == 2) { // 회원가입 

		u.push_back(new_Member());
		Save_Members_Data(u);
		system("cls");
		goto home;

	}
	else if (state == 3) { // 비회원 사용

		n_u.push_back(new_Non_Member());

	}
	else if (state == 4) { // 프로그램 종료

		cout << "프로그램을 종료합니다." << endl;
		Save_Members_Data(u);
		return 0;

	}
	else { // 의도되지 않은 선택지

		cout << "해당 선택지는 존재하지 않습니다." << endl;
		Sleep(500);
		system("cls");
		goto home;

	}

	system("cls");

	login_cnt = 0;

	if (admin_login == 1) { // 관리자 로그인 화면

		cout << "---------- ΩOhm PC 관리 프로그램 ----------" << endl;

	}
	else if (state == 3) { // 비회원 사용 화면

		cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;
		cout << "※비회원 이용자는 음식 주문 및 제자리 결제, 자리 이동 및 외출 또는 예약기능, 카운터 문의(메신저) 기능을 사용하실 수 없습니다." << endl;

	}
	else if(state == 1) { // 회원 사용 화면

			cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;

	}

	return 0;

}

void Read_Save_Data(vector<member>& m) {

	ifstream readData("Member_Data.txt");

	if (readData.is_open()) {

		string first_line;
		string date_time;
		getline(readData, first_line);
		int n = stoi(first_line);
		getline(readData, date_time);

		if (n != 0) {

			for (int i = 0; i < n; i++) {

				string str;
				getline(readData, str);

				vector<string> result = split(str, ' ');
				string name = result[0];
				string id = result[1];
				string pw = result[2];
				string tel = result[3];
				string email = result[4];
				int age = stoi(result[5]);
				string grade = result[6];
				int point = stoi(result[7]);
				vector<string> buffer = split(result[8], ':');
				vector<int> last_time;
				for (int i = 0; i < 6; i++) {
					last_time.push_back(stoi(buffer[i]));
				}

				member temp(name, id, pw, tel, email, age, grade, point, last_time);
				
				m.push_back(temp);

			}

		}
		else {

			cout << "There is no data." << endl;

		}

	}
	else {
		
		cout << "There is no data." << endl;

	}

}

void Delete_Save_Data() {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << 0 << endl;
	outfile << "Warning, Clear." << endl;

}

void Save_Members_Data(vector<member>& m) {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << m.size() << endl;
	outfile << Get_Current_Year() << ":" << Get_Current_Month() << ":" << Get_Current_Day() << ":" << Get_Current_Hour() << ":" << Get_Current_Min() << ":" << Get_Current_Sec() << endl;

	for (int i = 0; i < m.size(); i++) {

		string buffer = m[i].GetName();
		buffer += " ";
		buffer += m[i].GetId();
		buffer += " ";
		buffer += m[i].GetPw();
		buffer += " ";
		buffer += m[i].GetTel();
		buffer += " ";
		buffer += m[i].GetEmail();
		buffer += " ";
		buffer += to_string(m[i].GetAge());
		buffer += " ";
		buffer += m[i].GetGrade();
		buffer += " ";
		buffer += to_string(m[i].GetPoint());
		buffer += " ";
		buffer += to_string(m[i].Get_Last_Year());
		buffer += ":";
		buffer += to_string(m[i].Get_Last_Month());
		buffer += ":";
		buffer += to_string(m[i].Get_Last_Day());
		buffer += ":";
		buffer += to_string(m[i].Get_Last_Hour());
		buffer += ":";
		buffer += to_string(m[i].Get_Last_Min());
		buffer += ":";
		buffer += to_string(m[i].Get_Last_Sec());
		outfile << buffer << endl;

	}

}

member new_Member() {

	string name, id, pw, email, tel;
	int age;

	cout << "---------- 회원가입 ----------" << endl;
	cout << "ID: ";
	cin >> id;
	cout << "PW: ";
	cin >> pw;
	cout << "이름: ";
	cin >> name;
	cout << "나이: ";
	cin >> age;
	cout << "전화번호: ";
	cin >> tel;
	cout << "e-mail: ";
	cin >> email;

	member temp(name, id, pw, tel, email, age);

	cout << "회원가입에 성공했습니다." << endl;

	return temp;

}

n_member new_Non_Member() {

	string name, tel;
	int age;

	cout << "---------- 비회원 필수 정보 입력 ----------" << endl;
	cout << "이름: ";
	cin >> name;
	cout << "나이: ";
	cin >> age;
	cout << "전화번호: ";
	cin >> tel;

	n_member temp(name, tel, age);

	return temp;

}

vector<string> split(string str, char Delimiter) {
	istringstream iss(str);
	string buffer;

	vector<string> result;

	while (getline(iss, buffer, Delimiter)) {
		result.push_back(buffer);
	}

	return result;
}

int Get_Current_Year() {

	return (t->tm_year) + 1900;

}

int Get_Current_Month() {

	return (t->tm_mon) + 1;

}

int Get_Current_Day() {

	return t->tm_mday;

}

int Get_Current_Hour() {

	return t->tm_hour;

}

int Get_Current_Min() {

	return t->tm_min;

}

int Get_Current_Sec() {

	return t->tm_sec;

}
```

###### \<member.h\>
```c++
#pragma once

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> null(6);

class member {

	string name, id, pw, email, tel, grade;
	vector<int> last_time;
	int age, point;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age, string _grade = "Bronze", int _point = 0, vector<int> _last_time = null) {
		name = _name;
		tel = _tel;
		id = _id;
		pw = _pw;
		email = _email;
		age = _age;
		grade = _grade;
		point = _point;
		last_time = _last_time;
	}
	member(const member& u) {
		name = u.name;
		tel = u.tel;
		id = u.id;
		pw = u.pw;
		email = u.email;
		age = u.age;
		grade = u.grade;
		point = u.point;
		last_time = u.last_time;
	}
	~member() {
		name.clear();
		tel.clear();
		id.clear();
		pw.clear();
		email.clear();
		grade.clear();
		last_time.erase(last_time.begin(), last_time.end());
		age = 0;
		point = 0;
	}

	void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "ID: " << id << endl;
		cout << "PW: " << pw << endl;
		cout << "회원 등급: " << grade << endl;
		cout << "적립 포인트: " << point << endl;
		cout << "Tel: " << tel << endl;
		cout << "E-mail: " << email << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	string GetId() { return id; }
	string GetPw() { return pw; }
	string GetEmail() { return email; }
	string GetGrade() { return grade; }
	int GetAge() { return age; }
	int GetPoint() { return point; }
	int Get_Last_Year() { return last_time[0]; }
	int Get_Last_Month() { return last_time[1]; }
	int Get_Last_Day() { return last_time[2]; }
	int Get_Last_Hour() { return last_time[3]; }
	int Get_Last_Min() { return last_time[4]; }
	int Get_Last_Sec() { return last_time[5]; }

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetGrade(string _grade) { grade = _grade; }
	void SetAge(int _age) { age = _age; }
	void SetPoint(int _point) { point = _point; }
	void Set_Last_Year(int _y) { last_time[0] = _y; }
	void Set_Last_Month(int _mo) { last_time[1] = _mo; }
	void Set_Last_Day(int _d) { last_time[2] = _d; }
	void Set_Last_Hour(int _h) { last_time[3] = _h; }
	void Set_Last_Min(int _mi) { last_time[4] = _mi;}
	void Set_Last_Sec(int _s) { last_time[5] = _s; }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelGrade() { grade.clear(); }
	void DelAge() { age = 0; }
	void DelPoint() { point = 0; }
	void Del_Last_Year() { last_time[0] = 0; }
	void Del_Last_Month() { last_time[1] = 0; }
	void Del_Last_Day() { last_time[2] = 0; }
	void Del_Last_Hour() { last_time[3] = 0; }
	void Del_Last_Min() { last_time[4] = 0; }
	void Del_Last_Sec() { last_time[5] = 0; }

};
```

###### \<non_member.h\>
```c++
#pragma once

#include <iostream>
#include <string>

using namespace std;

class n_member {

	string name, tel;
	int age;

public:

	n_member() {}
	n_member(string _name, string _tel, int _age) {
		name = _name;
		tel = _tel;
		age = _age;
	}
	n_member(const n_member& u) {
		name = u.name;
		tel = u.tel;
		age = u.age;
	}
	~n_member() {
		name.clear();
		tel.clear();
		age = 0;
	}

	virtual void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "Tel: " << tel << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	int GetAge() { return age; }

	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetAge(int _age) { age = _age; }
	
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelAge() { age = 0; }

};
```
