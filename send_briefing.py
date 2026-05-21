"""
Cybersecurity Briefing - Invio settimanale
Invia ogni giovedì mattina il diario Word aggiornato via Gmail.
Le credenziali vengono lette dai GitHub Secrets:
  GMAIL_USER    - indirizzo Gmail mittente
  GMAIL_APP_PASS - App Password Gmail (16 caratteri)
  EMAIL_TO      - destinatario
"""

import smtplib
import ssl
import os
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ─── CONFIGURAZIONE ────────────────────────────────────────────────────────
GMAIL_USER  = os.environ["GMAIL_USER"]
GMAIL_PASS  = os.environ["GMAIL_APP_PASS"]
EMAIL_TO    = os.environ["EMAIL_TO"]

DOCX_PATH   = "diario-cybersecurity-2026.docx"
# ───────────────────────────────────────────────────────────────────────────

oggi     = datetime.date.today()
settimana = oggi.isocalendar()[1]
anno     = oggi.year

SUBJECT = f"🔐 Cybersecurity Briefing — W{settimana}/{anno}"

HTML_BODY = f"""
<html><body style="font-family:Calibri,Arial,sans-serif;color:#1a1a1a;max-width:600px;margin:auto">
<div style="background:#1F4E79;padding:20px 28px;border-radius:6px 6px 0 0">
  <h1 style="color:#fff;margin:0;font-size:20px">🔐 Cybersecurity Briefing</h1>
  <p style="color:#BDD7EE;margin:4px 0 0">W{settimana}/{anno} · Enterprise &amp; Mid-market</p>
</div>
<div style="border:1px solid #DEEAF1;border-top:none;padding:20px 28px;border-radius:0 0 6px 6px">
  <p>Ciao Marco,</p>
  <p>in allegato il diario settimanale di cybersecurity aggiornato con le <strong>3 soluzioni più rilevanti della settimana W{settimana}/{anno}</strong>.</p>
  <p>Ambiti coperti:</p>
  <ul>
    <li>Endpoint &amp; Identity (EDR/XDR, PAM, Zero Trust)</li>
    <li>Cloud &amp; Infrastructure Security (CNAPP, CSPM, CWPP)</li>
    <li>AI &amp; Threat Intelligence (SIEM/SOAR next-gen, threat hunting)</li>
    <li>OT/IoT &amp; Infrastrutture Critiche</li>
    <li>Network Security &amp; Microsegmentazione (ZTNA, SASE)</li>
  </ul>
  <p>Buona lettura.</p>
</div>
<p style="font-size:11px;color:#aaa;text-align:center;margin-top:16px">
  Generato automaticamente da Claude · Cowork · 
  <a href="https://github.com/Pakalino/cybersecurity-briefing" style="color:#4472C4">github.com/Pakalino/cybersecurity-briefing</a>
</p>
</body></html>
"""

def send():
    msg = MIMEMultipart("mixed")
    msg["From"]    = GMAIL_USER
    msg["To"]      = EMAIL_TO
    msg["Subject"] = SUBJECT

    msg.attach(MIMEText(HTML_BODY, "html", "utf-8"))

    # Allega il diario Word
    with open(DOCX_PATH, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    filename = f"diario-cybersecurity-{anno}.docx"
    part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
    msg.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, EMAIL_TO, msg.as_string())
    print(f"✅ Email inviata a {EMAIL_TO} — W{settimana}/{anno}")

if __name__ == "__main__":
    send()
