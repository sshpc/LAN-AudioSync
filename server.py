import socket
import pyaudio

# 音频参数
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

# 网络参数
BROADCAST_IP = 'x.x.x.x'  # 修改为你局域网的广播地址
PORT = 12345

# 初始化音频输入
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                 input=True, frames_per_buffer=CHUNK)

# 初始化UDP广播
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"Broadcasting audio to {BROADCAST_IP}:{PORT}...")

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    sock.sendto(data, (BROADCAST_IP, PORT))
