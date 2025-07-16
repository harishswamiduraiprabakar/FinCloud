FROM public.ecr.aws/amazonlinux/amazonlinux:2023

RUN yum update -y &&     yum install -y python3 python3-pip &&     yum clean all

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates/

RUN pip3 install flask gunicorn

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
