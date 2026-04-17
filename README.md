cat > ~/crypto-101/README.md << 'EOF'
# Crypto 101 — Classic Ciphers

Implementation and breaking of classical ciphers in Python — Caesar and Vigenère.
Built as a portfolio project to understand the fundamentals of cryptography.

## Features

- Caesar cipher — encrypt and decrypt with a numeric key
- Vigenère cipher — encrypt and decrypt with a word key
- Caesar brute force — tries all 25 possible shifts
- Frequency analysis — breaks Caesar using letter frequency statistics
- Language support — Polish and English frequency tables

## Usage

```bash
python3 crypto.py
```

### Menu options
1. Encrypt   — Caesar
2. Decrypt   — Caesar
3. Crack     — Caesar (brute force, all 25 shifts)
4. Encrypt   — Vigenère
5. Decrypt   — Vigenère
6. Frequency analysis (Caesar cracking)
7. Exit
## How it works

### Caesar cipher
Each letter is shifted by a fixed number of positions in the alphabet.
With shift 3: A→D, B→E, Z→C. Decryption reverses the shift.

### Vigenère cipher
An extension of Caesar — instead of one fixed shift, a keyword is used.
Each letter of the keyword defines a different shift for the corresponding
letter of the plaintext. Considered unbreakable for ~300 years.

### Frequency analysis
Natural languages have predictable letter distributions.
In Polish, A appears ~8.9% of the time. In English, E appears ~12.7%.
By comparing the frequency distribution of the ciphertext to the expected
distribution of the target language, we can guess the shift key.

## Known limitations

### Short ciphertexts
Frequency analysis requires 200+ letters to work reliably.
With short texts the letter distribution is too random to draw conclusions —
brute force is more effective in those cases.

### Polish diacritics problem
Classical ciphers operate only on the basic 26-letter Latin alphabet.
Polish letters (ą, ę, ó, ś, ź, ż, ć, ń) are not part of this alphabet,
so Polish text must be written without diacritics before encryption.

This causes a real problem for frequency analysis:
- Standard Polish frequency table assumes natural text with diacritics
- Text without diacritics has a different distribution (e.g. without ą and ę,
  the letter A appears more often than expected)
- This mismatch causes the analyzer to guess the wrong key

During testing, encrypting "ALA MA KOTA I PSA" with shift 7 and then
running frequency analysis returned the wrong key because the text was
too short and lacked diacritics. Brute force confirmed the correct result.

This is an intentional demonstration — real cryptanalysis requires
high-quality, representative source material.

## What I learned

- How substitution ciphers work at the code level
- Why Vigenère is stronger than Caesar (polyalphabetic substitution)
- How frequency analysis exploits statistical properties of natural language
- Why short ciphertexts and non-standard text (no diacritics) break frequency analysis
- The difference between brute force and statistical cryptanalysis
- Why modern encryption (AES, RSA) replaced classical ciphers entirely
EOF