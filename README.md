# DS-Project
A real time collaborative text Editor using CRDT implemented in python. Text Editor support using codemirror5 and websockets using flask.

This project was implemented as a part of `Distributed Systems` Course IIIT Hyderabad Spring 2024 Semester.

## Team Members
1. Anirudh Kaushik (2020111015)
2. Hitesh Goel (2020115003)
3. Shreyansh Agarwal 
## Running the code
 1. Clone the repository
 2. unzip the codemirror.zip file in `static` folder and rename it to `codemirror`
 3. Run the following command to start the server
    ```bash
    flask run -p port_number
    ```
 4. Open the browser and go to `http://localhost:port_number/`
 5. for multiple clients, open another terminal and run the following command
    ```bash
    flask run -p port_number2
    ```
