# DYATLOV PASS — THE SILENT EXPEDITION

A story-driven, seven-stage Capture The Flag (CTF) web application inspired by the 1959 Dyatlov Pass incident.

**Stack:** Python, Flask, Jinja2, HTML, CSS and JavaScript  
**Theme:** Classified investigation archive  
**Progression:** Seven sequential stages with server-side flag validation and session-based progress

> This repository contains the narrative web front end. FTP, SSH, Linux services and other VM-side challenge infrastructure are configured separately.

## Features

- Seven progressive investigation stages
- Server-side flag validation
- Session-based progress tracking
- Locked-stage handling and progress reset
- Downloadable challenge artifacts
- Story pages, recovered documents, timeline and radio archive

## Project structure

```text
dyatlov_ctf/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── templates/
└── static/
    ├── artifacts/
    ├── css/
    ├── images/
    └── js/
```

## Run locally

1. Install Python 3 and `python3-venv`.
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```powershell
   .venv\\Scripts\\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your local environment file:

   ```bash
   cp .env.example .env
   ```

   On Windows, copy `.env.example` to `.env` manually.

5. Edit `.env`. Set a long random `SECRET_KEY` and enter the seven flag answers from your private author copy. Do not commit `.env`.

6. Start the application:

   ```bash
   python app.py
   ```

7. Open http://127.0.0.1:5000

## Challenge areas

| Stage | Investigation |
|---|---|
| 1 | The Missing Expedition |
| 2 | The Last Diary Entry |
| 3 | The Forgotten Checkpoint |
| 4 | The Photograph That Should Not Exist |
| 5 | The Restricted Report |
| 6 | The Unidentified Frequency |
| 7 | The Final Truth |

## Deployment notes

This web application is only the story, clue and flag-submission front end. Configure any FTP, SSH, Linux permissions, privilege-escalation paths and supporting services separately on an isolated CTF VM.

For a production deployment, use a WSGI server such as Gunicorn behind a properly configured reverse proxy, use HTTPS, set `SESSION_COOKIE_SECURE=True`, and keep `.env` outside version control.

## Before publishing / running an event

- Replace the Stage 4 text placeholder with the intended photograph challenge artifact and test it.
- Verify that the Stage 6 audio decodes to the intended answer.
- Test all seven stages, including incorrect flags, locked stages, reset and artifact downloads.
- Keep author solutions and real flag values out of the public repository.
- Run the challenge only in an isolated, authorized lab environment.

## Disclaimer

This is a fictional CTF narrative inspired by the historical Dyatlov Pass incident. The challenge's invented evidence is for educational gameplay and is not presented as new historical evidence or a solution to the real incident.
