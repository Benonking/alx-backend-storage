import requests
import cachetools
import time

# Create an LRUCache with a maximum size
lru_cache = cachetools.LRUCache(maxsize=100)

# Create a TTLCache with a time-to-live of 10 seconds
ttl_cache = cachetools.TTLCache(maxsize=100, ttl=10)

# Decorator to cache the result
def cache_result(func):
    def wrapper(url):
        # Check if the page is cached
        if url in ttl_cache:
            # Increment the access count and return the cached HTML content
            ttl_cache[url]["count"] += 1
            return ttl_cache[url]["html"]

        # If not cached, make an HTTP request
        response = requests.get(url)

        if response.status_code == 200:
            # Cache the HTML content with an access count and a timestamp
            ttl_cache[url] = {"html": response.text, "count": 1, "timestamp": time.time()}
            return response.text
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"

    return wrapper

# Function to get the page content with caching
@cache_result
def cached_get_page(url):
    return url

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://example.com"
    html = cached_get_page(url)
    print(f"HTML Content of {url}:\n{html}")