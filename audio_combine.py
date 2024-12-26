from pydub import AudioSegment
import os

# 현재 프로젝트 디렉터리를 가져옴
current_dir = os.getcwd()

# FFmpeg 및 FFprobe 경로 강제 설정 (프로젝트 폴더 내에 있는 경우)
AudioSegment.converter = os.path.join(current_dir, "ffmpeg.exe")
AudioSegment.ffprobe = os.path.join(current_dir, "ffprobe.exe")


# RX와 TX MP3 파일 경로 설정 (프로젝트 내)
# 예시) /audio_before/call_RX.mp3 라면 오디오파일경로는 audio_before 은 call_RX.mp3 이다.
rx_mp3_path = os.path.join(current_dir, "오디오파일경로", "파일명")
tx_mp3_path = os.path.join(current_dir, "오디오파일경로", "파일명")

# 결합된 WAV 파일 저장 경로
output_wav_path = os.path.join(current_dir, "파일저장소", "파일명.wav")

# 경로 확인
if not os.path.exists(rx_mp3_path):
    print(f"RX MP3 파일이 존재하지 않습니다: {rx_mp3_path}")

if not os.path.exists(tx_mp3_path):
    print(f"TX MP3 파일이 존재하지 않습니다: {tx_mp3_path}")

try:
    # RX 오디오 파일 읽기
    rx_audio = AudioSegment.from_file(rx_mp3_path, format="mp3")

    # TX 오디오 파일 읽기
    tx_audio = AudioSegment.from_file(tx_mp3_path, format="mp3")

    # RX+TX 합치기
    combined_audio = rx_audio.overlay(tx_audio)

    # 결합된 오디오를 WAV 형식으로 저장
    os.makedirs(os.path.dirname(output_wav_path), exist_ok=True)
    combined_audio.export(output_wav_path, format="wav")

    # 성공 출력문
    print(f"결합된 WAV 파일이 생성되었습니다: {output_wav_path}")

except FileNotFoundError as e:
    print("오류: 지정된 파일이나 디렉토리를 찾을 수 없습니다. 아래 항목을 확인해주세요.")
    print(f"1. RX MP3 경로: {rx_mp3_path}")
    print(f"2. TX MP3 경로: {tx_mp3_path}")
    print(str(e))

except Exception as e:
    print("오류가 발생했습니다:")
    print(str(e))
