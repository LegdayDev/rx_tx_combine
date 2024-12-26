## audio_combine.py
`audio_combine.py`는 MP3 오디오 파일의 화자분리된 Rx, Tx 파일을 결합하는 기능을 제공하는 Python 기반의 프로그램입니다.

## 요구 사항
- **Python 3.10 이상**
- 내장 라이브러리 및 외부프로그램 :
  - `pydub`
  - `ffmpeg.exe`
  - `ffprobe.exe`
---
## 준비사항
- 가상환경에서 `conda install pydub` 명령어를 통해 `pydub` 패키지 사용
- `.mp3` 파일을 `pydub` 패키지로 읽을 경우 `ffmpeg` 프로그램이 필요하므로 아래 링크에서 2개의 `.exe` 실행파일을 프로젝트 루트경로에 둔다
  - [ffmpeg](http://naver.me/F2ZbIRA1)
- 화자분리된 RX,TX 음성파일은 알아서 준비해서 프로젝트 내 폴더에 넣어둔다.


## 코드 동작 설명
`audio_combine.py`는 다음과 같이 작동합니다:
1. 지정된 `.mp3` 파일들의 RX, TX 를 결합하여 새로운 음성파일인 `.wav` 파일로 저장한다.
---

