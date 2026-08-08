import socket
import threading


# ============================================================
# Configuration
# ============================================================

HOST = "127.0.0.1"
PORT = 5000


# ============================================================
# Layout
# ============================================================

def print_header(title):

    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


# ============================================================
# Receive Messages
# ============================================================

def receive_messages(connection, user_name):

    while True:

        try:

            message = connection.recv(1024).decode()

            if not message:
                print("\nConnection closed.")
                break

            print(f"\n{user_name}: {message}")

            print("You: ", end="", flush=True)

            if message.lower() == "exit":
                break

        except:

            break


# ============================================================
# SERVER
# ============================================================

def start_server():

    print_header("CHAT SERVER")

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind(
        (HOST, PORT)
    )

    server.listen(1)

    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for client connection...")

    connection, address = server.accept()

    print(f"Client connected: {address}")

    # Receive messages in separate thread
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(connection, "Client"),
        daemon=True
    )

    receive_thread.start()

    print("\nChat started!")
    print("Type 'exit' to close the chat.\n")

    while True:

        try:

            message = input("You: ")

            connection.send(
                message.encode()
            )

            if message.lower() == "exit":
                break

        except:

            print("Connection closed.")
            break

    connection.close()
    server.close()

    print("\nServer stopped.")


# ============================================================
# CLIENT
# ============================================================

def start_client():

    print_header("CHAT CLIENT")

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client.connect(
            (HOST, PORT)
        )

    except ConnectionRefusedError:

        print("Unable to connect to server.")
        print("Please start the Server first.")

        return

    print(f"Connected to server {HOST}:{PORT}")

    # Receive messages in separate thread
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client, "Server"),
        daemon=True
    )

    receive_thread.start()

    print("\nChat started!")
    print("Type 'exit' to close the chat.\n")

    while True:

        try:

            message = input("You: ")

            client.send(
                message.encode()
            )

            if message.lower() == "exit":
                break

        except:

            print("Connection closed.")
            break

    client.close()

    print("\nClient stopped.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print_header(
            "PYTHON CHAT APPLICATION"
        )

        print("1. Start Server")
        print("2. Start Client")
        print("0. Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            start_server()

        elif choice == "2":

            start_client()

        elif choice == "0":

            print("\nThank you!")
            break

        else:

            print("\nInvalid choice!")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()
