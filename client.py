import socket
import pyaudio

# 音频参数
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

# 服务端设置
PORT = 12345

# 播放设备匹配关键词（可根据需要修改，例如 'Speakers'）
DEVICE_KEYWORD = "扬声器"

# 初始化 PyAudio
pa = pyaudio.PyAudio()

# 打印全部播放设备信息
print("🎧 可用播放设备列表：")
default_index = pa.get_default_output_device_info()["index"]
selected_index = None

for i in range(pa.get_device_count()):
    info = pa.get_device_info_by_index(i)
    if info["maxOutputChannels"] > 0:
        is_default = "(默认)" if i == default_index else ""
        print(f"  [{i}] {info['name']} {is_default}")
        if DEVICE_KEYWORD in info["name"] and selected_index is None:
            selected_index = i

# 选择播放设备
if selected_index is not None:
    print(f"\n✅ 选择匹配到的播放设备: [{selected_index}] {pa.get_device_info_by_index(selected_index)['name']}")
else:
    selected_index = default_index
    print(f"\n⚠️ 未匹配到关键词“{DEVICE_KEYWORD}”，使用默认设备: [{default_index}]")

# 初始化UDP接收
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))
sock.settimeout(5)

# 初始化播放流
try:
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                     output=True, frames_per_buffer=CHUNK,
                     output_device_index=selected_index)
except Exception as e:
    print(f"❌ 无法打开音频设备 [{selected_index}]: {e}")
    exit(1)

print(f"\n🔊 Listening on UDP port {PORT}...")

# 主循环
while True:
    try:
        data, _ = sock.recvfrom(4096)
        stream.write(data)
    except socket.timeout:
        print("⏳ Waiting for server...")
