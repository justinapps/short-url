# short-url

A simple URL shortener in Django. Was curious how URL shorteners were implemented.

1. The original URL is provided.

2. It is shortened to a 4 character slug (ensure the slug does not already exist). The slug is a primary key.

3. When the shortened URL is visited, the original URL is retrieved from the database. Remember, the slug is a primary key.
