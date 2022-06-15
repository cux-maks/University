뭉치 PC 관리 프로그램

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
#include <iostream>
#include <fstream>
#include <vector>
#include <Windows.h>
#include <sstream>
#include "member.h"
#include "non_member.h"

#define admin_id "mc_admin"
#define admin_pw "mc_716_admin"

using namespace std;


void Delete_Save_Data();
void Read_Save_Data(vector<member>& m);
void Save_Members_Data(vector<member>& m);
vector<string> split(string str, char Delimiter);
member new_Member();
n_member new_Non_Member();

int main() {

	vector<member> u;
	vector<n_member> n_u;

	Read_Save_Data(u);

	string id_input, pw_input;
	bool admin_login = 0;
	bool login = 0;
	int login_cnt = 0;
	int state = 0;

home:

	cout << "---------- ΩOhm PC ----------" << endl;
	cout << "1. 로그인" << endl;
	cout << "2. 회원가입" << endl;
	cout << "3. 비회원 이용" << endl;
	cout << "4. 프로그램 종료" << endl;
	cout << ">> ";
	cin >> state;

	if (state == 1) {

		do {

			system("cls");

			cout << "---------- ΩOhm PC Login ----------" << endl;
			cout << "ID: ";
			cin >> id_input;
			cout << "PW: ";
			cin >> pw_input;

			if (id_input == admin_id && pw_input == admin_pw) {
				cout << "관리자 로그인 성공." << endl;
				login = 1;
				admin_login = 1;
			}
			else {

				if (u.size() == 0) {

					cout << "로그인 실패." << endl;
					login_cnt += 1;
					Sleep(1000);
					system("cls");

				}
				else {

					for (int i = 0; i < u.size(); i++) {

						if (id_input == u[i].GetId() && pw_input == u[i].GetPw()) {

							cout << "로그인 성공." << endl;
							login = 1;

						}
						else if (i == u.size()) {

							cout << "로그인 실패." << endl;
							login_cnt += 1;
							Sleep(1000);
							system("cls");

						}

					}

				}

			}

			if (login_cnt == 5) {

				cout << "로그인 5회 실패." << endl;
				cout << "프로그램을 종료합니다." << endl;
				Sleep(500);
				return 0;

			}

		} while (login == 0);
	}
	else if (state == 2) {

		u.push_back(new_Member());
		Save_Members_Data(u);
		system("cls");
		goto home;

	}
	else if (state == 3) {

		n_u.push_back(new_Non_Member());

	}
	else if (state == 4) {

		cout << "프로그램을 종료합니다." << endl;
		return 0;

	}
	else {

		cout << "해당 선택지는 존재하지 않습니다." << endl;
		Sleep(500);
		system("cls");
		goto home;

	}

	system("cls");

	login_cnt = 0;

	if (admin_login == 1) {

		cout << "---------- ΩOhm PC 관리 프로그램 ----------" << endl;

	}
	else if (state == 3) {

		cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;
		cout << "※비회원 이용자는 음식 주문 및 제자리 결제, 자리 이동 및 외출 또는 예약기능, 카운터 문의(메신저) 기능을 사용하실 수 없습니다." << endl;

	}
	else if(state == 1) {

			cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;

	}

	return 0;

}

void Read_Save_Data(vector<member>& m) {

	ifstream readData("Member_Data.txt");

	if (readData.is_open()) {

		string first_line;
		getline(readData, first_line);
		int n = stoi(first_line);

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

				member temp(name, id, pw, tel, email, age, grade, point);
				
				m.push_back(temp);

			}

		}
		else {

			cout << "There is no data." << endl;

		}

	}
	else {
		
		cout << "File open error" << endl;

	}

}

void Delete_Save_Data() {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << "Warning, Clear." << endl;

}

void Save_Members_Data(vector<member>& m) {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << m.size() << endl;

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
```

###### \<member.h\>
```c++
#pragma once

#include <iostream>
#include <string>

using namespace std;

class member {

	string name, id, pw, email, tel, grade;
	int age, point;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age, string _grade = "Bronze", int _point = 0) {
		name = _name;
		tel = _tel;
		id = _id;
		pw = _pw;
		email = _email;
		age = _age;
		grade = _grade;
		point = _point;
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
	}
	~member() {
		name.clear();
		tel.clear();
		id.clear();
		pw.clear();
		email.clear();
		grade.clear();
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

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetGrade(string _grade) { grade = _grade; }
	void SetAge(int _age) { age = _age; }
	void SetPoint(int _point) { point = _point; }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelGrade() { grade.clear(); }
	void DelAge() { age = 0; }
	void DelPoint() { point = 0; }

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
