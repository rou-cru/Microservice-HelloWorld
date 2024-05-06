FROM python AS base

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

FROM base AS exec
EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0", "--debug"]