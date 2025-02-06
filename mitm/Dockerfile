FROM mitmproxy/mitmproxy

WORKDIR /app

# Copy the MITM attack script into the container
COPY mitm.py /app/mitm.py

# Run mitmproxy with the custom script
CMD ["mitmdump", "-s", "/app/mitm.py", "--listen-host", "0.0.0.0", "--listen-port=8080"]
