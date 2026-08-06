
1. What is Multiprocessing?
A process is an independent program with its own memory space.

Unlike threads , processes do not share memory by default.

Example:
CPU
│
├── Process 1
├── Process 2
├── Process 3
└── Process 4

Each process can run on a different CPU core.

2. Thread vs Process

    Feature         Thread              Process
    Memory          Shared              sequence
    Best for        I/O-bound tasks     Slightly heavier
    Example         Downloading files   Image processing encryption

Rule of Thumb:
-- Use threading for network requests , API and file I/O
-- Use multiprocessing for calculations, encryption, compression, and hasing