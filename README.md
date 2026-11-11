<div align="center">
  <img src="./assets/header.svg" width="100%" alt="Dmytro Murza: a red GT car driving an alpine pass at sunset" />

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-15121a?style=for-the-badge&logo=github&logoColor=ffffff)](https://github.com/d-murza)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-15121a?style=for-the-badge&logo=linkedin&logoColor=ffffff)](https://www.linkedin.com/in/dmytro-murza)
[![Email](https://img.shields.io/badge/Email-15121a?style=for-the-badge&logo=gmail&logoColor=ffffff)](mailto:dmytro.murza.work@gmail.com)
![Location](https://img.shields.io/badge/Konstanz,_Germany-15121a?style=for-the-badge&logo=googlemaps&logoColor=e10600)
![Profile views](https://komarev.com/ghpvc/?username=d-murza&color=e10600&style=for-the-badge&label=PIT+STOPS)

</div>

---

## 🏁 Driver Profile

I'm a **software engineer** and **Computer Science Master's student at the University of Konstanz**. I started on the systems side: as R&D team lead I built a high-frequency **crypto trading terminal in C#/.NET** used by 2,000+ customers, and I added distributed tracing to cloud video encoding services at **Bitmovin**. Now I'm adding **machine learning** to that: multimodal RAG, LLM fine-tuning and vision foundation models.

I like building complete systems end to end, from the model or the concurrency model down to the API, the UI, and the bug that only appears under load.

Off the keyboard, I'm a car person. Hence the circuit below.

```yaml
driver:
  name:       Dmytro Murza
  team:       M.Sc. Computer Science @ University of Konstanz
  previously: B.Sc. Computer Science @ Constructor University
  engine:     [C# / .NET, Python, PyTorch, TypeScript, C / C++, Java]
  specialty:  [Concurrent & real-time systems, Backend, Multimodal RAG, LLM fine-tuning]
  languages:  { English: C1, German: B1 }
  setup:      "Simplify, then add lightness."
  off_track:  cars, motorsport, and anything with a well-tuned engine
```

---

## 🏎️ Race History · Experience

- 📈 **R&D Engineer (Team Lead)** · VPMF Technologies OÜ, Tallinn · *09/2023 – 08/2026*
  Built a WPF trading terminal (C#/.NET) for high-frequency crypto trading that integrates 6 exchanges (Binance, Bybit, OKX, …) and has 2,000+ customers. Built parallel data ingestion with async/await, concurrent collections and producer/consumer pipelines. Hunted down memory leaks, deadlocks and race conditions using dumps and regression tests. Led a team of 3 engineers in Agile sprints. Product overview videos (in Russian) are on the [ProfitForge YouTube channel](https://www.youtube.com/@ProfitForgeOfficial).
- 🎬 **Software Engineering Intern** · Bitmovin, Berlin · *06/2024 – 08/2024*
  Added OpenTelemetry distributed tracing across cloud video encoding services, with trace context propagated through the HTTP pipeline. Worked in C++, Java and Kotlin, and tested with Google Test and JUnit. Monitored services in Kibana and verified encoding output with FFmpeg and MP4Box.
- 🧑‍🏫 **Teaching Assistant: Operating Systems** and **Digital Systems & Computer Architecture** · Constructor University · *2024 – 2025*
  Mentored 100+ students in concurrency, scheduling, synchronization, memory management, Verilog and CPU fundamentals.
- 🎓 **Academic project: Concurrency and data synchronization in real-time financial applications** · Constructor University · *05/2025* · grade 1.0
  Compared thread-based and task-based concurrency models for low-latency trading, and evaluated synchronization primitives and concurrent collections.

---

## 🏆 Podium · Featured Builds

| | Build | What it does | Under the hood |
|:-:|:--|:--|:--|
| 🔎 | **[Multimodal RAG Assistant](https://github.com/d-murza/multimodal-rag-assistant)** | Answers "how do I…?" questions: retrieves WikiHow articles, generates grounded steps with a local LLM, and matches each step to a HowTo100M video clip. | `RAG` `FAISS` `CLIP` `TinyLlama` `Gradio` |
| 🧬 | **[Qwen3 Patent Classifier](https://github.com/d-murza/qwen3-patent-classifier)** | LoRA fine-tuning of Qwen3-0.6B with completion-only loss masking; raises patent IPC classification F1 from 0.05 to 0.44 on a single T4. | `PEFT` `LoRA` `Transformers` |
| 👁️ | **[Vision Foundation Models](https://github.com/d-murza/vision-foundation-models)** | Zero-label anomaly detection with DINOv2 patch features (0.98 mean AUROC on MVTec-AD), plus segmentation and monocular depth. | `DINOv2` `SegFormer` `Depth Anything` |
| 🗓️ | **[PlanIt](https://github.com/d-murza/PlanIt_WebApp)** | Schedule desktop automations from the web: .NET microservices push triggered plans over RabbitMQ and SignalR to an Electron client. | `.NET` `RabbitMQ` `SignalR` `React` `Docker` |
| 🌐 | **[InvestBud Podillia](https://investbud-podillia.com.ua/)** | Production website for a Ukrainian construction company: bilingual, project portfolio with city filters, interactive map, lead form. | `Web` `Vite` `Leaflet` |
| 🧪 | **[Machine Learning Labs](https://github.com/d-murza/machine-learning-labs)** | Transformers and ViTs written from scratch, autoencoders vs. VAEs, DINOv2 image search, T5 vs. TinyLlama. | `PyTorch` `Transformers` |
| 🔌 | **[TCP Word Game Server](https://github.com/d-murza/tcp-word-game-server)** | Multiplayer game server in C: single-threaded libevent loop, non-blocking IPv4/IPv6 sockets. | `C` `libevent` `sockets` |

---

## 🔧 The Garage · Tech Stack

<div align="center">

**Languages**

![C#](https://img.shields.io/badge/C%23-15121a?style=for-the-badge&logo=dotnet&logoColor=ffcf6b)
![Python](https://img.shields.io/badge/Python-15121a?style=for-the-badge&logo=python&logoColor=ffcf6b)
![TypeScript](https://img.shields.io/badge/TypeScript-15121a?style=for-the-badge&logo=typescript&logoColor=ffcf6b)
![C++](https://img.shields.io/badge/C%2B%2B-15121a?style=for-the-badge&logo=cplusplus&logoColor=ffcf6b)
![C](https://img.shields.io/badge/C-15121a?style=for-the-badge&logo=c&logoColor=ffcf6b)
![Java](https://img.shields.io/badge/Java-15121a?style=for-the-badge&logo=openjdk&logoColor=ffcf6b)
![SQL](https://img.shields.io/badge/SQL-15121a?style=for-the-badge&logo=postgresql&logoColor=ffcf6b)

**Backend & Desktop**

![.NET](https://img.shields.io/badge/ASP.NET_Core-15121a?style=for-the-badge&logo=dotnet&logoColor=ff8a3d)
![WPF](https://img.shields.io/badge/WPF-15121a?style=for-the-badge&logo=windows&logoColor=ff8a3d)
![React](https://img.shields.io/badge/React-15121a?style=for-the-badge&logo=react&logoColor=ff8a3d)
![Electron](https://img.shields.io/badge/Electron-15121a?style=for-the-badge&logo=electron&logoColor=ff8a3d)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-15121a?style=for-the-badge&logo=rabbitmq&logoColor=ff8a3d)
![Redis](https://img.shields.io/badge/Redis-15121a?style=for-the-badge&logo=redis&logoColor=ff8a3d)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15121a?style=for-the-badge&logo=postgresql&logoColor=ff8a3d)
![SQL Server](https://img.shields.io/badge/SQL_Server-15121a?style=for-the-badge&logo=microsoftsqlserver&logoColor=ff8a3d)

**Machine Learning**

![PyTorch](https://img.shields.io/badge/PyTorch-15121a?style=for-the-badge&logo=pytorch&logoColor=e10600)
![Hugging Face](https://img.shields.io/badge/Transformers-15121a?style=for-the-badge&logo=huggingface&logoColor=e10600)
![PEFT](https://img.shields.io/badge/PEFT_·_LoRA-15121a?style=for-the-badge&logo=huggingface&logoColor=e10600)
![FAISS](https://img.shields.io/badge/FAISS-15121a?style=for-the-badge&logo=meta&logoColor=e10600)
![scikit-learn](https://img.shields.io/badge/scikit--learn-15121a?style=for-the-badge&logo=scikitlearn&logoColor=e10600)
![Gradio](https://img.shields.io/badge/Gradio-15121a?style=for-the-badge&logo=gradio&logoColor=e10600)

**Infrastructure, Observability & Tooling**

![Docker](https://img.shields.io/badge/Docker-15121a?style=for-the-badge&logo=docker&logoColor=ffffff)
![AWS](https://img.shields.io/badge/AWS_S3_·_SQS-15121a?style=for-the-badge&logo=amazonwebservices&logoColor=ffffff)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-15121a?style=for-the-badge&logo=opentelemetry&logoColor=ffffff)
![Kibana](https://img.shields.io/badge/Kibana-15121a?style=for-the-badge&logo=kibana&logoColor=ffffff)
![TeamCity](https://img.shields.io/badge/TeamCity-15121a?style=for-the-badge&logo=teamcity&logoColor=ffffff)
![Linux](https://img.shields.io/badge/Linux-15121a?style=for-the-badge&logo=linux&logoColor=ffffff)
![Git](https://img.shields.io/badge/Git-15121a?style=for-the-badge&logo=git&logoColor=ffffff)
![Jira](https://img.shields.io/badge/Jira-15121a?style=for-the-badge&logo=jira&logoColor=ffffff)

</div>

---

## 📈 Telemetry · Contribution Circuit

<div align="center">
  <img
    src="https://raw.githubusercontent.com/d-murza/d-murza/output/contribution-circuit.svg"
    width="100%"
    alt="My last 12 months of GitHub contributions drawn as kerb blocks around an animated race track, with a live stats panel"
  />
  <sub>Every kerb block is a day of the year. The car laps the track, and busy days light up as it passes. Rebuilt daily by a GitHub Action.</sub>
</div>

<br/>

<div align="center"><sub>🏁 Thanks for stopping by the pit lane.</sub></div>
