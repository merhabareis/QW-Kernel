import os
import sys
import time
from datetime import datetime

try:
    import msvcrt
    MSVCRT_AVAILABLE = True
except ImportError:
    MSVCRT_AVAILABLE = False

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

CURRENT_COLOR = CYAN

def boot_system():
    print(f"{GREEN}QW Kernel Version 0.0.9")
    print("(C) Copyright merhabareis All rights reserved.\n")
    print("Booting kernel...")
    time.sleep(1)
    print(f"Kernel booted successfully.{RESET}\n")

def mini_editor(filename):
    print(f"{YELLOW}--- QWos Text Editor: {filename} ---{RESET}")
    print("Type your lines. To save and exit, type ':q' on a new line and press Enter.\n")
    lines = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print("Current Content:")
            for l in lines:
                print(l, end="")
            print("\n--- Add New Lines ---")

    while True:
        line = input("> ")
        if line.strip() == ":q":
            break
        lines.append(line + "\n")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"{GREEN}'{filename}' saved successfully.{RESET}")

def run_dashboard():
    if not MSVCRT_AVAILABLE:
        print(f"{RED}Error: Dashboard module requires a Windows environment.{RESET}")
        return
        
    options = [
        "1. System Information",
        "2. Network Configuration (IP)",
        "3. About QWKERNEL",
        "4. Exit Dashboard"
    ]
    selected_index = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{CYAN}========================================={RESET}")
        print(f"{GREEN}         QWKERNEL v0.0.7 DASHBOARD       {RESET}")
        print(f"{CYAN}========================================={RESET}\n")
        print(" [Use UP/DOWN arrows to navigate, ENTER to select]\n")

        for i, option in enumerate(options):
            if i == selected_index:
                print(f"{YELLOW}  ==> [ {option} ] <=={RESET}")
            else:
                print(f"      {option}")

        print(f"\n{CYAN}========================================={RESET}")

        key = msvcrt.getch()
        
        if key == b'\xe0':
            arrow = msvcrt.getch()
            if arrow == b'H':  # Up arrow
                selected_index = (selected_index - 1) % len(options)
            elif arrow == b'P':  # Down arrow
                selected_index = (selected_index + 1) % len(options)
                
        elif key == b'\r':  # Enter key
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if selected_index == 0:
                print(f"{YELLOW}--- System Information ---{RESET}\n")
                os.system("systeminfo")
                print(f"\n{CYAN}Press any key to return...{RESET}")
                msvcrt.getch()
                
            elif selected_index == 1:
                print(f"{YELLOW}--- Network Information ---{RESET}\n")
                os.system("ipconfig")
                print(f"\n{CYAN}Press any key to return...{RESET}")
                msvcrt.getch()
                
            elif selected_index == 2:
                print(f"{YELLOW}--- About QWKERNEL v0.0.7 ---{RESET}\n")
                print("Developer: Quality Waranty Corp.")
                print("A hybrid CLI & TUI environment designed for power users.")
                print(f"\n{CYAN}Press any key to return...{RESET}")
                msvcrt.getch()
                
            elif selected_index == 3:
                print("Exiting Dashboard...")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

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
                print(f"{YELLOW}--- QWos v0.0.7 COMMAND LIST ---{RESET}")
                print("  date / time     - Show date and time")
                print("  sysinfo         - System information")
                print("  dashboard       - Open interactive TUI Dashboard")
                print("  cls / clear     - Clear screen")
                print("  dir / ls        - Directory listing")
                print("  cd <path>       - Change directory (e.g.: cd ..)")
                print("  mkdir / rmdir   - Create/Remove directory")
                print("  edit <file>     - Edit file with built-in text editor")
                print("  type / read     - Read file")
                print("  del / rm        - Delete file")
                print("  ren <old> <new> - Rename file")
                print("  ping <ip/host>  - Test network connection (e.g.: ping google.com)")
                print("  color <color>   - Change text color (green, cyan, yellow, red, magenta)")
                print("  calc <expr>     - Calculator")
                print("  exit            - Shutdown system")

            elif cmd in ["date", "time"]:
                print(f"Time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

            elif cmd == "sysinfo":
                print(f"{GREEN}QWos v0.0.7 | Platform: {os.name.upper()} | Python {sys.version.split()[0]}{RESET}")

            # İŞTE YENİ DASHBOARD KOMUTU BURADA
            elif cmd == "dashboard":
                run_dashboard()

            elif cmd in ["cls", "clear"]:
                os.system('cls' if os.name == 'nt' else 'clear')

            elif cmd in ["dir", "ls"]:
                for item in os.listdir(current_dir):
                    prefix = "<DIR>" if os.path.isdir(os.path.join(current_dir, item)) else "<FILE>"
                    print(f"  {prefix:<7} {item}")

            elif cmd == "cd":
                if args:
                    try: os.chdir(args)
                    except Exception as e: print(f"{RED}Error: {e}{RESET}")
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
                    print("Usage: edit <filename>")

            elif cmd in ["type", "read"]:
                if args and os.path.exists(args):
                    with open(args, "r", encoding="utf-8") as f: print(f.read())
                else: print(f"{RED}File not found.{RESET}")

            elif cmd in ["del", "rm"]:
                if args and os.path.exists(args): os.remove(args)

            elif cmd == "ren" and " " in args:
                old, new = args.split(" ", 1)
                os.rename(old, new)

            elif cmd == "ping":
                if args:
                    os.system(f"ping {args}")
                else:
                    print("Usage: ping <address>")

            elif cmd == "color":
                colors = {"green": GREEN, "cyan": CYAN, "yellow": YELLOW, "red": RED, "magenta": MAGENTA}
                if args.lower() in colors:
                    CURRENT_COLOR = colors[args.lower()]
                else:
                    print("Options: green, cyan, yellow, red, magenta")

            elif cmd == "calc":
                if args and all(c in "0123456789+-*/(). " for c in args):
                    print(f"Result: {eval(args)}")

            elif cmd == "exit":
                print("Shutting down QWos...")
                break

            else:
                print(f"{RED}Unknown command. Type 'help' for the list of commands.{RESET}")

        except KeyboardInterrupt:
            print("\nShutting down QWos...")
            break

if __name__ == "__main__":
    main()

#you expected me to put an easter egg here right? well if you are reading this then you already found the easter egg.
