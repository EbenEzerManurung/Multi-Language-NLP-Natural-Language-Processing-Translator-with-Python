from deep_translator import GoogleTranslator

# daftar bahasa tujuan
languages = {
    "English": "en",
    "Korean": "ko",
    "Japanese": "ja",
    "Mandarin": "zh-CN",
    "German": "de",
    "French": "fr"
}

print("=== MULTI LANGUAGE NLP TRANSLATOR ===")
print("Ketik 'exit' untuk keluar\n")

while True:
    text = input("Input teks (exit untuk keluar): ")

    if text.lower() == "exit":
        print("Program selesai.")
        break

    print("\n=== HASIL TERJEMAHAN ===")
    for lang_name, lang_code in languages.items():
        result = GoogleTranslator(
            source="auto",
            target=lang_code
        ).translate(text)

        print(f"{lang_name}: {result}")

    print("-" * 35)
