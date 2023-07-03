# BattleBit Remastered Statistics 

This is a web application to display statistics for the game BattleBit Remastered. This project uses Angular for the frontend, Django for the backend, and PostgreSQL for the database, with Docker to manage the environment.

## Prerequisites

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

## Local Development

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/battlebit-remastered-stats.git
    ```

2. Navigate into the cloned repository:

    ```
    cd battlebit-remastered-stats
    ```

3. Copy the `.env.example` file to `.env` and fill it with the necessary information:

    ```
    cp .env.example .env
    ```
    Then, open the `.env` file and set the values for the variables:

    ```
    POSTGRES_DB=your_database
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    DJANGO_SECRET_KEY=your_secret_key
    ```
    
    Please replace `your_database`, `your_user`, `your_password`, and `your_secret_key` with the appropriate values for your setup.

4. Build and start the Docker containers:

    ```
    docker-compose up --build
    ```

    This will start three services:

    - A Django API server running on [http://localhost:8000](http://localhost:8000)
    - An Angular server for the frontend running on [http://localhost:4200](http://localhost:4200)
    - A PostgreSQL server for the database

5. You can stop the Docker containers at any time by pressing `Ctrl+C` in the terminal where you ran `docker-compose up`, or by running `docker-compose down` in another terminal.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT](LICENSE)

