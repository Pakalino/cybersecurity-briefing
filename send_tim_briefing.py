import smtplib, ssl, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASS = os.environ["GMAIL_APP_PASS"]
EMAIL_TO = "taglientim@yahoo.it"
today = date.today().strftime("%d %B %Y")
SUBJECT = f"Briefing settimanale TIM S.p.A. - {today}"

HTML_BODY = """
<html><body style="font-family:Arial,sans-serif;color:#1a1a1a;max-width:680px;margin:auto">
<div style="background:#003366;padding:20px 28px;border-radius:6px 6px 0 0">
<h1 style="color:#fff;margin:0;font-size:20px">Briefing settimanale TIM S.p.A.</h1>
<p style="color:#BDD7EE;margin:4px 0 0">Settimana del 2 giugno 2026</p>
</div>
<div style="border:1px solid #DEEAF1;border-top:none;padding:20px 28px">

<h2 style="color:#003366">1. Notizie Principali</h2>
<p>La settimana e' dominata dall'avanzamento dell'<b>OPA totalitaria di Poste Italiane su TIM</b>: il 28 maggio il documento d'offerta e' stato illustrato al CdA di TIM, che ha gia' nominato advisor indipendenti. L'offerta vale circa <b>10,8 miliardi di euro</b>, mira al delisting e al controllo statale maggioritario (Stato + CDP oltre il 50%). TIM ha avviato una prima tranche di <b>buyback</b> su 140 milioni di azioni e ha anticipato al <b>29 luglio 2026</b> il nuovo piano industriale al 2028.</p>

<h2 style="color:#003366">2. Andamento Finanziario (TIT.MI)</h2>
<ul>
<li><b>Quotazione</b> al 1 giugno 2026: ~0,732 EUR (+0,47% nella seduta)</li>
<li><b>Performance YTD 2026:</b> +41,85%</li>
<li><b>Performance 12 mesi:</b> +85,7%</li>
<li><b>Max 2026:</b> 0,7312 EUR (26 maggio) - <b>Min 2026:</b> 0,5052 EUR (2 gennaio)</li>
<li><b>Consensus:</b> 7 Buy, 0 Sell - target medio 12m: 0,6217 EUR</li>
<li><b>Azionariato:</b> Poste al 20,1% (da 27,3% a dic 2025); Morgan Stanley al 3,09%</li>
</ul>

<h2 style="color:#003366">3. Risultati Q1 2026</h2>
<p>Ricavi organici: <b>3,32 mld EUR</b> (+1,4% YoY). EBITDA After Lease: 794M EUR (-2,7%). Risultato netto: -292M EUR (vs -124M Q1 2025). Rallentamento legato alla transizione MVNO. Guidance 2026 confermata.</p>

<h2 style="color:#003366">4. Scenari Strategici e M&A</h2>
<p><b>OPA Poste Italiane:</b> 0,635 EUR/azione (0,167 EUR cash + 0,0218 azioni Poste), premio 9,01%. Gruppo combinato: ricavi ~26,9 MLD EUR, EBIT ~4,8 MLD EUR, 150k+ dipendenti. Completamento previsto entro fine 2026.</p>
<p><b>FiberCop/KKR:</b> 1 MLD EUR da Ares Management per riacquisto centrali. Debito rinegoziato con estensione 2 anni, risparmio ~75M EUR. Sotto indagine Commissione UE.</p>

<h2 style="color:#003366">5. Regolatorio e Normativo</h2>
<p><b>AGCM:</b> Istruttoria formale su accordo RAN Sharing TIM/Fastweb+Vodafone (avviata aprile 2026, conclusione attesa aprile 2027).</p>
<p><b>Commissione UE:</b> Indagine formale su KKR/FiberCop per dichiarazioni durante acquisizione NetCo.</p>

<h2 style="color:#003366">6. Prodotti e Mercato</h2>
<p>Dal <b>7 giugno 2026</b>: aumenti offerte mobili ricaricabili +1,99-2,99 EUR/mese. TIMVISION +1-4 EUR/mese da giugno. Recesso gratuito entro 9 giugno (tel. 119). Accordo RAN Sharing con Fastweb+Vodafone per 5G nelle aree rurali.</p>

<h2 style="color:#003366">7. Management e Governance</h2>
<p>AD <b>Pietro Labriola</b>: "Il business digitale e' una questione di scala." Il <b>29 luglio</b> e' la data chiave: risultati H1 2026 + piano industriale 2026-2028.</p>

<h2 style="color:#003366">Prospettive per la Settimana</h2>
<ol>
<li>OPA Poste: attesa fairness opinion CdA TIM</li>
<li>Rimodulazione mobile: entra in vigore il 7 giugno</li>
<li>FiberCop: aggiornamenti su debito e indagine UE</li>
<li>RAN Sharing: sviluppi istruttoria AGCM</li>
<li>Titolo sopra target medio analisti: possibile consolidamento</li>
</ol>

<p style="font-size:11px;color:#aaa;text-align:center;margin-top:24px">
Fonti: MilanoFinanza, Soldionline, Bloomberg, GruppoTIM.it, Borsa Italiana, AGCOM, AGCM<br/>
Generato automaticamente da Claude - Cowork - 2 giugno 2026
</p>
</div></body></html>
"""

msg = MIMEMultipart("alternative")
msg["From"] = GMAIL_USER
msg["To"] = EMAIL_TO
msg["Subject"] = SUBJECT
msg.attach(MIMEText(HTML_BODY, "html", "utf-8"))

ctx = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as s:
    s.login(GMAIL_USER, GMAIL_PASS)
    s.sendmail(GMAIL_USER, EMAIL_TO, msg.as_string())
print("Email inviata a " + EMAIL_TO)
