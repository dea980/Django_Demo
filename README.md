# SimpleApp 실행 가이드

## 시스템 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

## 설치 및 실행 방법

1. 가상환경 생성 및 활성화
```bash
python -m venv venv
# Windows의 경우
venv\Scripts\activate
# macOS/Linux의 경우
source venv/bin/activate
```

2. 필요한 패키지 설치
```bash
pip install django
```

3. 데이터베이스 마이그레이션
```bash
cd SimpleApp
python manage.py migrate
```

4. 관리자 계정 생성 (선택사항)
```bash
python manage.py createsuperuser
```

5. 개발 서버 실행
```bash
python manage.py runserver
```

서버가 실행되면 브라우저에서 다음 주소로 접속할 수 있습니다:
- 메인 페이지: http://127.0.0.1:8000
- 관리자 페이지: http://127.0.0.1:8000/admin

## 주요 기능
- 스케줄러: 일정 관리 및 상태 추적
- 채팅: 실시간 메시지 교환

# SimpleApp API Documentation

## API 엔드포인트 목록

### 스케줄러 API (Scheduler API)

#### 1. 스케줄 목록 조회
- **URL**: `/`
- **Method**: GET
- **Description**: 모든 스케줄을 날짜와 시간순으로 정렬하여 조회
- **Authentication**: 로그인 필요
- **Response**: 스케줄 목록을 HTML 형식으로 반환

#### 2. 스케줄 생성
- **URL**: `/create/`
- **Method**: POST
- **Description**: 새로운 스케줄 생성
- **Authentication**: 로그인 필요
- **Request Body**:
  ```json
  {
    "title": "스케줄 제목",
    "description": "스케줄 설명",
    "date": "YYYY-MM-DD",
    "time": "HH:MM"
  }
  ```
- **Response**: 성공 시 스케줄 목록 페이지로 리다이렉트

#### 3. 스케줄 수정
- **URL**: `/edit/<int:pk>/`
- **Method**: POST
- **Description**: 기존 스케줄 정보 수정
- **Authentication**: 로그인 필요
- **Parameters**: 
  - pk: 스케줄 ID
- **Request Body**:
  ```json
  {
    "title": "수정된 제목",
    "description": "수정된 설명",
    "date": "YYYY-MM-DD",
    "time": "HH:MM",
    "status": "pending/completed/cancelled"
  }
  ```
- **Response**: 성공 시 스케줄 목록 페이지로 리다이렉트

#### 4. 스케줄 삭제
- **URL**: `/delete/<int:pk>/`
- **Method**: POST
- **Description**: 스케줄 삭제
- **Authentication**: 로그인 필요
- **Parameters**: 
  - pk: 스케줄 ID
- **Response**: 성공 시 스케줄 목록 페이지로 리다이렉트

#### 5. 스케줄 상태 토글
- **URL**: `/toggle-status/<int:pk>/`
- **Method**: GET
- **Description**: 스케줄 상태를 pending ↔ completed 간 전환
- **Authentication**: 로그인 필요
- **Parameters**: 
  - pk: 스케줄 ID
- **Response**: 스케줄 목록 페이지로 리다이렉트

### 메시지 채팅 API (Message Chat API)

#### 1. 채팅방 접속
- **URL**: `/chat/`
- **Method**: GET
- **Description**: 기본 채팅방 페이지 접속
- **Response**: 채팅방 HTML 페이지 반환

#### 2. 특정 채팅방 접속
- **URL**: `/chat/<str:room_name>/`
- **Method**: GET
- **Description**: 특정 이름의 채팅방 접속
- **Parameters**:
  - room_name: 채팅방 이름
- **Response**: 채팅방 HTML 페이지 반환

#### 3. 메시지 전송
- **URL**: `/send-message/`
- **Method**: POST
- **Description**: 채팅 메시지 전송
- **Request Body**:
  ```json
  {
    "message": "메시지 내용",
    "room_name": "채팅방 이름"
  }
  ```
- **Response**: 성공/실패 상태 반환

#### 4. 전체 메시지 조회
- **URL**: `/get-messages/`
- **Method**: GET
- **Description**: 모든 채팅 메시지 조회
- **Response**: 메시지 목록 반환

#### 5. 특정 채팅방 메시지 조회
- **URL**: `/get-messages/<str:room_name>/`
- **Method**: GET
- **Description**: 특정 채팅방의 메시지만 조회
- **Parameters**:
  - room_name: 채팅방 이름
- **Response**: 해당 채팅방의 메시지 목록 반환

## 인증 요구사항

- 스케줄러 API의 모든 엔드포인트는 로그인이 필요합니다.
- 채팅 API는 별도의 인증 없이 사용 가능합니다.

## 에러 처리

- 모든 API는 적절한 에러 메시지와 함께 실패 상태를 반환합니다.
- 스케줄러 API는 실패 시 에러 메시지를 포함한 페이지로 리다이렉트됩니다.
- 채팅 API는 실패 시 에러 상태와 메시지를 JSON 형식으로 반환합니다.
