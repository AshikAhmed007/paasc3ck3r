import re
from colorama import Fore, Style, Back, init

# Initialize colorama for colored terminal output
init(autoreset=True)

AUTHOR = "Ashik Ahmed"

def ascii_art_header():
    header = f"""
{Fore.CYAN}{Style.BRIGHT}

██████╗  ██████╗ ▄▄███▄▄·▄▄███▄▄· ██████╗██╗  ██╗██████╗  ██████╗██╗  ██╗██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██║  ██║╚════██╗██╔════╝██║ ██╔╝╚════██╗██╔══██╗
██████╔╝██║██╗██║███████╗███████╗██║     ███████║ █████╔╝██║     █████╔╝  █████╔╝██████╔╝
██╔═══╝ ██║██║██║╚════██║╚════██║██║     ██╔══██║ ╚═══██╗██║     ██╔═██╗  ╚═══██╗██╔══██╗
██║     ╚█║████╔╝███████║███████║╚██████╗██║  ██║██████╔╝╚██████╗██║  ██╗██████╔╝██║  ██║
╚═╝      ╚╝╚═══╝ ╚═▀▀▀══╝╚═▀▀▀══╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝
                                                                                         
                                                                                
{Style.RESET_ALL}
"""
    print(header)
    print(f"{Fore.MAGENTA}{Style.DIM}Author: {AUTHOR}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}Tool: {TOOL_NAME}{Style.RESET_ALL}\n")

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password))

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    print(f"{Fore.YELLOW}{Style.BRIGHT}Password Requirements:{Style.RESET_ALL}")
    print(f" {Fore.GREEN if length else Fore.RED}✔ Minimum 8 characters{Style.RESET_ALL}")
    print(f" {Fore.GREEN if has_upper else Fore.RED}✔ Contains uppercase letter(s){Style.RESET_ALL}")
    print(f" {Fore.GREEN if has_lower else Fore.RED}✔ Contains lowercase letter(s){Style.RESET_ALL}")
    print(f" {Fore.GREEN if has_digit else Fore.RED}✔ Contains digit(s){Style.RESET_ALL}")
    print(f" {Fore.GREEN if has_special else Fore.RED}✔ Contains special character(s){Style.RESET_ALL}\n")

    if score == 5:
        return f"{Fore.GREEN}{Style.BRIGHT}✅ Excellent! Your password is STRONG.{Style.RESET_ALL}"
    elif 3 <= score < 5:
        missing = []
        if not length:
            missing.append("at least 8 characters")
        if not has_upper:
            missing.append("uppercase letters")
        if not has_lower:
            missing.append("lowercase letters")
        if not has_digit:
            missing.append("digits")
        if not has_special:
            missing.append("special characters")
        
        msg = ", ".join(missing)
        return (f"{Fore.YELLOW}⚠️ Moderate strength. Consider adding: {msg}.{Style.RESET_ALL}")
    else:
        return (f"{Fore.RED}{Style.BRIGHT}❌ Weak password. Try to include uppercase, lowercase, digits, special characters, "
                f"and make it at least 8 characters long.{Style.RESET_ALL}")

def main():
    ascii_art_header()
    print(f"{Fore.CYAN}Enter your password below to check its complexity.{Style.RESET_ALL}")
    password = input(f"{Fore.MAGENTA}Password: {Style.RESET_ALL}")
    print()
    result = check_password_strength(password)
    print(result)
    print("\nThank you for using p@@sc3ck3r!\n")

if __name__ == "__main__":
    main()
