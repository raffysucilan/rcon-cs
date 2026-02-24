import socket
import re
import argparse

def get_challenge(sock, ip, port):
    packet = b"\xFF\xFF\xFF\xFFchallenge rcon\n"

    try:
        sock.sendto(packet, (ip, port))
        data, _ = sock.recvfrom(4096)

        text = data[4:].decode(errors="ignore")
        match = re.search(r"challenge rcon (\d+)", text)

        if match:
            return match.group(1)

    except ConnectionResetError:
        print("Connection Reset - Wrong IP/Port or server unreachable.")
        return None

    except socket.timeout:
        print("Timeout - No response from server.")
        return None

    return None


def send_command(sock, ip, port, password, challenge, command):
    packet = (
        b"\xFF\xFF\xFF\xFFrcon "
        + challenge.encode()
        + b" "
        + password.encode()
        + b" "
        + command.encode()
        + b"\n"
    )

    sock.sendto(packet, (ip, port))

    try:
        while True:
            data, _ = sock.recvfrom(4096)
            print(data[5:].decode(errors="ignore"), end="")
    except socket.timeout:
        pass
    except ConnectionResetError:
        print("Connection lost.")


def interactive_rcon(ip, port, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    challenge = get_challenge(sock, ip, port)
    if not challenge:
        print("Failed to get challenge.")
        return

    print(f"Connected to {ip}:{port}")
    print("Type commands. Type ':q' to close.\n")

    while True:
        try:
            command = input("rcon_cs > ").strip()

            if not command:
                continue

            if command.lower() in (":q"):
                break

            send_command(sock, ip, port, password, challenge, command)

        except KeyboardInterrupt:
            break

    sock.close()
    print("Disconnected.")


def single_command(ip, port, password, command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    challenge = get_challenge(sock, ip, port)
    if not challenge:
        print("Failed to get challenge.")
        sock.close()
        return

    send_command(sock, ip, port, password, challenge, command)
    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Counter-Strike 1.6 RCON CLI")

    parser.add_argument("-i", "--ip", required=True, help="IP address")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port")
    parser.add_argument("-a", "--password", required=True, help="Password")
    parser.add_argument("command", nargs="*", help="Command to execute")

    args = parser.parse_args()
    if args.command:
        # Standalone mode
        command_str = " ".join(args.command)
        single_command(args.ip, args.port, args.password, command_str)
    else:
        # Interactive mode
        interactive_rcon(args.ip, args.port, args.password)