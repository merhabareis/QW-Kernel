import os
import sys
import time
from datetime import datetime

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

CURRENT_COLOR = CYAN

def boot_system():
    print(f"{GREEN}QW Kernel Version 0.0.7")
    print("(C) Copyright merhabareis All rights reserved.\n")
    print("Booting kernel...")
    time.sleep(1)
    print(f"Kernel booted successfully.{RESET}\n")

def mini_editor(filename):
    print(f"{YELLOW}--- QWos Metin Editörü: {filename} ---{RESET}")
    print("Satırları yazın. Kaydetmek ve çıkmak için tek satıra ':q' yazıp Enter'a basın.\n")
    lines = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print("Mevcut İçerik:")
            for l in lines:
                print(l, end="")
            print("\n--- Yeni Satır Ekle ---")

    while True:
        line = input("> ")
        if line.strip() == ":q":
            break
        lines.append(line + "\n")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"{GREEN}'{filename}' başarıyla kaydedildi.{RESET}")

def main():
    global CURRENT_COLOR
    boot_system()
    
    while True:
        try:
            current_dir = os.getcwd()
            user_input = input(f"{CURRENT_COLOR}{current_dir}>{RESET} ").strip()
            
            if not user_input:
                continue
                
            parts = user_input.split(" ", 1)
            cmd = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            if cmd == "help":
                print(f"{YELLOW}--- QWos v0.0.3 KOMUT LİSTESİ ---{RESET}")
                print("  date / time     - Tarih ve saat")
                print("  sysinfo         - Sistem bilgisi")
                print("  cls / clear     - Ekranı temizle")
                print("  dir / ls        - Dizin listesi")
                print("  cd <path>       - Dizin değiştir (Örn: cd ..)")
                print("  mkdir / rmdir   - Klasör oluştur/sil")
                print("  edit <dosya>    - Dâhilî metin editörü ile dosya düzenle")
                print("  type / read     - Dosya oku")
                print("  del / rm        - Dosya sil")
                print("  ren <eski> <yeni>- İsim değiştir")
                print("  ping <ip/host>  - Ağ bağlantısını test et (Örn: ping google.com)")
                print("  color <renk>    - Yazı rengini değiştir (green, cyan, yellow, red, magenta)")
                print("  calc <ifade>    - Hesap makinesi")
                print("  exit            - Sistemi kapat")

            elif cmd in ["date", "time"]:
                print(f"Zaman: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

            elif cmd == "sysinfo":
                print(f"{GREEN}QWos v0.0.3 | Platform: {os.name.upper()} | Python {sys.version.split()[0]}{RESET}")

            elif cmd in ["cls", "clear"]:
                os.system('cls' if os.name == 'nt' else 'clear')

            elif cmd in ["dir", "ls"]:
                for item in os.listdir(current_dir):
                    prefix = "<DIR>" if os.path.isdir(os.path.join(current_dir, item)) else "<FILE>"
                    print(f"  {prefix:<7} {item}")

            elif cmd == "cd":
                if args:
                    try: os.chdir(args)
                    except Exception as e: print(f"{RED}Hata: {e}{RESET}")
                else: print(current_dir)

            elif cmd == "mkdir":
                if args: os.makedirs(args, exist_ok=True)

            elif cmd == "rmdir":
                if args: os.rmdir(args)

            elif cmd == "edit":
                if args:
                    filename = args if args.endswith(".txt") else f"{args}.txt"
                    mini_editor(filename)
                else:
                    print("Kullanım: edit <dosya_adı>")

            elif cmd in ["type", "read"]:
                if args and os.path.exists(args):
                    with open(args, "r", encoding="utf-8") as f: print(f.read())
                else: print(f"{RED}Dosya bulunamadı.{RESET}")

            elif cmd in ["del", "rm"]:
                if args and os.path.exists(args): os.remove(args)

            elif cmd == "ren" and " " in args:
                old, new = args.split(" ", 1)
                os.rename(old, new)

            elif cmd == "ping":
                if args:
                    os.system(f"ping {args}")
                else:
                    print("Kullanım: ping <adres>")

            elif cmd == "color":
                colors = {"green": GREEN, "cyan": CYAN, "yellow": YELLOW, "red": RED, "magenta": MAGENTA}
                if args.lower() in colors:
                    CURRENT_COLOR = colors[args.lower()]
                else:
                    print("Seçenekler: green, cyan, yellow, red, magenta")

            elif cmd == "calc":
                if args and all(c in "0123456789+-*/(). " for c in args):
                    print(f"Sonuç: {eval(args)}")

            elif cmd == "exit":
                print("QWos kapatılıyor...")
                break

            else:
                print(f"{RED}Bilinmeyen komut. 'help' yazabilirsiniz.{RESET}")

        except KeyboardInterrupt:
            print("\nQWos kapatılıyor...")
            break

if __name__ == "__main__":
    main()
