FROM ubuntu:latest

ENV VERSION=1.2.0

RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install -y vim
RUN apt-get install -y zip unzip
RUN pip3 install python-dotenv
# Copy python file
COPY zip_job.py /tmp

# Print the architecture
RUN uname -m && cat /etc/os-release
RUN if [ -f /tmp/zip_job.py ]; then echo "zip_job.py exists."; else echo "Couldn't find zip_job."; fi
# Print to check if the py file is in the tmp folder 
CMD if [ -f /tmp/zip_job.py ]; then echo "zip_job.py exists."; else echo "Couldn't find zip_job."; fi
# CMD uname -m && cat /etc/os-release && if [ -f /tmp/zip_job.py ]; then echo "zip_job.py exists."; else echo "Couldn't find zip_job."; fi
