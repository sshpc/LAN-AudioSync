# 局域网电脑声音分享到另一台电脑并实时同步播放

## 介绍
* 基于pyaudio 
* 局域网UDP广播实现音频传输,支持多接收端

### 原理图
```scss
[播放器] → [CABLE Input] → (1) → 网络 → 接收端播放  
                            ↘ (2) → 监听 → 本机扬声器播放
```

## 安装

### 接收端&客户端
1. 克隆仓库
2. 安装Python环境 3.0 + (https://www.python.org/downloads/) （记得勾选添加系统环境变量）

3. 执行 install.bat
4. 执行 runclient.bat

### 发送端&服务端
1. 克隆仓库
2. 安装Python环境 3.0 + (https://www.python.org/downloads/) （记得勾选添加系统环境变量）

3. 安装 VB-Audio 虚拟音频线。解压VBCABLE_Driver_Pack45.zip 安装驱动
4. 在window声音里配置监听（控制面板->声音）将CABLE Input 设备设置为默认通信设备,然后转到录制栏打开CABLE Output属性,找到侦听勾选并选择扬声器
5. 在 server.py 里配置广播地址（假如你的ip段192.168.0.0 255.255.255.0  则广播地址是192.168.0.255）
6. 执行 install.bat
7. 执行 runserver.bat




