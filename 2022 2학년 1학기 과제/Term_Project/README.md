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
#include "member.h"

using namespace std;

void Save_Members_Data(vector<member>& m) {

	ofstream outfile("Member_Data.txt", ios_base::out);

	for (int i = 0; i < m.size(); i++) {

		string buffer = m[i].GetName();
		buffer += " ";
		buffer += to_string(m[i].GetAge());
		buffer += " ";
		buffer += m[i].GetId();
		buffer += " ";
		buffer += m[i].GetPw();
		buffer += " ";
		buffer += m[i].GetTel();
		buffer += " ";
		buffer += m[i].GetEmail();
		buffer += " ";
		buffer += m[i].GetGrade();
		outfile << buffer << endl;

	}

}

int main() {

	vector<member> u;

	member u1("이름", "아이디", "비밀번호", "010-1234-5678", "이@메일.com", 25);

	u.push_back(u1);

	Save_Members_Data(u);

	return 0;

}
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

###### \<member.h\>
```c++
#pragma once

#include <iostream>
#include <string>
#include "non_member.h"

using namespace std;

class member {

	string name, id, pw, email, tel, grade;
	int age;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age, string _grade = "Bronze") {
		name = _name;
		tel = _tel;
		id = _id;
		pw = _pw;
		email = _email;
		age = _age;
		grade = _grade;
	}
	member(const member& u) {
		name = u.name;
		tel = u.tel;
		id = u.id;
		pw = u.pw;
		email = u.email;
		age = u.age;
		grade = u.grade;
	}
	~member() {
		name.clear();
		tel.clear();
		id.clear();
		pw.clear();
		email.clear();
		grade.clear();
		age = 0;
	}

	void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "ID: " << id << endl;
		cout << "PW: " << pw << endl;
		cout << "회원 등급: " << grade << endl;
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

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetGrade(string _grade) { grade = _grade; }
	void SetAge(int _age) { age = _age; }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelGrade() { grade.clear(); }
	void DelAge() { age = 0; }

};
```
