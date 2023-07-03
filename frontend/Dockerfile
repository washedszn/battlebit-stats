# Use an official Node runtime as the parent image
FROM node:latest

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY package*.json /app/

# Install any needed packages specified in package.json
RUN npm install

# Bundle the app source inside the Docker image
COPY . /app/

# Make port 4200 available to the outside world
EXPOSE 4200

# Run npm start when the container launches
CMD ["npm", "start"]
