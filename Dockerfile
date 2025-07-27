
FROM python

WORKDIR /reverse_ai

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
RUN python3 -m pip install colorama 

# Make sure the output directory exists
RUN mkdir -p output

# Expose Flask default port
EXPOSE 5000

CMD [ "sh", "start.sh" ]