FROM discord-bot-py:latest

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

RUN pip3 install setuptools
RUN pip3 install wheel
RUN pip3 install discord.py

COPY ../../Bot /usr/src/bot

CMD ["python3", "main.py"]