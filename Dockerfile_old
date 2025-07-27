 
FROM python
#FROM jpgmoreira/coloramatest 

WORKDIR /reverse_ai

# from colorama 
# import Fore
# Install dependencies
# RUN apt-get update && apt-get install -y \
#    colorama

RUN python3 -m pip install colorama 

COPY . /reverse_ai

# For Anonymous volumes only
# VOLUME [ "/ai_data/test/" ]

# EXPOSE 80

CMD [ "python", "main.py" ]