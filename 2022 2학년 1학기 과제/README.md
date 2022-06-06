# 과제

###### 2022 2학년 1학기 C++프로그래밍 과제 모음


## 과제 1
#### 문제1. 길이가 10인 배열을 선언하고, 총 10개의 정수를 입력 받아서, 홀수와 짝수를 구분 지어서 출력하는 프로그램을 작성해 보자. 일단 홀수부터 출력하고 나서, 짝수를 출력하도록 하자. 단 10개의 정수는 main 함수 내에서 입력 받도록 하고, 배열을 인자로 받아서 배열 내에 존재하는 홀수만을 출력하는 함수와 짝수만을 출력하는 함수를 각각 정의해서 이 함수들을 호출하는 형식으로 프로그램을 작성하자.

```c++
#include <stdio.h>

int num[10]; // 정수를 저장하기위한 배열 선언
void odd(int n[]); // 홀수 출력 함수 선언
void even(int n[]); // 짝수 출력 함수 선언

int main() { 

	for (int i = 0; i < 10; i++) { // 10회 반복하여
		scanf_s("%d", &num[i]); // 배열에 정수를 하나씩 저장
	}

	odd(num); // 홀수만 출력
	even(num); // 짝수만 출력

	return 0;
}

void odd(int n[]) { // 홀수 출력 함수

	printf("홀수출력: "); // 홀수출력 안내문구 출력

	for (int i = 0; i < 10; i++) { // 배열의 크기인 10만큼 반복하여
		if (n[i] % 2 != 0) { // i번째 원소가 홀수라면
			printf("%d ", n[i]); // i번째 원소 출력
		}
	}

}
void even(int n[]) { // 짝수 출력 함수

	printf("\n짝수출력: "); // 짝수출력 안내문구 출력

	for (int i = 0; i < 10; i++) { // 배열의 크기인 10만큼 반복하여
		if (n[i] % 2 == 0) { // i번째 원소가 짝수라면
			printf("%d ", n[i]); // i번째 원소 출력
		}
	}

}
```

#### 문제2. 길이가 10인 배열을 선언하고, 총 10개의 정수를 입력 받는다. 단 입력받은 숫자가 홀수이면 배열의 앞에서부터 채워나가고, 짝수이면 뒤에서부터 채워나가는 형식을 취하기로 하자. 따라서 사용자가 [1,2,3,4,5,6,7,8,9,10]을 입력했다면, 배열에는 [1,3,5,7,9,10,8,6,4,2]의 순으로 저장이 될 것이다. 최종적인 배열의 결과값을 화면에 출력하자.

```c++
#include <stdio.h>

int num[10]; // 입력한 정수를 저장하기 위한 배열 선언
int even_cnt = 0; // 짝수의 개수를 카운트하기 위해 선언
int odd_cnt = 0; // 홀수의 개수를 카운트하기 위해 선언

int main() {

	for (int i = 0; i < 10; i++) { // 10회 반복하여

		int a;
		scanf_s("%d", &a); // 정수를 한 개씩 입력받는다

		if (a % 2 != 0) { // 만약 홀수라면

			num[odd_cnt] = a; // 앞에서부터 채우기 시작하고
			odd_cnt += 1; // 홀수의 개수를 1 증가시킨다.

		}
		else { // 홀수가 아닌 짝수라면

			num[9 - even_cnt] = a; // 맨 뒤에서부터 채우기 시작하고
			even_cnt += 1; // 짝수의 개수를 1 증가시킨다.

		}
	}

	for (int i = 0; i < 10; i++) { // 10회 반복하여
		printf("%d ", num[i]); // 배열의 원소를 하나씩 출력한다.
	}

	return 0;

}
```

## 과제2
#### 문제1. 문제에서 주어진 2차원 데이터 배열을(배열의 행과 열 정보도 같이) 메모장 등의 텍스트 편집기를 이용하여 임의의 이름으로 파일을 저장(예 test.txt)하고, File 입출력 함수를 통하여 test.txt에 저장되어 있는 배열 정보와 데이터를 정확하게 읽고 출력해 보는 프로그램을 작성한다. (동적으로 배열을 할당 시 2차원 배열을 1차원 배열로 할당해도 상관없음) 
#### 각 행의 평균과 전체 데이터의 최소값, 최대값을 계산하고, 출력하는 프로그램을 추가하여 프로그램을 완성한다.

