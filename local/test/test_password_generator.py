import string

import pytest
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from password_generator import generate_password, ALLOWED_SYMBOLS


class TestGeneratePassword:
    """generate_password関数のテストクラス"""

    def test_default_length(self):
        """デフォルト長（12文字）のテスト"""
        password = generate_password()
        assert len(password) == 12

    def test_custom_length(self):
        """カスタム長のテスト"""
        for length in [12, 15, 20, 25]:
            password = generate_password(length)
            assert len(password) == length

    def test_minimum_length_validation(self):
        """最小長バリデーションのテスト"""
        with pytest.raises(ValueError, match="パスワードは最低12文字以上にしてください"):
            generate_password(11)

    def test_contains_all_character_types(self):
        """全文字種（大文字・小文字・数字・記号）を含むかのテスト"""
        for _ in range(10):  # 複数回テストして確実性を高める
            password = generate_password(12)

            # 大文字を含むか
            assert any(c in string.ascii_uppercase for c in password), f"大文字が含まれていません: {password}"

            # 小文字を含むか
            assert any(c in string.ascii_lowercase for c in password), f"小文字が含まれていません: {password}"

            # 数字を含むか
            assert any(c in string.digits for c in password), f"数字が含まれていません: {password}"

            # 記号を含むか
            assert any(c in ALLOWED_SYMBOLS for c in password), f"記号が含まれていません: {password}"

    def test_only_allowed_characters(self):
        """許可された文字のみを使用しているかのテスト"""
        allowed_chars = string.ascii_letters + string.digits + ALLOWED_SYMBOLS

        for _ in range(10):
            password = generate_password(12)
            for char in password:
                assert char in allowed_chars, f"許可されていない文字が含まれています: {char} in {password}"

    def test_argon2_hashing_integration(self):
        """Argon2ハッシュ化のテスト"""
        password = generate_password(12)
        ph = PasswordHasher()

        # ハッシュ化が成功するか
        hashed = ph.hash(password)
        assert hashed is not None
        assert len(hashed) > 0

        # ハッシュ化されたパスワードで検証が成功するか
        try:
            ph.verify(hashed, password)
        except VerifyMismatchError:
            pytest.fail("ハッシュ化されたパスワードの検証に失敗しました")
