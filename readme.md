to start the services, run:
```bash
docker-compose up -d --build
```
This repo shows how to use
- Nginx
    - load balancing
    - reverse proxy
    - static resouce hosting
- Fastapi
    - render dynamic HTML page with jinja2 template
    - validate input schema with Pydantic model
    - auto swagger testing UI
    - connect with Nginx
- Docker Compose
    - how to use fragments and anchors
    - how to spin up multiple services 