```c++
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

	FILE* fp = fopen("test.txt", "r"); // test.txt를 읽기 형식으로 연다.

	int rc[2] = { 0, 0 }; // 행과 열을 저장할 1차원 정수형 배열을 선언한다.
	int a = 0; // 행과 열을 저장할 때 필요한 정수형 변수 선언
	int num = NULL; // test.txt에서 숫자를 불러와 저장할 때 사용할 정수형 변수 선언
	int r = 0; // test.txt에서 숫자를 불러와 저장할 때 몇 번째 행인지 판단하기 위한 정수형 변수 선언
	int c = 0; // test.txt에서 숫자를 불러와 저장할 때 몇 번째 열인지 판단하기 위한 정수형 변수 선언
	int max = -2147483648; // 최대값을 구하기 위한 정수형 변수를 선언
	int min = 2147483647; // 최소값을 구하기 위한 정수형 변수 선언
	float total = 0; // 평균값을 구하기 위한 실수형 변수 선언
	int **arr; // 동적할당을 위한 정수형 이중포인터 선언
	int pm = 1; // 양수 음수 판단을 위한 정수형 변수 선언

	while (true) {

		int ch = fgetc(fp); // fp에서 문자를 하나씩 읽어옴

		if (ch - 48 >= 0 && ch - 48 <= 9) { // 만약 읽어온 문자가 0~9 사이라면

			num *= 10; // num에 10을 곱한 뒤
			num += ch - 48; // 읽어온 문자를 더함

		}
		else { // 만약 읽어온 문자가 0~9 사이에 없다면 해당 숫자가 끝났다는 의미이므로

			if (num != NULL) { // num이 NULL이 아닐 때

				rc[a] = num; // num을 rc[a]저장
				num = NULL; // num 초기화
				a++; // a를 1 증가

			}

		}

		if (a == 2) break; // 행과 열을 전부 읽어왔다면 while문 종료

	}

	arr = (int**)malloc(sizeof(int*) * rc[0]); // 읽어온 행의 수를 이용하여 arr에 동적할당.

	for (int i = 0; i < rc[0]; i++) { // 읽어온 열의 수를 이용하여

		arr[i] = (int*)malloc(sizeof(int) * rc[1]); // 행의 수 만큼 동적할당한 arr에 인덱스 표기법을 이용하여 열의 수만큼 동적할당.

	}

	num = NULL; // num초기화

	while (true) {

		int ch = fgetc(fp); // fp에서 문자를 하나씩 읽어옴

		if (ch == 45) { // 만약 읽어온 문자가 45('-')라면
			pm = -1; // pm에 -1 저장
		}
		else {

			if (ch - 48 == 0 && num == NULL) { // 만약 읽어온 문자가 0이고 num변수가 비어있다면

				arr[r][c] = 0; // arr[r][c]에 num 저장
				num = NULL; // num초기화
				c++; // c를 1증가
				pm = 1; // pm 초기화

			}else if (ch - 48 >= 0 && ch - 48 <= 9) { // 읽어온 문자가 0~9 사이라면

				num *= 10; // num에 10을 곱한 뒤
				num += ch - 48; // 읽어온 문자를 더함

			}else { // 만약 읽어온 문자가 0~9 사이에 없다면 해당 숫자가 끝났다는 의미이므로

				if (num != NULL) { // num이 NULL이 아닐 때

					arr[r][c] = num * pm; // arr[r][c]에 num * pm을 저장
					num = NULL; // num초기화
					c++; // c를 1증가
					pm = 1; // pm초기화

				}

			}

			if (c >= rc[1]) { // 만약 c가 열의 수보다 크거나 같다면

				c = 0; // c를 0으로 초기화
				r += 1; // r을 1 증가

			}

		}

		if (r == rc[0]) break; // r이 행의 수보다 크거나 같다면 while 탈출

	}

	for (int i = 0; i < rc[0]; i++) {

		for (int j = 0; j < rc[1]; j++) {

			total = total + arr[i][j]; // 행의 숫자를 전부 더함
			min = min > arr[i][j] ? arr[i][j] : min; // 작은 수가 나올 때 마다 최소값 변수에 저장
			max = max < arr[i][j] ? arr[i][j] : max; // 큰 수가 나올 때 마다 최대값 변수에 저장

		}

		printf("line_%d_ave: %f\n", i + 1, total / float(rc[1])); // 한 행이 끝날 때 마다 그 행의 평균값 출력
		total = 0; // total 변수 초기화

	}

	printf("total_max: %d\n", max); // 전체의 최대값 출력
	printf("total_min: %d\n", min); // 전체의 최소값 출력

	return 0; // 프로그램 종료

}
```

