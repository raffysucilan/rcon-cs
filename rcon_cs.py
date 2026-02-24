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
        print("Connection reset - wrong IP/port or server unreachable")
        return None

    except socket.timeout:
        print("Timeout - no response from server")
        return None

    return None


def send_rcon(ip, port, password, command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)

    challenge = get_challenge(sock, ip, port)

    if not challenge:
        print("Failed to get challenge")
        return

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
            print(data[5:].decode(errors="ignore"))
    except socket.timeout:
        pass
    except ConnectionResetError:
        pass

    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count-Strike 1.6 RCON Client")

    parser.add_argument("-i", "--ip", required=True, help="IP address")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port")
    parser.add_argument("-a", "--password", required=True, help="Password")
    parser.add_argument("command", nargs="+", help="Command to execute")

    args = parser.parse_args()

    command_str = " ".join(args.command)

    send_rcon(args.ip, args.port, args.password, command_str)