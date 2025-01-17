# # 베이스 이미지로 Python 3.8을 사용
# FROM python:3.12-slim

# # 작업 디렉토리 설정
# WORKDIR /lionsnow_dockerfile

# #서버 가동을 위해 필요한 파일은 컨테이너 공간으로 복사
# # COPY main.py /app
# # COPY requirements.txt /app

# COPY . /lionsnow_dockerfile
# RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install -y nginx
# RUN python manage.py collectstatic --noinput

# EXPOSE 8000

# # 컨테이너 실행 시 실행할 명령어 지정
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

# # build 명령어
# # docker build -t myap:lastest . 

FROM python:3.12-slim
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]