#### 문제2
#### [1] lena.raw 파일은 lena 영상(256x256 영상)파일로 이 영상을 저장할 메모리를 동적으로 할당한다.
#### [2] lena 영상에 대한 산술연산(+,-)을 수행하는 두 함수를 구현해 보자.
###### 2.1 덧셈연산: Addition(unsigned char *, int value) 함수 / 각화소 밝기값+value
###### 2.2 뺄셈연산: Subtraction(unsigned char*, int value) 함수 / 각화소 밝기값-value
###### [참고사항 1] 파일에서 영상(Size_X*Size_Y) 읽고, 쓰기 
###### fread(InImage, sizeof(unsigned char), Size_X*Size_Y, infile);   영상 읽어오기
###### fwrite(InImage, sizeof(unsigned char), Size_X*Size_Y, outfile); 영상 출력하기
###### 영상 한 화소의 자료형은 unsigned char로 하세요. 한 화소의 밝기값은 0~255 까지의 밝기값을 가진다.

```c++
#define _CRT_SECURE_NO_WARNINGS // scanf 오류를 무시하기 위해 사용
#define X 256 // 가로 크기
#define Y 256 // 세로 크기
#include <stdio.h>
#include <stdlib.h>

void Addition(unsigned char *arr[X], int value) { // 밝기 증가 함수

	for (int i = 0; i < Y; i++)
	{
		for (int j = 0; j < X; j++)
		{
			arr[i][j] = arr[i][j] + value; // value 만큼 밝기 증가
			if (arr[i][j] > 255) arr[i][j] = 255; // 클리핑: 255보다 클 경우 255로 고정
		}

	}

}

void Subtraction(unsigned char *arr[X], int value) { // 밝기 감소 함수

	for (int i = 0; i < Y; i++)
	{
		for (int j = 0; j < X; j++)
		{
			arr[i][j] = arr[i][j] - value; // value 만큼 밝기 감소
			if (arr[i][j] < 0) arr[i][j] = 0; // 클리핑: 0보다 작을 경우 0으로 고정
		}

	}

}

int main()
{
	int num; // 증가 또는 감소 선택을 위한 정수형 변수 선언

	unsigned char **OrgImg = (unsigned char**)calloc(Y, sizeof(unsigned char*)); // raw파일의 세로 크기만큼 동적할당

	for (int i = 0; i < Y; i++)
	{
		OrgImg[i] = (unsigned char*)calloc(X, sizeof(unsigned char)); // raw파일의 가로 크기만큼 동적할당

	}

	FILE *infile = fopen("lena_256x256.raw", "rb"); // 이진파일로 열기

	// int a = fread(OrgImg, sizeof(unsigned char**), 256*256, infile);

	for (int i = 0; i < 256; i++) {

		for (int j = 0; j < 256; j++) {

			OrgImg[i][j] = fgetc(infile); // 파일의 내용을 하나씩 불러와서 OrgImg에 저장

		}

	}

	fclose(infile); // 파일 닫기

	printf("1. 밝기 증가\n2. 밝기 감소\n>> "); // 밝기를 증가할지 감소할지 결정하기 위한 안내문구 출력
	scanf("%d", &num); // 번호를 num 변수에 저장

	if (num == 1) // 만약 증가라면
	{
		
		int value; // 증가시킬 값을 저장할 value 선언
		
		printf("밝기 변화: "); // 변화 값을 입력하라는 안내문구 출력
		scanf("%d", &value); // value 입력

		Addition(OrgImg, value); // OrgImg와 value값을 함수에 전달

	}
	else if (num == 2) // 만약 감소라면
	{

		int value; // 감소시킬 값을 저장할 value 선언

		printf("밝기 변화: "); // 변화 값을 입력하라는 안내문구 출력
		scanf("%d", &value); // value 입력

		Subtraction(OrgImg, value); // OrgImg와 value값을 함수에 전달

	}
	else {
		return 0; // 그 외의 숫자가 입력되면 프로그램 종료
	}

	FILE* outfile = fopen("lena_256x256.raw", "wb"); // 이진파일을 쓰기형식으로 오픈

	for (int i = 0; i < 256; i++) {

		for (int j = 0; j < 256; j++) {

			fputc(OrgImg[i][j], outfile); // OrgImg의 값을 하나씩 파일에 입력

		}

	}

	fclose(outfile); // 파일 닫기

	return 0; // 프로그램 종료

}
```

