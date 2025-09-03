import subprocess

def run_cmd(cmd):
    print(f"Çalıştırılıyor: {cmd}")
    process = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if process.returncode == 0:
        print(process.stdout)
    else:
        print(f"Hata oluştu:\n{process.stderr}")

def main():
    packages = [
        "htop",
        "epel-release",
        "neofetch",
        "nmap",
        "curl",
        "wget",
        "iproute",
        "lsof",
        "net-tools",
        "sysstat",
        "smartmontools",
        "vim",
        "nano",
        "python3",
        "python3-pip",
        "nodejs",
        "git",
        "mariadb-server",
        "postgresql-server",
        "mongodb",
        "httpd",
        "nginx",
        "php",
        "php-mysqlnd",
        "firewalld",
        "fail2ban",
        "ufw",
        "selinux-policy",
        "rsync",
        "cronie",
        "logrotate",
        "tmux",
        "screen",
        "man",
        "wget",
        "openssh-server"
    ]

    print("Sistem güncelleniyor...")
    run_cmd("dnf update -y")

    print("EPEL reposu kuruluyor...")
    run_cmd("dnf install -y epel-release")

    print("Paketler kuruluyor...")
    run_cmd("dnf install -y " + " ".join(packages))

    print("SSH servisi başlatılıyor ve otomatik açılması sağlanıyor...")
    run_cmd("systemctl start sshd")
    run_cmd("systemctl enable sshd")

    print("Kurulum tamamlandı.")

if __name__ == "__main__":
    main()
