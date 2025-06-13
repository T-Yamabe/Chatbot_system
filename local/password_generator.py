import secrets
import string
import random

from argon2 import PasswordHasher


# 使用可能な記号
ALLOWED_SYMBOLS: str = '!"#$%&\'()*+=-/<>_~^:;,.?@\\|[]{}`'


# パスワード生成関数
def generate_password(length: int = 12) -> str:
    """指定された長さのパスワードを生成する関数"""
    if length < 12:
        raise ValueError("パスワードは最低12文字以上にしてください。")

    # 各カテゴリから1文字ずつ選択（必須条件）
    upper: str = secrets.choice(string.ascii_uppercase)
    lower: str = secrets.choice(string.ascii_lowercase)
    digit: str = secrets.choice(string.digits)
    symbol: str = secrets.choice(ALLOWED_SYMBOLS)

    # 残りの文字を全カテゴリからランダムに選択
    all_chars: str = string.ascii_letters + string.digits + ALLOWED_SYMBOLS
    remaining: list[str] = [secrets.choice(all_chars) for _ in range(length - 4)]

    # ランダムな並びにシャッフル
    password_list: list[str] = list(upper + lower + digit + symbol + ''.join(remaining))
    random.shuffle(password_list)

    return ''.join(password_list)


def main() -> None:
    """メイン関数：パスワード生成とハッシュ化を行う"""
    # 12文字のパスワードを生成
    password: str = generate_password(12)
    # Argon2でハッシュ化
    ph = PasswordHasher()
    hashed_password: str = ph.hash(password)
    print(f"password: {password}")
    print(f"hashed_password: {hashed_password}")


if __name__ == "__main__":
    main()
