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
    print(f"{GREEN}QW Kernel [Version 0.0.8 Extended DOS Edition]")
    print("(C) Copyright merhabareis All rights reserved.\n")
    print("Booting kernel...")
    time.sleep(1)
    print(f"Kernel booted successfully.{RESET}\n")

def advanced_editor(filename):
    lines = []
    is_new = not os.path.exists(filename)
    
    if not is_new:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f.readlines()]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{YELLOW}--- QW Kernel Advanced Text Editor: {filename} ---{RESET}")
        
        if is_new:
            print(f"{GREEN}[ NEW FILE ]{RESET}")
        else:
            print(f"{CYAN}[ EXISTING FILE ]{RESET}")
            
        print(f"{CYAN}Commands: :w (Save) | :q (Quit) | :wq (Save & Quit) | :del <line_no> (Delete line) | :clear (Clear all){RESET}\n")
        
        print("--- File Content ---")
        if not lines:
            print(f"{MAGENTA}(Empty File){RESET}")
        else:
            for idx, line in enumerate(lines, start=1):
                print(f"{idx:3d} | {line}")
        print("-" * 30)

        choice = input("editor> ")
        cmd_choice = choice.strip()

        if cmd_choice == ":q":
            confirm = input("Discard changes? (y/n): ").strip().lower()
            if confirm == 'y':
                break
        elif cmd_choice == ":w":
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines([l + "\n" for l in lines])
                print(f"{GREEN}Saved successfully.{RESET}")
                is_new = False
            except Exception as e:
                print(f"{RED}Error saving file: {e}{RESET}")
            time.sleep(0.8)
        elif cmd_choice == ":wq":
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines([l + "\n" for l in lines])
                print(f"{GREEN}Saved and exited.{RESET}")
                time.sleep(0.8)
                break
            except Exception as e:
                print(f"{RED}Error saving file: {e}{RESET}")
                time.sleep(1.5)
        elif cmd_choice == ":clear":
            lines = []
        elif cmd_choice.startswith(":del "):
            try:
                line_no = int(cmd_choice.split(" ")[1])
                if 1 <= line_no <= len(lines):
                    removed = lines.pop(line_no - 1)
                    print(f"{YELLOW}Deleted line {line_no}: {removed}{RESET}")
                else:
                    print(f"{RED}Invalid line number.{RESET}")
                time.sleep(0.8)
            except ValueError:
                print(f"{RED}Usage: :del <line_number>{RESET}")
                time.sleep(0.8)
        else:
            if choice.endswith('\n'):
                choice = choice[:-1]
            lines.append(choice)

