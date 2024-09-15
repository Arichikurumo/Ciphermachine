# Ciphermachine
Ciphermachine is a collection of cipheralgorithms implemented in Python. It is a commandline tool which allows the user to finetune the needs using flags (e.g. -a or --algorithm) to specify arguments.

## Usage
```
python main.py -a {algorithm of your choice} -t {string you want to encrypt/decrypt} -d {OPTIONAL - Use to decrypt instead of encrypt} -s {OPTIONAL - shift of chars for certain algorithms like caesar}
```
### Examples

```
python main.py -a rot13 -t "Hello World!"

python main.py -a caesar -t "Olssv Dvysk!" -s 7 -d
```

## Supported Algorithms
- [x] ROT13
- [X] Ceasar Cipher
- [ ] Enigma Machine

