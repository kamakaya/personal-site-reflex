# Rommel Silva - Personal Reflex Website
This website is a web app built using the Reflex.dev framework, which allows developers to build modern web-apps in pure python.

I used this as a simple experiment to play around with the Reflex framework.

## Deployment
The application is deployed on Railway.app using nixpacks and Caddy.

### Custom build plan: `nixpacks.toml`
- Runs all the necessary commands to setup, initialize, export, and install Caddy
- Starts the Reflex backend and Caddy server using parallel to avoid having to run two separate services in the project

### The Caddy Server/Proxy: `Caddyfile`
- Serves the exported frontend Reflex app
- Proxies all requests to /backend/* through to the Reflex backend server

### Live Demo
The application can be accessed [here](https://personal-site-reflex-production.up.railway.app/)