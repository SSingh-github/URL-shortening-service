# URL Shortening Service

![Badge](https://img.shields.io/badge/python-3.8%2B-blue)
![Badge](https://img.shields.io/badge/flask-2.0%2B-green)
![Badge](https://img.shields.io/badge/redis-database-orange)

A Flask-based URL shortening service that converts long URLs into short, memorable links. This project uses Redis for efficient storage and retrieval of URLs and implements HTTP redirects for seamless user redirection.

---

## About the Project

### Problem Solved
Long URLs are difficult to share, remember, and use in contexts like social media or printed materials. This project solves this problem by:
1. **Shortening URLs**: Converting long URLs into short, easy-to-share links.
2. **Efficient Storage**: Using Redis for fast storage and retrieval of URL mappings.
3. **Seamless Redirection**: Automatically redirecting users from the short URL to the original long URL.

---

## Features
- **URL Shortening**: Converts long URLs into short, unique codes.
- **Database Storage**: Stores both short and long URLs in Redis for quick access.
- **HTTP Redirects**: Automatically redirects users from the short URL to the original URL.
- **RESTful API**: Provides endpoints for creating and accessing short URLs.

---

## Technologies and Skills Used
- **Backend Framework**: Flask (Python)
- **Database**: Redis (in-memory key-value store)
- **API Design**: RESTful endpoints
- **HTTP Protocols**: Redirects (HTTP 301/302)
- **Other Tools**: Git, Docker (optional for containerization)

---

## How It Works
1. A user submits a long URL to the service.
2. The service generates a unique short code for the URL and stores the mapping in Redis.
3. When a user visits the short URL, the service looks up the original URL in Redis and performs an HTTP redirect.

---

## Steps to Clone and Run the Project

### Prerequisites
- Python 3.8+
- Redis server (locally or via Docker)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
