shell_name = input("Enter shell name: ").strip()

if shell_name == "bash":
    profile_file = "bashrc"
elif shell_name == "ksh":
    profile_file = "kshrc"
elif shell_name == "psh":
    profile_file = "winprofile"
else:
    shell_name = "nologin"
    profile_file = "/etc/profile"

print("Shell name:", shell_name)
print("Shell profile filename:", profile_file)