## 과제3
#### 문제1. 다음은 어느 인터넷 사이트 사용자에 대한 정보이다. 이러한 사용자 정보를 표현할 수 있는 구조체를 정의하고, 초기화한 후, 모든 사용자 정보를 모니터에 출력하는 함수를 포함하는 프로그램을 작성해 보자. 초기화는 사용자 정보가 기록되어 있는 파일정보(user.txt)를 개방하여(open) 초기화하고, 사용자 전체를 출력하는 함수(PrnUser(..))의 매개변수는 포인터를 사용하여 출력하도록 하자.

###### user.txt 파일 내용은 차례대로

아이디     비밀번호     5개스테이지별 점수     마법 포인트   체력 포인트
---------------------------------------------------------
denzang    sd933k      80  56  72  86  91       300          10010
zzazang    !@sd487    100  98  100 100 91     20000         19000
gochuzang  df321#4     34  54  70  48  54       400           5000
---------------------------------------------------------

```c++
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct user_info { // 사용자 정보 저장을 위한 구조체 생성

    char id[50]; // 아이디
    char pw[50]; // 비밀번호
    int scores[5]; // 스테이지별 점수
    int magic_point; // 마법 포인트
    int health_point; // 체력 포인트

} ui;

void PrnUser(ui* users, int user_num); // 사용자 정보 출력 함수

int main() {

    char buffer[1000] = { 0 }; // 파일에서 읽어온 내용을 저장하기 위한 buffer 생성.
    int cnt = 0; // 라인수를 체크하기 위한 변수 생성
    int user_num = 0; // 사용자 수를 저장하기 위한 변수 생성
    FILE* fp = fopen("user.txt", "r"); // user.txt를 읽기모드로 open

    if (fp == NULL) { // 파일을 여는데 실패했다면
        printf("File Open Failed\n"); // 실패했다는 안내문구를 출력하고
        return 0; // 프로그램 종료
    }

    fread(buffer, 1000, 1, fp); // 파일 전체를 읽어와 buffer에 저장
    fclose(fp); // 파일 닫기

    // printf("buffer length: %d\n", strlen(buffer)); // buffer의 크기를 체크하기 위해 출력
    // printf("%s", buffer); // buffer의 내용을 체크하기 위해 출력

    for (int i = 0; i < strlen(buffer); i++) { // buffer의 길이만큼 반복하여
        if (buffer[i] == '\n') cnt++; // 만일 i번째 buffer가 줄바꿈 문자라면, cnt을 1 증가
    }

    if (buffer[strlen(buffer) - 1] == '\n') user_num = cnt - 3; // 만일 buffer의 마지막 문자가 줄바꿈문자라면 전체 cnt - 3이 user_num
    else user_num = cnt - 2; // 아니면 cnt - 2 가 user_num

    ui* users = (ui*)malloc(user_num * sizeof(ui)); // 사용자 수 만큼 ui 구조체 포인터를 동적할당
    char** lines = (char**)malloc((user_num + 1)* sizeof(char*)); // buffer에 저장되어있는 내용을 라인별로 나누어 저장하기 위해 user_num + 1만큼 동적할당

    for (int i = 0; i < user_num; i++) { // 각 line을 1024만큼 동적할당
        lines[i] = (char*)malloc(1024 * sizeof(char));
    }

    int a = 0; // 전체 라인수를 체크하기 위한 a 선언
    int b = 0; // 사용자 수를 체크하기 위한 b 선언

    char *str = strtok(buffer, "\n"); // buffer에서 줄바꿈 문자가 나오기 전까지 잘라서 str에 저장

    while (str != NULL) { // str이 안비어있으면 계속 반복하여
       if (b < user_num && a >= 2) { // 만약 b가 전체 사용자 수보다 작고 a가 2보다 크거나같다면
            // printf("\nwhile_line_%d: %s\n", b, str);
            strcpy(lines[b], str); // str의 내용이 사용자의 정보이기 때문에 lines[b]에 복사.
            b++; // b를 1 증가
        }
        else if (b > user_num) break; // 만일 b가 전체 사용자 수 보다 크다면 반복문 탈출
        str = strtok(NULL, "\n"); // str에 다음 줄바꿈 문자가 나올 때 까지 잘라서 저장
        a++; // a를 1 증가
    }

    for (int i = 0; i < user_num; i++) { // 사용자 수 만큼 반복하여
        strcpy(users[i].id, strtok(lines[i], " ")); // 아이디 복사
        strcpy(users[i].pw, strtok(NULL, " ")); // 비밀번호 복사
        for (int j = 0; j < 5; j++) users[i].scores[j] = atoi(strtok(NULL, " ")); // 5번 반복하여 스테이지별 점수 저장
        users[i].magic_point = atoi(strtok(NULL, " ")); // 마법 포인트 저장
        users[i].health_point = atoi(strtok(NULL, " ")); // 체력 포인트 저장

    }

    //for (int i = 0; i < user_num; i++) { // 각 라인의 내용을 라인 번호와 함께 출력
    //    printf("\n\nlies_line_%d: %s", i + 1, lines[i]);
    //}

    //printf("\n사용자 수 : % d\n\n", user_num); // 사용자의 수가 몇인지 확인하기 위해 출력

    PrnUser(users, user_num); // 사용자의 정보를 저장한 구조체포인터와 사용자의 수를 매개변수로 전달하여 사용자 정보 출력

    return 0; // 프로그램 종료

}

void PrnUser(ui* users, int user_num) {

    for (int i = 0; i < user_num; i++) { // 매개변수로 전달받은 사용자의 수 만큼 반복하여
        printf("\n<%d번째 사용자>\n", i + 1); // i+1번째 사용자의 정보를 출력한다는 안내문구 출력
        printf("아이디: %s\n비밀번호: %s\n", users[i].id, users[i].pw); // i+1번째 사용자의 아이디와 비밀번호 출력
        for (int j = 0; j < 5; j++) { // i+1번째 사용자의 1~5 스테이지별 점수 출력
            printf("%d 스테이지 점수: %d점\n", j + 1, users[i].scores[j]);
        }
        printf("마법 포인트: %d\n체력 포인트: %d\n", users[i].magic_point, users[i].health_point); // i+1번째 사용자의 마법포인트와 체력포인트 출력
    }

}
```

