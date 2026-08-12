---
tags: ["Generative AI", "Applications", "Security"]
date: 2026-07-10
author: "Dario Ferrero"
---

# I taught AI to stand guard: how I built a zero-cost security system
![sistema-sicurezza-ai.jpg](sistema-sicurezza-ai.jpg)

*In the TV series 'Person of Interest', a superintelligence nicknamed simply "the Machine" monitors every corner of the planet through cameras, microphones, and sensors of all kinds, identifying threats before they materialize. It's science fiction, of course. But the underlying idea—using computer vision to understand what's happening in an environment—is now accessible to anyone with a PC and a webcam. Less than 250 lines of code. No subscription, no cloud, no video traveling the world. Just a notification on your phone, with a photo, when someone enters the house.*

The question I asked myself a few weeks ago was simple: how much does a security system cost that alerts you in real time if someone enters your home, sends you a photo, and runs entirely locally without depending on a monthly subscription? The answer: zero euros. Only hardware that you most likely already own. In this article, I tell how I built that system, what I learned along the way, and why the experiment says something bigger about the way artificial intelligence is changing the relationship between technology and daily life.

## Before pointing it at home: the test at Times Square

Every security system worthy of the name must be tested before being put into production. But pointing a webcam at my room without having verified its operation in challenging conditions seemed naive. So I decided to start with the most chaotic context I could find without moving from my chair: Times Square, New York, seen from above through one of the many public webcams accessible in streaming.

The scenario was deliberately extreme. Hundreds of people crossing paths, yellow taxis, buses, delivery trucks, all in simultaneous movement, with sudden light variations and difficult angles. The kind of situation that puts any mediocre visual recognition system in crisis.

The result was surprising: the system recognized up to nine vehicles simultaneously among cars, buses, and trucks, identified pedestrians even at a considerable distance, maintained a stable 40 frames per second, all on a CPU, without touching the GPU. *"If it works on Times Square, it works anywhere,"* I told myself. And so it was.
![timesquare.jpg](timesquare.jpg)
*Screenshot of the tests done on the Times Square webcam.*

## The heart of the system: YOLO explained simply

Before getting to the moment when the phone vibrated with the first alarm photo, it's worth spending a few lines on what happens under the hood, because the technology involved is genuinely fascinating even if viewed from afar.

