캡스톤 프로젝트: Mozik
본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.

본 프로젝트는 KT Cloud 환경에서 배포될 예정이었으나, 시연 편의를 위해 Docker 환경을 기반으로 README를 작성하였습니다.

1. 작품 주제 (Subject)
제목: Mozik

요약: 파일을 업로드하여 사진이나 동영상 모자이크 처리

2. 실용적 근거 (Rationale)
문제: 동영상이나 사진 내의 사람들의 초상권이나 개인정보가 침해될 수 있는 위험이 존재합니다.

근거 (수치/설명/사례):

어느 유명인의 유튜브 영상에서 무단 촬영된 사람들의 모습이 그대로 노출되는 문제

법률 관련 자료 또는 교육 자료 등으로 사용된 동영상 내 개인 식별 정보 처리 필요성

기대 가치: 수동으로 모자이크 처리하는 시간 절약 및 개인정보 보호 강화.

3. 핵심 기능 (Features)
기능 1: 동영상 모자이크 처리

기능 2: 원하는 사람을 지정해서 해당 인물만 모자이크 해제 (선택적 모자이크 해제)

기능 3: 빠른 업로드 및 처리 속도

4. 구현 환경 (Environment)
구분항목Front-End (프론트엔드)HTML, CSS, Flask (템플릿 엔진)Back-End (백엔드)Flask, Yolo, OpenCV tensorFlow mediapipe ffmpeg pytorch (런타임)KT Cloud (또는 Local Docker 환경)Deploy (배포)KT Cloud (최종), Flask 환경 (개발/시연)5. 팀원 구성 및 역할 (Team)이름,역할 최정환 프론트엔드 개발 (UI/UX 구현) 김하민발표 자료 및 문서 제작 (PPT 제작) 이소빈 백엔드 개발 (API 설계 및 구현)6. 실행 방법 6.1. 가상 환경 (데비안 서버 사용)프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 서비스를 실행합니다 sudo systemctl start nginx, sudo systemctl mozik

6. 실행 방법 (Run)
6.1. 가상 환경 (KT Cloud 사용)
프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 서비스를 실행합니다
sudo systemctl start nginx, sudo systemctl mozik

6.2. 접속서비스가 성공적으로 배포되면 웹 브라우저를 통해 접속합니다.http://211.253.27.46 < 프로젝트에 맞는 포트 또는 배포된  IP >
