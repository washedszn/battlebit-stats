# Stage 1: Build the Angular application
FROM node:latest as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build --omit=dev

# Stage 2: Serve the application with Nginx
FROM nginx:1.19
COPY --from=build /app/dist/frontend /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
