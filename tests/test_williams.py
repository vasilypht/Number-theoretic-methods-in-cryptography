from ntmcrypt import williams


def main():
    # A
    pr_a, pub_a = williams.gen_keys(256)
    print(f"User: A\n"
          f"Private key = {pr_a}\n"
          f"Public key = {pub_a}\n")

    # B
    pr_b, pub_b = williams.gen_keys(512)
    print(f"User: B\n"
          f"Private key = {pr_b}\n"
          f"Public key = {pub_b}\n")

    # A -> B
    message = "Hello, world!👨‍💻"
    encrypted_data = williams.encrypt(message, pub_b)
    print(f"A -> B\n"
          f"User A:\n"
          f"Message = '{message}'\n"
          f"Encrypted data = {encrypted_data}\n")

    # B
    decrypted_message = williams.decrypt(encrypted_data, pr_b, pub_b)
    print(f"User B:\n"
          f"Decrypted message = {decrypted_message}\n")

    # B -> A
    message = "Hello, world!👨‍💻"
    encrypted_data = williams.encrypt(message, pub_a)
    print(f"B -> A\n"
          f"User B:\n"
          f"Message = '{message}'\n"
          f"Encrypted data = {encrypted_data}\n")

    # A
    decrypted_message = williams.decrypt(encrypted_data, pr_a, pub_a)
    print(f"User A:\n"
          f"Decrypted message = {decrypted_message}\n")


if __name__ == '__main__':
    main()
