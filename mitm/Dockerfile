FROM mitmproxy/mitmproxy
WORKDIR /app
COPY mitm.py /app/mitm.py
CMD ["mitmdump", "-s", "/app/mitm.py", "--listen-host", "0.0.0.0", "--listen-port=8080"]