#### 문제2. 문자열을 인자로 받는 함수가 있다. 이 함수에서는 이 문자열의 내용을 뒤집은 문자열을 새로 만들어서 반환하는데, 이때 동적메모리를 할당해서 뒤집은 문자열을 저장한 후 반환하도록 다음 프로그램을 완성해 보자.

###### <주어진 코드>
```c++
#include <stdio.h>
#include <stdlib.h>

char* ReverseString(const char* src, int len); // 문자열을 뒤집는 함수

int main()
{
     char source[] = "InternetMedia Engineering";
     char* result = ReverseString(source, strlen(source));
     
     printf(“원본 문자열 : %s \n”, source);
     printf(“변경된 문자열 : %s \n”, result);
     
     free(result);

     return 0;
}

char * ReverseString(const char* src, int len)
{
   ....
}

```

```c++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* ReverseString(const char* src, int len); // 문자열을 뒤집는 함수

int main() {

    char source[] = "InternetMedia Engineering"; // 초기의 문자열 선언
    char* result = ReverseString(source, strlen(source)); // 결과 문자열 선언

    printf("원본 문자열 : %s \n", source); // 원본 문자열 출력
    printf("변경된 문자열 : %s \n", result); // 결과 문자열 출력

    free(result); // 할당 해제

    return 0; // 프로그램 종료

}

char* ReverseString(const char* src, int len){

    char* str = (char*)calloc(len + 1, sizeof(char)); // 문자열의 길이+1 만큼 동적할당

    for (int i = 0; i < len; i++) { // 문자열의 길이만큼 반복하여

        str[i] = src[len - 1 – i]; // 동적할당한 문자열 변수에 거꾸로 저장

    }

    return str; // 거꾸로 저장한 문자열 반환

}
```

