FROM node:alpine

WORKDIR /app
COPY package.json ./
RUN npm install
COPY . /app

ENV PORT 4001



CMD ["npm", "start"]