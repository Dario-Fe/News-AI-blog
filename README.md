# AITalk: Static Site Engine & Content Repository

[![Deployment Status](https://img.shields.io/github/actions/workflow/status/darioferrero/aitalk/deploy.yml?branch=main&label=Deploy)](https://github.com/darioferrero/aitalk/actions)
[![Technology](https://img.shields.io/badge/Engine-Python%20SSG-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Netlify-00ad9f.svg)](https://www.netlify.com/)

AITalk is a professional, high-performance static site generator (SSG) specifically engineered for multi-language news portals focused on Artificial Intelligence. This repository contains the complete source code, automation scripts, and Markdown-based content database.

---

## 🚀 Key Features

### ⚡ Performance & Architecture
- **Pure Python SSG**: Customized build engine (`build.py`) designed for maximum speed and minimal overhead.
- **Atomic Incremental Builds**: Intelligent change detection using SHA-1 hashing ensures only modified content is re-processed.
- **Parallel Processing**: Utilizes `ProcessPoolExecutor` for high-speed HTML generation across multiple CPU cores.

### 🌐 Multilingual Excellence
- **Native Support**: Full localized experiences for **Italian**, **English**, **Spanish**, **French**, and **German**.
- **Live Search**: Integrated high-speed, client-side search engine with language-aware filtering and dynamic path resolution.
- **SEO Optimized**: Language-specific RSS feeds, automated robots.txt generation, and proper OpenGraph/Twitter metadata for every page.

### 🎙️ Multimedia & Engagement
- **Podcast Integration**: Automated detection and integration of language-specific audio (`.mp3`) with a native HTML5 player.
- **YouTube Embedding**: Seamless support for video content within articles.
- **E-Book Engine**: Specialized scripts to compile Markdown articles into professionally formatted PDF/EPUB e-books.
- **Newsletter Automation**: Serverless newsletter subscription system via Netlify Forms.

### 📊 Analytics & Insights
- **Privacy-First Tracking**: Lightweight, cookie-less page view tracking via Netlify Functions and Netlify Blobs.
- **Performance Dashboards**: Real-time statistics monitoring without third-party trackers.

---

## 📂 Project Structure

```text
├── articoli/           # Primary content database (Markdown + Media)
├── content/            # Auxiliary data (Author biographies, profiles)
├── ebook/              # E-book generation suite (Python + CSS)
├── netlify/            # Serverless functions (Stats, Analytics)
├── pages/              # Static informational pages (Legal, Cookies, Method)
├── templates/          # HTML blueprints (Base, Article, Author, 404)
├── public/             # Static assets (Flags, icons, logos)
├── build.py            # Core SSG Engine
├── build.sh            # Global build automation
└── style.css           # Global design system
```

---

## 🛠️ Development Workflow

### Prerequisites
- **Python 3.10+**
- **pip** (Python Package Manager)

### Local Environment Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Build System
- **Full Build (All Languages)**:
  ```bash
  ./build.sh
  ```
- **Targeted Build**:
  ```bash
  python build.py --lang [it|en|es|fr|de]
  ```

### Local Preview
Launch a local development server to inspect the generated site in `dist/`:
```bash
cd dist
python -m http.server 8000
```
Access the portal at: `http://localhost:8000`

---

## 📝 Content Management

### Articles
Every article resides in its own directory within `articoli/`, identified by a numeric prefix for chronological sorting (e.g., `105-slug/`).
- **Translations**: Suffix files with language codes (e.g., `article_en.md`).
- **Media**: Place images and audio files directly in the article folder. The engine handles optimization and format conversion (WebP/JPEG) automatically.

### Authors
Manage author profiles in `content/authors/`. Biographical data supports full Markdown formatting.

---

## ☁️ Deployment & CI/CD
The portal is continuously deployed via **GitHub Actions**. Every push to the main branch triggers an automated build and deployment to **Netlify**. The workflow utilizes advanced caching strategies to ensure rapid deployment times.

---
© 2025 AITalk - Curated by **Dario Ferrero**
