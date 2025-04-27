import socket
import pyaudio

# 音频参数
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

# 服务端设置
PORT = 12345

# 初始化UDP接收
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))  # 监听所有网卡
sock.settimeout(5)

# 初始化播放输出
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                 output=True, frames_per_buffer=CHUNK)

print(f"Listening on UDP port {PORT}...")

while True:
    try:
        data, _ = sock.recvfrom(4096)
        stream.write(data)
    except socket.timeout:
        print("Waiting for server...")
