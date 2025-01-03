# 채용 전쟁: 로봇 회사가 찾는 인재는? 
![Roschool](https://github.com/user-attachments/assets/fcda667d-c755-4b03-a3ae-0891467e41fc)

## 프로젝트 소개
- **목차**
  - [프로젝트 목표](#프로젝트-목표)
  - [주제 선정 배경](#주제-선정-배경)
  - [구성원 및 역할](#구성원-및-역할)
  - [기술스택](#기술스택)
  - [DB](#db)
  - [Data 분석 및 시각화](#data-분석-및-시각화)
  - [결론](#결론)
 

## 프로젝트 목표  
- 로봇 SW 개발 직군의 채용 시장 동향을 파악하고, 데이터 기반의 인사이트를 제공하기 위해 사전 조사를 진행.
- 주요 채용 플랫폼(사람인, 잡코리아, 인크루트)을 통해 데이터 수집 가능성을 확인하고, 조사 범위 및 키워드를 선정.


## 주제 선정 배경
- **미래 산업의 핵심 분야로서의 성장성**
  - 로봇 기술은 4차 산업혁명의 핵심으로 자리 잡고 있으며, 제조, 물류, 의료, 농업 등 다양한 산업에서 빠르게 확산되고 있음.
  - 자율주행, 물류 로봇, 협동 로봇 등에서 소프트웨어 개발은 로봇의 성능을 결정짓는 중요한 역할을 하고 있어 채용 수요 지속 증가
![image](https://github.com/user-attachments/assets/1aed04c5-3016-41ec-bdfd-758c01e8216d)
  - 출처 : 글로벌 로봇산업 추이 전망/제공=KIAT(2023) 전기신문(https://www.electimes.com)

- **기술 발전에 따른 직군 전문성 요구**
  - 로봇 SW 개발은 ROS/ROS2, 자율주행 알고리즘, 모션 제어 등 고도화된 기술 역량을 요구하는 직군으로, 채용 공고에서 명확한 기술 스택과 경험을 요구하는 비율이 높아지고 있음.
  - 이러한 전문 기술을 보유한 인재를 채용하기 위한 시장 분석이 구직자와 기업 모두에게 중요한 정보이기 때문에 로봇시장 채용시장 데이터를 주제로 선정.

- **기존 채용 사이트와 정보 플랫폼 내 로봇 산업에 특화된 채용 정보나 요구 기술 분석의 어려움**

![Screenshot from 2024-12-31 13-39-31](https://github.com/user-attachments/assets/6997e06f-1790-4811-a7b5-9b46a79e6695)
![line](https://github.com/user-attachments/assets/9e53e135-aee1-4376-99ac-aca4bf49e287)
  - 출처 : 사람인 메인화면(https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1)


## 구성원 및 역할

🏫**ROSchool**🏫
| 이름       | 업무                                                         |
|------------|--------------------------------------------------------------|
| **심채훈** (팀장) | 프로젝트 총괄, 데이터 수집(사람인), 데이터 정제 및 분류      |
| **나덕윤**  | 데이터 수집(인크루트), 데이터 분석 및 시각화, DB 분류 |
| **이태민**  | 데이터 수집(잡코리아), 데이터 정제 및 분류, GitHub README |
| **박정배**  | 데이터 정제 및 분류, 데이터 분석 및 시각화, DB 관리, 발표 |
| **공통**  | 데이터 처리 기준 논의, 발표자료 준비, Confluence, Jira |

## 프로젝트 기간
***2024.12.27. ~ 2025.01.03. (1주)***

## Workflow
![ROSchool_jira](https://github.com/user-attachments/assets/e63385a8-6704-45f6-ae22-4624786680b4)

## 수집 데이터
| 사이트 | 데이터 | 기준 |
| --- | --- | --- |
| [사람인](https://www.saramin.co.kr/zf_user/) | 채용정보, 기업정보 | 2024.12.27. |
| [잡코리아](https://www.jobkorea.co.kr/) | 채용정보 | 2024.12.27. |
| [인크루트](https://www.incruit.com/) | 채용정보 | 2024.12.26. |

## 기술스택

|     |     |
| --- | --- |
| **OS** | <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=Ubuntu&logoColor=white"> |
| **개발툴** | <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white"> |
| **라이브러리** | <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white"> <img src="https://img.shields.io/badge/Beautifulsoup-008080?style=flat&logo=beautifulsoup&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"> <br/> <img src="https://img.shields.io/badge/numpy-013243?style=flat&logo=numpy&logoColor=white"> |
| **DB** | <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/amazonrds-527FFF?style=flat&logo=amazonrds&logoColor=white"> |
| **협업툴** | <img src="https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/Jira-0052CC?style=flat&logo=Jira&logoColor=white"> <img src="https://img.shields.io/badge/Confluence-172B4D?style=flat&logo=confluence&logoColor=white"> |


## DB

### ERD
![ERD](https://github.com/user-attachments/assets/6bf182a4-5461-4098-bc31-8f3615c441ff)


## Data 분석 및 시각화

### 로봇 기업 분석

- 지역별 기업 분포

  ![로봇 기업 지역분포](https://github.com/user-attachments/assets/ef73b88f-de4c-4418-b886-012c89016bf9)
  - 주로 수도권에 분포되어 있으며, 충청도 및 경남 지역 소수 위치

- 기업 규모 비율

  ![기업분류별 분포](https://github.com/user-attachments/assets/15c026d8-d679-4591-94ee-a66e540d5953)
  - 중소기업의 비율이 2/3 이상 차지하며 그 뒤로 스타트업, 강소기업의 비율이 높음
 
- 기업 규모별 사원수

  ![규모별 사원수](https://github.com/user-attachments/assets/89092d22-6a12-428c-9855-1d1f2a877abc)
  
- 업력별 매출액
  
  ![업력별 매출 히트맵(경신 X)](https://github.com/user-attachments/assets/6c71502a-6447-4eb8-9eac-63ba2d40697e)
  ![설립일별 평균매출 회귀선 스케터](https://github.com/user-attachments/assets/dd8bd56c-40a1-4dc2-b575-04decf52d0bd)
  - 20~30년 업력을 가진 기업의 매출액이 높게 형성 (단위: 억)

- 기업 규모별 연봉

  ![규모별 평균연봉 박스플롯](https://github.com/user-attachments/assets/fa6fb7a6-6047-4776-ad5d-fe963172ac03)
  - 스타트업, 중소기업, 중견기업은 5000-6000만, 대기업은 7000-8000만으로 형성

- 지역별 연봉

  ![지역별 연봉 수평플롯](https://github.com/user-attachments/assets/bcc39db1-1f5f-4d85-b481-0eb326a46d0b)
  - 4000-6000만이 주를 이르며 경기, 서울의 연봉이 높게 형성

### 채용 정보 분석

- 경력별 연봉

  ![경력별 평균연봉 박스플롯](https://github.com/user-attachments/assets/fee99190-6016-4fd6-954a-3573ab404c91)
  - 대체로 5000-7000만으로 형성되며, 최소 3000-4000만 연봉을 지급

- 기술스택 선호도(공통)

  ![기술 스택 막대그래프](https://github.com/user-attachments/assets/911c3e9b-6e72-4e39-95dd-3423d5797923)
  - C++, ROS, Python, C, Linux 순으로 선호

- 기술스택 선호도(자격요건)

  ![기술 필수사항 막대그래프](https://github.com/user-attachments/assets/fefa6155-a5ab-4921-bf10-4306461e27a5)
  - 자격 요건으로 C++, C, Python, C#, Linux를 선호

- 기술스택 선호도(우대사항)

  ![기술 우대사항 막대그래프](https://github.com/user-attachments/assets/40cb9fab-183d-4f6b-8169-ac230a4f5af6)
  - 우대사항으론 ROS, Linux, C++, Git, Embedded를 선호

- 업력별 기술스택 선호도 (자격요건)

  ![Screenshot from 2025-01-03 10-17-04](https://github.com/user-attachments/assets/938a2cd2-6ddb-4fcc-835f-70ffb2fb4add)
  ![Screenshot from 2025-01-03 10-17-18](https://github.com/user-attachments/assets/3c8e8e18-d3ee-42e2-8806-46b8ea743b6b)
  - 공통적으로 C 계열의 언어를 많이 요구

- 규모별 기술스택 선호도 (자격요건)

  ![Screenshot from 2025-01-03 10-17-04](https://github.com/user-attachments/assets/682f7cd2-922b-4bdc-a7ee-f08357179d3e)
  ![Screenshot from 2025-01-03 10-17-18](https://github.com/user-attachments/assets/1e1bd59b-6ab3-4379-9aa6-d4cac6c038c8)
  - 규모별 기술스택도 C 계열의 언어를 많이 요구
 
- 경력 선호도

  ![경력별 선호도 막대그래프](https://github.com/user-attachments/assets/daceca89-d09c-4ff4-b25c-a5a048970077)
  ![규모별 경력 선호도 파이차트-1](https://github.com/user-attachments/assets/310d2de2-959b-4bbb-8902-1a949e9ba62e)
  ![Screenshot from 2025-01-03 10-12-06-20250103-011206](https://github.com/user-attachments/assets/836b2a80-9fb0-47b3-9456-0feeaa7ffab6)
  - 경력 1-3년, 신입을 가장 선호
 
- 학력 선호도

  ![학력별 선호도 막대그래프](https://github.com/user-attachments/assets/c1359c92-5d91-48fa-bbb3-4f41b3cdd7c8)
  ![규모별 학력 선호도 파이차트-1](https://github.com/user-attachments/assets/93705df8-7ceb-4794-9ffb-1e7fda26c42a)
  ![규모별 학력 선호도 파이차트-2](https://github.com/user-attachments/assets/1775a1f3-805c-4343-96e9-316cf8e56a2c)
  - 스타트업은 초대졸이상의 비율이 높고, 대체로 대졸이상을 선호

## 결론

### 필수 기술 역량

- **C++**
  - 고성능 실시간 제어: C++는 로봇의 핵심 알고리즘과 제어 시스템 구축에 필수적
  - STL과 메모리 관리: 고급 개념 학습으로 효율적인 코드 작성 능력 향상
  - ROS 통합 프로젝트: 실제 로봇 시스템에 적용할 수 있는 실무 경험 축적
  - 최적화 기술: 멀티스레딩과 동시성 프로그래밍으로 성능을 극대화하는 기술 학습

- **Python과 ROS**
  - Python 역할: 데이터 분석, AI/ML 통합 시뮬레이션에 활용 Pandas, Matplotlib로 데이터를 시각화, PyTorch, TensorFlow로 AI 모델 구축
  - ROS의 중요성: ROS2 아키텍처와 통신프로토콜 응용, Gazebo, RViz로 **시뮬레이션 수행
 
- **임베디드 시스템**
  - MCU 프로그래밍: STM32, ESP32 등의 MCU를 활용해 로봇 하드웨어를 제어
  - ROS 활용: 실시간 운영 체제로 정확한 타이밍과 리소스 관리를 구현
  - 센서 및 액추에이터 인터페이스: 다양한 하드웨어 컴포넌트와의 효율적인 통신을 설계하고 테스트

### 취업전략

- **규모별 스타트업을 위한 역량 개발**
  - 빠른 프로젝트 진행 능력: 다양한 프로젝트 경험을 통해 신속한 개발 능력 향상
  - 다양한 기술 활용: C++, Python, ROS 여러 기술을 활용한 프로젝트로 포트폴리오 강화
  - 임베디드 시스템 경험: 임베디드 시스템 관련 프로젝트를 수행
 
- **규모별 중소 / 중견기업 취업 전략**
  - 실무 중심 역량: 안정서오가 실무 능력을 겸비한 인재로 성장
  - 핵심 기술 마스터: C++과 Python 중심으로 기술 역량 강화
  - ROS 프로젝트 경험: 실제 ROS 프로젝트 수행으로 실무 적용 능력 증명
  - 협업 능력 강조: 팀 프로젝트 경험을 통한 협업 스킬 향상
 
- **지역별 수도권 중심의 취업 활동**
  - 기업 집중도: 로봇 소프트웨어 개발 관련 기업과 채용 공고가 수도권에 집중
  - 네트워킹 기회: 다양한 협업 기회를 통해 기술과 경력을 확장
  - 취업 전략: 수도권 채용 공고와 박람회 정보 주시
  - 트렌트 파악: 주요 기업과 스타트업의 최신 프로젝트 동향 주시

- **지역별 비수도권 취업 가능성 탐색**
  - 지역 특성: 경남, 전남, 충북 등 제조 기반 기업들이 로봇 자동화를 도입하며 기술 수요가 증가
  - 경쟁 우위: 상대적으로 낮은 경쟁률과 장기적인 성장 가능성이 있음
  - 취업 전력: 지역 강소기업과 연구소 채용 공고를 주시하고, 지역 기반 지원 프로그램 활용
