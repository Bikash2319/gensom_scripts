def get_token(token_path=r"C:\Automation\gensom_scripts\backend\Login_Module\token.txt"):

    with open(token_path, "r") as f:
        return f.read().strip()
    