def run_dashboard():
    if not MSVCRT_AVAILABLE:
        print(f"{RED}Error: Dashboard module requires a Windows environment.{RESET}")
        return
        
    options = [
        "1. System Information",
        "2. Network Configuration (IP)",
        "3. About QW Kernel",
        "4. Exit Dashboard"
    ]
    selected_index = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{CYAN}========================================={RESET}")
        print(f"{GREEN}        QW KERNEL v0.0.8 DASHBOARD       {RESET}")
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
            if arrow == b'H':
                selected_index = (selected_index - 1) % len(options)
            elif arrow == b'P':
                selected_index = (selected_index + 1) % len(options)
                
        elif key == b'\r':
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
                print(f"{YELLOW}--- About QW Kernel v0.0.8 ---{RESET}\n")
                print("Developer: merhabareis")
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
    
    # Varsayılan başlangıç dizinini C:\Users\<kullanıcı> olarak ayarla
    try:
        os.chdir(os.path.expanduser("~"))
    except Exception:
        pass

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
                print(f"{YELLOW}--- QW Kernel v0.0.8 COMMAND LIST ---{RESET}")
                print("  date / time     - Show date and time")
                print("  sysinfo         - System information")
                print("  dashboard       - Open interactive TUI Dashboard")
                print("  cls / clear     - Clear screen")
                print("  dir / ls        - Directory listing")
                print("  cd <path>       - Change directory (e.g.: cd ..)")
                print("  mkdir / rmdir   - Create/Remove directory")
                print("  create / touch  - Create a new empty file")
                print("  edit <file>     - Create/Edit file with built-in text editor")
                print("  type / read     - Read file")
                print("  del / rm        - Delete file")
                print("  ren <old> <new> - Rename file")
                print("  echo <text>     - Print text or write to file (e.g.: echo hello > a.txt)")
                print("  ping <ip/host>  - Test network connection (e.g.: ping google.com)")
                print("  color <color>   - Change text color (green, cyan, yellow, red, magenta)")
                print("  calc <expr>     - Calculator")
                print("  exit            - Shutdown system")

            elif cmd in ["date", "time"]:
                print(f"Time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

            elif cmd == "sysinfo":
                print(f"{GREEN}QW Kernel v0.0.8 | Platform: {os.name.upper()} | Python {sys.version.split()[0]}{RESET}")

            elif cmd == "dashboard":
                run_dashboard()

            elif cmd in ["cls", "clear"]:
                os.system('cls' if os.name == 'nt' else 'clear')

            elif cmd in ["dir", "ls"]:
                try:
                    for item in os.listdir(current_dir):
                        prefix = "<DIR>" if os.path.isdir(os.path.join(current_dir, item)) else "<FILE>"
                        print(f"  {prefix:<7} {item}")
                except Exception as e:
                    print(f"{RED}Error reading directory: {e}{RESET}")

            elif cmd == "cd":
                if args:
                    try: os.chdir(args)
                    except Exception as e: print(f"{RED}Error: {e}{RESET}")
                else: print(current_dir)

            elif cmd == "mkdir":
                if args: 
                    try: os.makedirs(args, exist_ok=True)
                    except Exception as e: print(f"{RED}Error: {e}{RESET}")

            elif cmd == "rmdir":
                if args:
                    try: os.rmdir(args)
                    except Exception as e: print(f"{RED}Error: {e}{RESET}")

            elif cmd in ["create", "touch"]:
                if args:
                    filename = args if "." in args else f"{args}.txt"
                    if not os.path.exists(filename):
                        try:
                            open(filename, 'w').close()
                            print(f"{GREEN}File '{filename}' created successfully.{RESET}")
                        except Exception as e:
                            print(f"{RED}Error creating file: {e}{RESET}")
                    else:
                        print(f"{YELLOW}File already exists.{RESET}")
                else:
                    print("Usage: create <filename>")

            elif cmd == "edit":
                if args:
                    filename = args if "." in args else f"{args}.txt"
                    advanced_editor(filename)
                else:
                    print("Usage: edit <filename>")

            elif cmd in ["type", "read"]:
                if args and os.path.exists(args):
                    try:
                        with open(args, "r", encoding="utf-8") as f: print(f.read())
                    except Exception as e:
                        print(f"{RED}Error reading file: {e}{RESET}")
                else: print(f"{RED}File not found.{RESET}")

            elif cmd in ["del", "rm"]:
                if args and os.path.exists(args):
                    try: os.remove(args)
                    except Exception as e: print(f"{RED}Error deleting file: {e}{RESET}")
                else:
                    print(f"{RED}File not found.{RESET}")

            elif cmd == "ren" and " " in args:
                try:
                    old, new = args.split(" ", 1)
                    os.rename(old, new)
                except Exception as e:
                    print(f"{RED}Error renaming file: {e}{RESET}")

            elif cmd == "echo":
                if ">>" in args:
                    parts_echo = args.split(">>", 1)
                    text = parts_echo[0].strip()
                    filename = parts_echo[1].strip()
                    if text.startswith('"') and text.endswith('"'): text = text[1:-1]
                    try:
                        with open(filename, "a", encoding="utf-8") as f:
                            f.write(text + "\n")
                    except Exception as e:
                        print(f"{RED}Error writing to file: {e}{RESET}")
                elif ">" in args:
                    parts_echo = args.split(">", 1)
                    text = parts_echo[0].strip()
                    filename = parts_echo[1].strip()
                    if text.startswith('"') and text.endswith('"'): text = text[1:-1]
                    try:
                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(text + "\n")
                    except Exception as e:
                        print(f"{RED}Error writing to file: {e}{RESET}")
                else:
                    text = args.strip()
                    if text.startswith('"') and text.endswith('"'): text = text[1:-1]
                    print(text)

            elif cmd == "ping":
                if args:
                    ping_cmd = f"ping -n 4 {args}" if os.name == "nt" else f"ping -c 4 {args}"
                    os.system(ping_cmd)
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
                    try:
                        print(f"Result: {eval(args)}")
                    except Exception as e:
                        print(f"{RED}Calculation error: {e}{RESET}")
                else:
                    print(f"{RED}Invalid expression or missing argument.{RESET}")

            elif cmd == "exit":
                print("Shutting down QW Kernel...")
                break

            else:
                print(f"{RED}Unknown command. Type 'help' for the list of commands.{RESET}")

        except KeyboardInterrupt:
            print("\nShutting down QW Kernel...")
            break
        except Exception as e:
            print(f"{RED}An unexpected error occurred: {e}{RESET}")

if __name__ == "__main__":
    main()