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
