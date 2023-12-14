FROM prefecthq/prefect:2.14-python3.11
COPY flows/*.py /modules/
ENV PYTHONPATH=$PYTHONPATH:modules/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt