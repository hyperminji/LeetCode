class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = longUrl.encode()
        return url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url = shortUrl.decode()
        return url

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))