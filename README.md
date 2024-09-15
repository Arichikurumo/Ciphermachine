# Ciphermachine

## Objective
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

### Supported Algorithms
- [x] ROT13
- [X] Ceasar Cipher
- [ ] Enigma Machine

## Skills Learned
[Bullet Points - Remove this afterwards]

- Advanced understanding of SIEM concepts and practical application.
- Proficiency in analyzing and interpreting network logs.
- Ability to generate and recognize attack signatures and patterns.
- Enhanced knowledge of network protocols and security vulnerabilities.
- Development of critical thinking and problem-solving skills in cybersecurity.

## Tools Used
[Bullet Points - Remove this afterwards]

- Security Information and Event Management (SIEM) system for log ingestion and analysis.
- Network analysis tools (such as Wireshark) for capturing and examining network traffic.
- Telemetry generation tools to create realistic network traffic and attack scenarios.
