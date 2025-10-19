---
date: 2025-10-19T17:20:00
---
docker-compose.yml 
```docker 
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    restart: unless-stopped
    environment:
      TZ: "Etc/GMT-4"
      WEBPASSWORD: "batooot"
      DNSMASQ_LISTENING: all
    volumes:
      - "./etc-pihole:/etc/pihole"
      - "./etc-dnsmasq.d:/etc/dnsmasq.d"
    cap_add:
      - NET_ADMIN
    ports:
      - "80:80"
      - "53:53/tcp"
      - "53:53/udp"
```

run -> `docker compose up -d`

change password -> `docker exec -it pihole pihole setpassword 'batooot'`

go to ``