The central component is called [YOLO](https://github.com/ultralytics/ultralytics), an acronym for *You Only Look Once*. The name isn't marketing: it describes exactly how it works. Traditional visual recognition systems analyzed an image in multiple steps, first identifying regions of interest and then classifying them. YOLO flips the approach: it analyzes the entire image in a single pass, dividing it into a grid and simultaneously predicting the position and type of object for each cell. The result is significantly higher speed, with accuracy that has reached excellent levels on recent versions.

The version I used, YOLOv8n, is the lightest variant of the family. The "n" suffix stands for *nano*, and it's designed explicitly to run on limited hardware. It's trained on the COCO dataset, which includes eighty categories of objects: people, vehicles, pets, furniture. For my purposes, the only category I'm interested in is "person," with a confidence threshold set at 0.4, meaning the model signals a presence only when it's at least forty percent sure it has detected it. A lower threshold produces more false alarms, a higher one risks missing real detections.

The second crucial ingredient is [ONNX](https://onnxruntime.ai/), which stands for *Open Neural Network Exchange*. It's an open format for representing machine learning models, but above all, it's an optimized inference engine that knows how to make the best use of the specific instructions of each processor. When you export YOLOv8n to ONNX format, the model goes from 10-15 frames per second to 40-45 frames per second on the same CPU, without changing a single line of application code. The file goes from 6 MB to 12 MB, but the speed gain is nearly fourfold. It's like having a simultaneous translator who perfectly knows your processor's dialect.

## GINA lends me the bot

Those who follow this portal will remember [GINA, my personal voice assistant](https://aitalk.it/it/gina-assistente-vocale.html). For real-time notifications, I had already built a Telegram bot integrated into the GINA ecosystem, capable of sending me messages, updates, and alerts directly to my smartphone. Reusing that infrastructure for the security system was natural: a classic example of how pieces of a technological ecosystem built over time start to fit together in ways not always foreseen.

The Telegram bot does only one thing, but it does it well: when the system detects a person, it receives an HTTP call with a text message and a photo of the offending frame, and delivers them to my phone in two to five seconds. No proprietary app, no account on cloud video surveillance platforms, no data crossing third-party servers other than Telegram's servers for the final delivery of the notification. Alternatively, one could think of sending an email. The video itself never leaves the PC.

The bot configuration takes about five minutes: it's created via [@BotFather](https://core.telegram.org/bots) on Telegram, an authentication token is obtained, your chat ID is retrieved by sending a message to the bot and querying the APIs, and the two strings are inserted into the configuration file. After that, the notification channel is operational.

## The moment of truth: my room

Having passed the New York test, it was time to point the webcam at the environment that really mattered: my room. I positioned the camera, started the script, waited for the five seconds of stabilization that the system takes at startup to avoid generating false alarms during loading, and left the room.

Then I came back.

The phone vibrated even before I reached the center of the frame. The message read: *"🚨 SECURITY ALARM! People detected: 1. Time: 13:43:07. Alarm #1"*. Below, a photo with my outline highlighted by a box and a red overlay at the top of the frame. Latency from entry to notification: less than a second for recognition, two-three seconds for Telegram delivery.

It worked.

The system has a built-in false alarm protection logic: a ten-second cooldown between one alarm and the next prevents a person standing in the frame from generating dozens of notifications per minute. The 0.4 confidence threshold proved well-calibrated for a home environment: no false positives during testing, no missed recognitions in normal light conditions. With poor lighting, performance degrades, but it's a physical limit of the webcam even before the model.
![allarme.jpg](allarme.jpg)
*Screenshot of the alarm message on Telegram, as well as the most unlikely thief in the history of crime.*

## How it's built: the technical recipe

The complete code takes less than 250 lines of Python. The structure is linear and understandable even for those who don't write code professionally. There are four logical blocks: the initial configuration with Telegram tokens and threshold parameters, the functions for sending messages and photos via Telegram API, the person detection function that queries ONNX, and the main loop that acquires frames from the webcam, analyzes them, and manages the alarm logic.

The dependencies are five standard Python libraries in the machine learning ecosystem: `ultralytics` to load YOLO, `onnxruntime` for optimized inference, `opencv-python` for webcam management and frame processing, and `requests` for HTTP calls to Telegram.

The final project structure is essential: a main Python file, the 12 MB ONNX model, and a configuration file. In all, less than 15-20 MB on disk.

On the performance front, the numbers speak clearly:
![tabella.jpg](tabella.jpg)

The hardware used is an AMD Ryzen 7 7700 with 32 GB of RAM, but tests on less powerful configurations confirm that the system works without problems even on a laptop with a fifth or sixth generation Intel i5 processor and 8 GB of RAM. The GPU is never involved.

## Where it makes sense to use it and where not

A system of this type works well in specific contexts, and it's honest to state it clearly. For home security in an apartment or a small house, it is effective: it monitors a room or an entrance, alerts in real time, costs zero. For monitoring an office during night closing, a shop after closing hours, or a warehouse with limited access, the system lends itself equally well.

However, it's not a substitute for a professional security system certified for critical environments. False negatives exist, especially in difficult lighting conditions. The system doesn't distinguish between those who have house keys and a real intruder, at least in the basic version. It doesn't record video, only photos of the alarm moments. And it runs on a PC that must be on and connected to the Internet for notifications.

On the legal front, it's worth remembering that in Italy, video surveillance is regulated by the GDPR and the Privacy Guarantor. For exclusively domestic use, within one's own private property, the restrictions are significantly less burdensome than for public or working environments. If the camera captures common spaces or shared external areas, signage obligations and, in some cases, notification to the Guarantor come into play. The guiding principle is simple: informing people that the area is monitored is always the correct choice, not just the legal one.
![log.jpg](log.jpg)
*Screenshot of the terminal with the system in operation, with object recognition and the alarm at the moment of a person's entry.*

## The roads ahead

The project in its current form is a working starting point, not a destination. Natural extensions are diverse, with increasing complexity.

The most obvious next step is facial recognition to distinguish residents from strangers. Python's `face_recognition` library allows building an archive of known faces and filtering alarms accordingly: if it's me entering the house, no notification. If it's someone the system has never seen, alarm. The additional code is just a few dozen lines.

Integration with passive PIR sensors, the classic infrared motion sensors, would allow activating YOLO only in the presence of movement, drastically reducing energy consumption during periods of inactivity. In the current implementation, the webcam runs and the model analyzes frames continuously, even when the room has been empty for hours.

Multi-camera support would require instantiating multiple parallel processes, one for each webcam, with a centralized alarm management system. A lightweight web dashboard built with Flask or FastAPI would allow viewing the system status remotely. All extensions achievable with a few days of work.

## Local wins (almost always)

Every time I build something of this type, I find myself grappling with a broader question: why do it locally when cloud APIs for computer vision exist that work with three lines of code?

The answer isn't ideological. It's practical.

As I've discussed in other contexts on this portal, local models have reached a level of maturity that makes the choice between local and cloud genuinely dependent on the use case, not on the automatic assumption that the cloud is always superior. For a home video surveillance system, the advantages of local are hard to beat: images of your home never leave your PC, there are no variable costs, the system works even without Internet once configured, and there is no dependence on third-party pricing policies that can change.

The cloud wins in different scenarios: when dozens of cameras are needed, when local computing power is insufficient, when the required models are too large to run locally, or when infrastructure maintenance is an unsustainable burden. But for a home experiment like this, the cloud would have been overhead without concrete benefits.

There is, however, a consideration that is always worth making explicit: ONNX and YOLOv8n are mature, documented tools with active communities. It's not black magic reserved for specialists. It's applied engineering that anyone with curiosity and a few hours to spare can replicate. This is perhaps the most significant thing about the entire experiment: not the security system itself, but the demonstration that the distance between "AI technology" and "thing that works on my PC" has shortened to the point of becoming almost irrelevant.

---

*The code is available on the [GitHub Security-System-Yolo](https://github.com/Dario-Fe/Security-System-Yolo) repository*