## 과제4
#### 문제1. 다음 main 함수에서 필요로 하는 swap 함수를 함수 오버로딩조건을 만족하도록 구현해보자.
###### main

```c++
  int main() 
{ 
   int num1 = 20, num2 = 30; 
   swap(&num1, &num2); 
   std::cout << num1 << ' ' << num2 <<std::endl; 
   
   char ch1 = 'a',  ch2 = 'z' ; 
   swap(&ch1, &ch2); 
   std::cout << ch1 << ' ' << ch2 <<std::endl; 
   
   double db1 = 1.111,  db2 = '5.555' ; 
   swap(&db1, &db2); 
   std::cout << db1 << ' ' << db2 <<std::endl; 
   
   return 0; 
} 

```

```c++
#include <iostream>

using namespace std; // std namespace를 사용한다고 선언

void swap(int* a, int* b) { // 정수형 변수를 swap 하는 함수 선언 (오버로딩)

	int temp = *a;
	*a = *b;
	*b = temp;

}
void swap(char* a, char* b) { // 문자 변수를 swap 하는 함수 선언 (오버로딩)

	char temp = *a;
	*a = *b;
	*b = temp;

}
void swap(double* a, double* b) { // double 변수를 swap 하는 함수 선언 (오버로딩)

	double temp = *a;
	*a = *b;
	*b = temp;

}

int main() {

	int num1 = 20; // num1에 20 저장
	int num2 = 30; // num2 에 30 저장

	swap(&num1, &num2); // swap함수로 두 변수의 값 변경
	cout << num1 << ' ' << num2 << endl; // swap한 값 출력

	char ch1 = 'a'; // ch1에 'a' 저장
	char ch2 = 'z'; // ch2에 'b' 저장

	swap(&ch1, &ch2); // swap함수로 두 변수의 값 변경
	cout << ch1 << ' ' << ch2 << endl; // swap한 값 출력

	double db1 = 1.111; // db1에 1.111 저장
	double db2 = 5.555; // db2에 5.555 저장

	swap(&db1, &db2); // swap함수로 두 변수의 값 변경
	cout << db1 << ' ' << db2 << endl; // swap한 값 출력

	return 0; // 프로그램 종료

}
```

#### 문제2. 함수가 호출될 때 사용되는 두 개의 매개변수 중에서 작은 값을 반환하는 min(..)이라는 함수를 구현해보자. min() 함수가 매개변수로서 int 형 정수, float형, double 형 실수를 가질 수 있도록 함수를 오버로딩하고 그 예를 보이는 프로그램을 작성하자. 

```c++
#include <iostream>

using namespace std; // std namespace를 사용한다고 선언

int min(int a, int b) { // 두 정수 중 더 작은 값을 리턴하는 함수선언

	return a < b ? a : b;

}

float min(float a, float b) { // 두 float 중 더 작은 값을 리턴하는 함수 선언
	
	return a < b ? a : b;

}

double min(double a, double b) { // 두 double 중 더 작은 값을 리턴하는 함수 선언

	return a < b ? a : b;

}

int main() {

	int i1, i2; // 두 int형 변수를 저장할 i1, i2를 선언
	float f1, f2; // 두 float형 변수를 저장할 f1, f2를 선언
	double d1, d2; // 두 double형 변수를 저장할 d1, d2를 선언

	cout << "\n두 int형 변수를 입력하시오.\n>> "; // 두 int형 변수를 입력하라는 안내문구 출력
	cin >> i1 >> i2; // 두 int형 변수 입력
	cout << "두 int 중 가장 작은 값: " << min(i1, i2) << endl; // min함수를 통해 더 작은 수 출력

	cout << "\n두 float형 변수를 입력하시오.\n>> "; // 두 float형 변수를 입력하라는 안내문구 출력
	cin >> f1 >> f2; // 두 float형 변수 입력
	cout << "두 float 중 가장 작은 값: " << min(f1, f2) << endl; // min함수를 통해 더 작은 수 출력

	cout << "\n두 double형 변수를 입력하시오.\n>> "; // 두 double형 변수를 입력하라는 안내문구 출력
	cin >> d1 >> d2; // 두 double형 변수 입력
	cout << "두 double 중 가장 작은 값: " << min(d1, d2) << endl; // min함수를 통해 더 작은 수 출력

	return 0; // 프로그램 종료

}
```

