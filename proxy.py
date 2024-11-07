from mitmproxy import ctx
from mitmproxy import http

# Target server
TARGET_HOST = "192.168.2.8"
TARGET_PORT = 11443

# List of domains to forward
FORWARD_DOMAINS = [
    "yuanshen.com",
    "mihoyo.com",
    "hoyoverse.com",
]

# List of domains to NOT forward
EXCLUDED_DOMAINS = [
    "autopatchhk.yuanshen.com",
]

LOG_KEYWORDS = [
    # "h5log", # minor-api-os.hoyoverse.com
    # "admin", # webstatic.hoyoverse.com
]


def request(flow: http.HTTPFlow) -> None:
    # First check if the request host matches any excluded domains
    if any(flow.request.pretty_host.endswith(domain) for domain in EXCLUDED_DOMAINS):
        ctx.log.warn(f"Skipping forwarding for excluded domain: {flow.request.pretty_host}")
        return
    
    # Log keyword URLs
    if any(keyword in flow.request.pretty_url for keyword in LOG_KEYWORDS):
        ctx.log.warn(f"Keyword URL: {flow.request.pretty_url}")
        
    # Check if the request host contains any of our forward domains
    if any(flow.request.pretty_host.endswith(domain) for domain in FORWARD_DOMAINS):
        
        # Preserve the original scheme (http or https)
        original_host = flow.request.pretty_host
        original_scheme = flow.request.scheme
        original_port = flow.request.port
        
        # Update the host header and target
        flow.request.headers["Host"] = flow.request.pretty_host
        flow.request.host = TARGET_HOST
        flow.request.port = TARGET_PORT
        flow.request.scheme = "http"
        
        ctx.log.info(f"Forwarding request for {original_scheme}://{original_host}:{original_port} to {TARGET_HOST}:{TARGET_PORT}")
