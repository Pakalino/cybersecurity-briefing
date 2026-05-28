import smtplib, ssl, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_PASS = os.environ["GMAIL_APP_PASS"]
EMAIL_TO = "taglientim@yahoo.it"
SUBJECT = "Briefing settimanale TIM S.p.A. - 28 maggio 2026"

HTML_BODY = """
<html><body style="font-family:Arial,sans-serif;color:#1a1a1a;max-width:680px;margin:auto">
<div style="background:#003366;padding:20px 28px;border-radius:6px 6px 0 0">
<h1 style="color:#fff;margin:0;font-size:20px">Briefing settimanale TIM S.p.A.</h1>
<p style="color:#BDD7EE;margin:4px 0 0">Settimana del 28 maggio 2026</p>
</div>
<div style="border:1px solid #DEEAF1;border-top:none;padding:20px 28px">
<h2 style="color:#003366">1. Notizie Principali</h2>
<p>La settimana e' dominata da due grandi temi: il completamento della conversione delle azioni di risparmio
in ordinarie (93,5% convertite volontariamente, effettiva dal 21 maggio) e l'avanzamento dell'OPA totalitaria
di Poste Italiane su TIM. Il titolo TIT.MI ha toccato il massimo annuale di 0,7312 euro il 26 maggio
(+85,7% YTD). Moody's ha migliorato il rating a Ba1 (outlook stabile) l'11 maggio.</p>

<h2 style="color:#003366">2. Andamento Finanziario (TIT.MI)</h2>
<p>Prezzo max settimana: 0,7312 euro (26 mag, massimo annuale 2026). Prezzo 20 mag: 0,7246 euro (+1,14%).
Min. annuale: 0,5052 euro (2 gen 2026). Performance YTD: +85,7%.
Rating Moody's: Ba1 (upgrade da Ba2, 11 mag 2026).
Buyback 2026: prima tranche max 140 mln azioni (~100 mln euro) entro dic 2026.</p>

<h2 style="color:#003366">3. Risultati Ufficiali Q1 2026</h2>
<p>CdA del 6 maggio ha approvato i risultati al 31 marzo 2026.
Ricavi organici: 3,32 mld euro (+1,4% YoY). Domestico: 2,2 mld euro (-0,9%). Brasile: 1,1 mld euro (+6,4%).
EBITDA: 964 mln euro (-1,7%). EBITDA After Lease: 794 mln euro (-2,7%).
Risultato netto: -292 mln euro (vs -124 mln Q1 2025). Indebitamento netto AL: 7,3 mld euro (leva inferiore a 2x).
Guidance 2026 confermata dall'AD Labriola. Rallentamento parzialmente dovuto al cambio MVNO sulla rete TIM.</p>

<h2 style="color:#003366">4. Scenari Strategici e M&A</h2>
<p><b>OPA Poste Italiane:</b> Lanciata il 22 marzo 2026 per ~10,8 mld euro.
Poste e' al 20,1% del capitale ordinario TIM dopo la conversione delle savings shares (era 27,3% a dic 2025).
Gruppo combinato: ricavi ~26,9 mld euro, EBIT ~4,8 mld euro, 150k+ dipendenti.
Sinergie: ~0,7 mld euro/anno a regime. OPA valida al 66,67% di adesione (obiettivo: delisting TIM).
CdA TIM ha nominato advisor. Quota statale post-OPA scenderebbe al ~50%.
Morgan Stanley scesa al 3,09% (dal 6,26% di marzo).</p>
<p><b>FiberCop / KKR:</b> Q1 2026 con ricavi 888 mln euro e EBITDA AL 391 mln euro, in linea con guidance
(+10% EBITDAaL annuale). Rollout FTTH a 14,6 mln unita' (72% target 2027).
KKR rinegozia debito da 10,5 mld euro, estensione 2 anni, risparmio ~75 mln euro.
KKR avvia ricerca nuovo AD per FiberCop. MEF valuta eventuale riacquisto della rete (rumors).</p>

<h2 style="color:#003366">5. Regolatorio e Normativo</h2>
<p>AGCOM Delibera 58/26/CONS: nuovi rimedi per accesso rete fissa, applicazione scaglionata feb e mag 2026.
AGCM ha espresso preoccupazioni su clausole MSA FiberCop-TIM.
Per il 2026 previsti oltre 30 adempimenti periodici per operatori TLC.</p>

<h2 style="color:#003366">6. Prodotti, Mercato e Concorrenza</h2>
<p>Rimodulazioni TIM: rete fissa +2,99 euro/mese da maggio (precedenti: fino a +5 euro/mese da febbraio).
Mobile: nuova rimodulazione dal 7 giugno (+2,99 euro/mese per ricaricabili).
TIMVISION: aumenti 1-4 euro/mese da giugno. Recesso gratuito entro 9 giugno 2026.
Fastweb e WindTre applicano aumenti simili; Iliad mantiene prezzi fissi.
INWIT: TIM ha presentato piano uscita in 10 anni (8.500 torri terzi + 6.000 nuove + 6.000 in JV).
Disdetta MSA inviata il 29 marzo (scadenza agosto 2030). INWIT contesta, ricorso cautelare in corso.</p>

<h2 style="color:#003366">7. Gruppo TIM</h2>
<p><b>TIM Brasil (TIMS3):</b> Ricavi netti Q1 2026: BRL 6,8 mld (+6,5% YoY).
EBITDA normalizzato: BRL 3,28 mld (margine 48,3%). Postpaid +7,5%, B2B IoT +30%.
Partnership PicPay (financial services), Brasileirao e Rock in Rio.
EPS sotto le stime per maggiori costi operativi.</p>
<p><b>FiberCop e INWIT:</b> vedi sezioni 4 e 6.</p>

<h2 style="color:#003366">8. Management e Governance</h2>
<p>AD Pietro Labriola: quarto anno consecutivo di target raggiunti, il meglio deve ancora avvenire.
Capital Market Day rinviato a H2 2026 per definire perimetro sinergie con Poste.
Nel 2027 previsti 500 mln euro di dividendi. Sinergie con Poste: ~50 mln euro margini aggiuntivi (non nel 2026).
Conversione savings shares completata come da piano.</p>

<h2 style="color:#003366">Prospettive Settimana 1-6 Giugno 2026</h2>
<ol>
<li>OPA Poste: attesa fairness opinion dal CdA TIM e aggiornamenti dagli advisor</li>
<li>Rimodulazione mobile: entra in vigore il 7 giugno, possibili reazioni AGCOM</li>
<li>INWIT: sviluppi sul ricorso cautelare contro la disdetta MSA</li>
<li>FiberCop: aggiornamenti su rinegoziazione debito e fusione Open Fiber</li>
<li>Capital Market Day TIM: il mercato attende il nuovo piano industriale</li>
</ol>
<p style="font-size:11px;color:#aaa;text-align:center">Generato automaticamente da Claude - Cowork - 28 maggio 2026</p>
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
