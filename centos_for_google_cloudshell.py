import os
import subprocess

def run_command(cmd):
    print(f"\nKomut çalıştırılıyor: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("Bir hata oluştu!")

def main():
    print("Docker kuruluyor...")
    run_command("sudo apt update")
    run_command("sudo apt install -y docker.io")

    print("Containerd işlemleri yapılıyor...")
    run_command("sudo apt remove -y containerd")
    run_command("sudo apt upgrade -y containerd")

    print("Docker servisi etkinleştiriliyor...")
    run_command("sudo systemctl enable docker")
    run_command("sudo systemctl start docker")

    print("\nLütfen istediğiniz CentOS dağıtımını seçin:")
    options = [
        "stream10",
        "stream9",
        "centos8",
        "centos7",
        "centos6",
        "centos5",
        "centos4",
        "centos3",
        "centos2",
        "centos1"
    ]

    for i, option in enumerate(options):
        print(f"{i} - {option}")

    secim = input("Seçiminizi girin (0-9): ")
    if not secim.isdigit() or int(secim) not in range(len(options)):
        print("Geçersiz seçim!")
        return

    secim = int(secim)
    print(f"Seçiminiz: {options[secim]}")

    if secim == 0:
        docker_cmd = "docker run -it quay.io/centos/centos:stream10"
    elif secim == 1:
        docker_cmd = "docker run -it quay.io/centos/centos:stream9"
    else:
        docker_cmd = f"sudo docker run -it centos:{9 - secim + 1}"  # centos:8 için secim=2 vs.

    run_command(docker_cmd)

if __name__ == "__main__":
    main()