#### 문제3. 정수 매개변수의 부호를 바꾸는 함수 neg(..)를 작성해보자. 포인터 매개변수를 사용해서, 그리고 레퍼런스 매개변수를 사용해서 두가지 버전의 함수를 작성해보자. 2가지 함수에 대한 동작하는 것을 보여주는 간단한 프로그램을 작성해서 그 동작내용을 보여주세요.

```c++
#include <iostream>

using namespace std; // std namespace를 사용한다고 선언

int neg(int* a) { // 포인터 매개변수를 사용한 정수 부호 변환 함수 선언

	return (-1) * (*a);

}

int neg(int& a) { // 레퍼런스 매개변수를 사용한 정수 부호 변환 함수 선언

	return (-1) * a;

}

int main() {

	int a; // 정수형 변수 a 선언
	int* a_p = &a; // a의 포인터 변수 선언
	int& a_r = a; // a이 레퍼런스 변수 선언

	cin >> a; // 정수 입력

	cout << "포인터 매개변수: " << neg(*a_p) << endl; // 포인터 매개변수를 사용한 neg함수 리턴값 출력
	cout << "레퍼런스 매개변수: " << neg(&a_r) << endl; // 레퍼런스 매개변수를 사용한 neg함수 리턴값 출력

	return 0; // 프로그램 종료

}
```

## 과제5
#### 문제1. 직사각형을 나타내는 Rectangle 클래스와 원을 나타내는 Circle 클래스를 디자인 해 보자. 이 두 클래스는 넓이를 구하는 기능과 둘레를 구하는 기능(함수)을 가지고 있다. 다음에 제공되는 main 함수와 출력결과를 통해서 요구되는 Rectangle 클래스와 Circle 클래스를 디자인해 전체 프로그램을 완성해 보자. 
###### main
```c++
int main(void) 
{ 
  Rectangle rec(3, 4);  초기화로 Rectangle rec(가로(cm), 세로(cm)) 
  cout << "면적: “ << rec.GetArea() << endl; 
  cout << "둘레: “ << rec.GetRound() << endl; 

  Circle ring(5);  초기화로 Circle ring(원의 반지름 길이(cm)) 
  cout << "면적: “ << ring.GetArea() << endl; 
  cout << "둘레: “ << ring.GetRound() << endl; 

  return 0; 
} 
```

```c++
#include <iostream>

using namespace std;

class Rectangle { // Rectangle 클래스 정의

	int w, h; // private 변수 w, h를 정수형으로 선언

public:

	Rectangle(int a, int b) { // Rectangle(a, b)로 w, h를 입력할 수 있도록 함수 선언

		w = a;
		h = b;

	}

	int GetArea() { // 직사각형의 면적을 리턴하는 함수 정의

		return w * h;

	}

	int GetRound() { // 직사각형의 둘레를 리턴하는 함수 정의

		return w * 2 + h * 2;

	}

};

class Circle { // Circle 클래스 정의

	double r; // 반지름을 저장할 r 을 double로 선언

public:

	Circle(int a) { // Circle(r)로 반지름의 길이를 입력할 수 있도록 함수 선언

		r = a;

	}

	double GetArea() { // 원의 면적을 리턴하는 함수 정의

		return r * r * 3.14;

	}

	double GetRound() { // 원의 둘레를 리턴하는 함수 정의

		return 2 * r * 3.14;

	}

};

int main(void)
{
	Rectangle rec(3, 4); // 직사각형의 가로, 세로 길이를 3, 4로 선언
	cout << "면적: " << rec.GetArea() << endl; // 직사각형의 면적 출력
	cout << "둘레: " << rec.GetRound() << endl; // 직사각형의 둘레 출력

	Circle ring(5); // 원의 반지름을 5로 선언
	cout << "면적: " << ring.GetArea() << endl; // 원의 면적 출력
	cout << "둘레: " << ring.GetRound() << endl; // 원의 둘레 출력

	return 0;
}
```

#### 문제2. 다음에 해당하는 프로그램을 순차적으로 완성해보자. 2차원 평면의 좌표를 위한 Point 클래스를 정의하자(수업시간에 사용한 클래스 수정해서 사용가능). Point 클래스에 대한 멤버변수와 멤버함수는 다음과 같다.

