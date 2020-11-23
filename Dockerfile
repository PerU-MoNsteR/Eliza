#running successfully

FROM suhaash02/eliza:latest   

#hope will run fast

#clonning repo 

RUN git clone https://github.com/suhaash02/Eliza.git /root/userbot

#working directory 
WORKDIR /root/userbotz

# Install requirements
RUN pip3 install -U -r requirements.txt

#success env
ENV PATH="/home/userbot/bin:$PATH"

#command executer

CMD ["python3","-m","userbot"]
