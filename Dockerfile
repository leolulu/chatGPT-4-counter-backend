# 使用官方的 Python 3.11 image 作为基础 image
FROM python:3.11

# 设置工作目录为 /app
WORKDIR /app

# 把当前目录下的所有文件和文件夹复制到 /app 下
COPY . /app

# 安装 requirements.txt 中的所有 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 指定容器启动后要运行的命令
CMD ["python", "./web.py"]