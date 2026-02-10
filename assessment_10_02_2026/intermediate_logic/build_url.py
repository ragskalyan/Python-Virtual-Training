"""
Build URL: Write a function called buildUrl that taken an endpoint (string), a params object (key-value pairs), and
a use https boolean

    1. The function should return a full url string
    2. if use Https is true, the url starts with https:// otherwise http://
    3. it must loop through the params object and append them as a query string
        ex. endpoint?key1=value1&key2=value2
"""

def build_url(endpoint, params, use_https=None):

    protocol = "https" if use_https else "http"

    query_string = ""

    for k, v in params.items():
        if query_string:
            query_string += "&"
        query_string += f"{k}={v}"

    return f"{protocol}://{endpoint}?{query_string}"


print(
    build_url(
        endpoint="orange.com",
        params={"name": "kalyan", "id": "7"},
        use_https=False,
    )
)

