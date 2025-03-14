from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
    try:
        data = request.get_json()
        print("受け取ったデータ:", data)  # 受け取ったデータをログに出力

        uid = data.get('uid')
        createAt = data.get('createAt')

        if not uid or not createAt:
            raise ValueError("uid または createAt が不足しています")

        # ここで、uid と createAt を使って暗号化処理を行う
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(f"{uid}-{createAt}".encode())

        return jsonify({"encrypted_data": encrypted_data.decode()}), 200

    except Exception as e:
        print(f"エラー発生: {e}")  # エラーメッセージを表示
        return jsonify({"error": str(e)}), 500