###### 멤버변수: x, y (2차원 평면의 한 점의 좌표)
###### SetX, SetY 함수: 멤버변수 좌표 값 x, y를 설정하는 함수
###### GetX 함수, GetY 함수: 좌표 값 x, y 를 각각 리턴하는 함수 
###### ShowData 함수: 객체의 모든 정보를 화면에 출력해 주는 함수
###### double Distance(Point &p1) 함수: 자기 자신의 Point 객체와 전달된 Point 객체 사이의 거리를 리턴 하는 함수. 두 점간의 거리(d)는 다음과 같다.



###### GetArea 함수: 0를 리턴한다. 
###### GetVolume 함수: 0을 리턴한다. 
###### GetName 함수: “Point" 문자를 리턴하는 함수.   

###### 위와 같은 Point 클래스를 이용하여, 정의된 멤버함수의 사용 예를 보이고, 두 객체간의 거리를 계산하여 출력하는 프로그램을 완성해보자. 이 때 두 점은 Point p1(1,2), p2(7,8)의 거리를 계산하여 출력하자.

```c++
#include <iostream>
#include <math.h> // 제곱근 계산을 위해 include

using namespace std;

class Point { // Point 클래스 선언

	int x, y; // private 변수 x, y를 정수형으로 선언

public:

	void SetX(int a) { // x좌표를 설정하는 함수 정의
		x = a;
	}
	void SetY(int b) { // y좌표를 설정하는 함수 정의
		y = b;
	}
	int GetX() { // x좌표의 값을 리턴하는 함수 정의
		return x;
	}
	int GetY() { // y좌표의 값을 리턴하는 함수 정의
		return y;
	}
	void ShowData() { // x, y좌표의 값을 출력하는 함수 정의
		cout << "(x, y): (" << x << ", " << y << ")\n";
	}
	double Distance(Point& p1) { // 또 다른 점을 매개변수로 하는 함수 선언
		return sqrt((x - p1.GetX()) * (x - p1.GetX()) + (y - p1.GetY()) * (y - p1.GetY())); // 현재의 점과 또 다른 점 사이의 거리를 계산하여 리턴
	}
	int GetArea() { // 면적을 리턴하는 함수 정의
		return 0;
	}
	int GetVolume() { // 부피를 리턴하는 함수 정의
		return 0;
	}
	string GetName() { // "Point"를 리턴하는 함수 정의
		string name = "Point";
		return name;
	}

};

int main(void)
{

	Point p1, p2; // Point 변수 p1, p2선언

	p1.SetX(1); // p1의 x좌표를 1로 설정
	p1.SetY(2); // p1의 y좌표를 2로 설정

	p2.SetX(7); // p2의 x좌표를 7로 설정
	p2.SetY(8); // p2의 y좌표를 8로 설정

	cout << "<GetX() & GetY() 사용 결과>\n"; // GetX(), GetY 함수 사용 결과
	cout << "p1 좌표: (" << p1.GetX() << ", " << p1.GetY() << ")\n";
	cout << "p2 좌표: (" << p2.GetX() << ", " << p2.GetY() << ")\n\n";
	
	cout << "<ShowData() 사용 결과>\n"; // ShowData() 함수 사용 결과
	p1.ShowData();
	p2.ShowData();
	cout << "\n";

	cout << "<Distance(Point &p1) 사용 결과>\n"; // Distance 함수 사용 결과
	cout << "Distance : " << p1.Distance(p2) << "\n\n";

	cout << "<GetArea() 사용 결과>\n"; // GetArea() 함수 사용 결과
	cout << "p1 Area : " << p1.GetArea() << "\n";
	cout << "p2 Area : " << p2.GetArea() << "\n\n";

	cout << "<GetVolume 사용 결과>\n"; // GetVolume() 함수 사용 결과
	cout << "p1 Volume : " << p1.GetVolume() << "\n";
	cout << "p2 Volume : " << p2.GetVolume() << "\n\n";

	string name1 = p1.GetName(); // GetName 함수 사용
	string name2 = p2.GetName(); // GetName 함수 사용

	cout << "<GetName() 사용 결과>\n"; // GetName() 함수 사용
	cout << "p1.GetName(): " << name1 << "\n";
	cout << "p2.GetName(): " << name2 << "\n\n";
	
	return 0;
}
```


















