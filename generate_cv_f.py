#!/usr/bin/env python3
"""
Academic CV Website Generator — Meghna P. Bhaugeerutty
Run:    python3 generate_cv.py
Output: index.html
Features: sidebar nav · mobile responsive · light/dark theme · email obfuscation · favicon
"""

# ─────────────────────────────────────────────
#   EDIT YOUR CONTENT HERE
# ─────────────────────────────────────────────

PROFILE = {
    "name": "Meghna P. Bhaugeerutty",
    "title": "PhD Candidate · Quantitative Researcher",
    "institution": "Université Paris Dauphine – PSL × Amundi",
    "email": "meghna.bhaugeerutty@dauphine.psl.eu",
    "github": "https://github.com/meghna-pb",
    "linkedin": "https://www.linkedin.com/in/meghna-bhaugeerutty/",
    "location": "Paris, France",
    "tagline": (
        "PhD candidate at Université Paris Dauphine – PSL and Amundi (CIFRE), "
        "researching allocation biases in Net Zero investing, physical climate risk, "
        "and quantitative portfolio management."
    ),
    "about": [
        "I am a PhD candidate in Economics at Université Paris Dauphine - PSL, "
        "in partnership with Amundi Investment Solutions (CIFRE). My doctoral research, co-supervised "
        "by Yannick Le Pen (LEDa-CGEMP) and Thierry Roncalli (Amundi Research Institute), "
        "focuses on allocation biases in Net Zero passive investing "
        "and the integration of physical climate risk in portfolio management.",

        "I hold an MSc in Economic and Financial Engineering (Quantitative Finance) from Université Paris Dauphine - PSL "
        "and a Double BSc in Applied Economics "
        "from Université Paris Dauphine – PSL and Goethe Universität Frankfurt. My academic work "
        "spans sustainable finance, ESG methodologies, "
        "and financial econometrics.",

        "Prior to my PhD, I worked as a Quantitative Analyst in ESG Research at Société Générale "
        "Investment Solutions, where I designed proprietary ESG scoring models and built a "
        "Net Zero commitment dashboard. I also interned at ING Wholesale Banking in Frankfurt, "
        "focusing on sustainable finance transactions and ESG client analysis.",
    ],
    "cv_url": None, #"cv_052026.pdf",  # Place cv.pdf in your repo root (same folder as index.html)
    "photo": "photo.JPG",  # Uncomment and set to your photo filename in repo root
}

EDUCATION = [
    {
        "degree": "PhD in Economics",
        "institution": "Université Paris Dauphine – PSL",
        "grade": None,
        "city": "Paris, France",
        "years": "2024 – 2027 (Scheduled)",
        "text": (
            "CIFRE partnership with Amundi Investment Solutions. "
            "Laboratoire d'Economie de Dauphine (LEDa-CGEMP)."
        ),
        "items": [
            "Supervisors: Yannick Le Pen (Dauphine) & Thierry Roncalli (Amundi Research Institute)",
            "Research on allocation biases in Net Zero passive investing",
            "Physical climate risk integration in portfolio management",
        ],
    },
    {
        "degree": "MSc in Economic and Financial Engineering – Quantitative Finance (272)",
        "institution": "Université Paris Dauphine – PSL",
        "grade": None, #"Mention Bien",
        "city": "Paris, France",
        "years": "2022 – 2024",
        "text": "Specialisation in quantitative methods applied to asset management and derivatives.",
        "items": [
            "Courses: Quantitative Asset Management, NLP & Machine Learning, Stochastic Calculus, Derivative Instruments, Econometrics",
            "M2 Thesis: <em>Analysis of current trends in decarbonisation</em> — 18.66/20",
            "M1 Thesis: <em>SRI label on fund financial performance & ESG breakdown</em> — 16/20",
        ],
    },
    {
        "degree": "Double BSc in Applied Economics",
        "institution": "Université Paris Dauphine – PSL & Goethe Universität Frankfurt",
        "grade": None,
        "city": "Paris & Frankfurt",
        "years": "2019 – 2022",
        "text": "Exchange year at Goethe Universität Frankfurt (2021–2022). Minor in Psychology.",
        "items": [
            "Courses: Economics, Mathematics, Statistics & Probability, Python & VBA, Accounting, Law, Social Sciences",
            "Thesis: <em>Selecting Key Performance Indicators for Sustainability-linked Products</em> — 1.0 (highest grade)",
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Quantitative Researcher — Environmental Quant Solutions",
        "org": "Amundi Investment Solutions",
        "years": "2024 – 2027",
        "location": "Paris, France",
        "bullets": [
            "CIFRE PhD project on Net Zero investing allocation biases and physical climate risk integration in portfolios.",
            "Estimated carbon emissions of projects financed by green bonds.",
            "Analysed the impact of mining activities on deforestation.",
        ],
    },
    {
        "role": "Quantitative Analyst — ESG Research",
        "org": "Société Générale Investment Solutions",
        "years": "2022 – 2024",
        "location": "Paris, France",
        "bullets": [
            "Designed and implemented proprietary ESG scoring methodologies using quantitative models.",
            "Built a dashboard to model the evolution of Net Zero commitments, with scenario and carbon trend analysis of AuM.",
            "Developed tools in Python and VBA for ESG data processing and reporting.",
        ],
    },
    {
        "role": "Sustainable Finance Intern",
        "org": "ING Wholesale Banking",
        "years": "Mar – Aug 2022",
        "location": "Frankfurt, Germany",
        "bullets": [
            "Conducted ESG analysis of potential clients and supported the team in transaction execution and client pitches.",
            "Researched ESG sector trends and regulatory requirements; produced sustainable finance market updates.",
            "Maintained data quality for the Sustainable Finance team.",
        ],
    },
    {
        "role": "President, Dauphine Model United Nations",
        "org": "Université Paris Dauphine – PSL",
        "years": "2020 – 2021",
        "location": "Paris, France",
        "bullets": [
            "'Honourable Mention' at Assas MUN (Dec 2019); participated in 10+ international conferences including Harvard NMUN 2022.",
            "Designed and coded the association website (layout, front-end development).",
        ],
    },
]

PUBLICATIONS = [
    {
        "type": "Working Paper",
        "title": "Beyond Decarbonisation: Disentangling Allocation Biases and Global Reallocation in Net Zero Passive Investing",
        "authors": "Bhaugeerutty, M.",
        "venue": "Working paper",
        "year": "2025",
        "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5958135",
        "abstract": ("This paper examines allocation biases arising from the simultaneous integration of carbon reduction targets"
                    " and the financing of climate solutions within passive portfolio management (Net Zero portfolios). "
                    " Using MSCI European Monetary Union, World, Emerging Markets and All Country World indices for 2022-2024, "
                    " we identify pronounced sectoral divergences: Financials are significantly overweighted when portfolios "
                    " prioritise carbon intensity reduction but underweighted when green revenue share is emphasised; "
                    " Utilities and Industrials show the opposite pattern. Pursuing both objectives concurrently produces a "
                    " considerable positive allocation bias to real estate and raises tracking error, though not prohibitively. "
                    " Geographically, India is underinvested in green revenues, while China receives the largest positive allocation bias. "
                    " The United States and India are underweighted across scenarios, reflecting many large and mid-cap firms "
                    " that are neither carbon-efficient nor major providers of green revenues despite substantial national green investment. "
                    " Europe is consistently overweighted, reflecting more advanced decarbonisation and green investment. "
                    " The results reveal the complex, often counter-intuitive relationship between decarbonisation and "
                    " climate solutions and underscore that neither objective can be forgone-both should be targeted concurrently. "
                    " Situated within a Total Portfolio Approach, the study stresses the need to integrate diverse asset classes "
                    " to meet financial and sustainability goals and offers actionable insights for investors and policymakers. "            
        ),
    },
    {
        "type": "Work in Progress",
        "title": "Climate Black-Litterman: physical risk integration in portfolio management",
        "authors": "Bhaugeerutty, M.",
        "venue": "Working paper",
        "year": "2026",
        "url": None,
        "abstract": ("Despite the accelerating frequency of natural catastrophes and the risk of climate tipping points, "
                      "physical climate risk remains scarcely incorporated into portfolio construction. "
                      "This paper proposes two practical methods to reduce physical risk exposure in active portfolios "
                      "by introducing a flexible penalty function that scales with a firm’s physical risk exposure, "
                      "and includes a tunable attention parameter representing investor sensitivity to such risks. "
                      "The penalty function is intentionally generalisable and can be applied to other extra‑financial "
                      "risk metrics (for example biodiversity loss, water stress or pollution). In the first approach, "
                      "expected risk premia are directly discounted by the penalty prior to optimisation; in the second, "
                      "the adjusted premia are incorporated as subjective views within a Climate Black–Litterman (C‑BL) framework. "
                      "Empirical application demonstrates that both methods significantly lower portfolio exposure to physical risk "
                      "while mostly preserving conventional financial performance. Nonetheless, the calibration of the attention "
                      "parameter exposes a clear trade-off relationship between financial returns and reduced exposure to physical "
                      "risks, bearing critical implications for policymakers and practitioners. The analysis further shows that physical "
                      "risks are unevenly distributed worldwide, reinforcing the urgency for firms and governments to act to reduce "
                      "exposure and avoid cascading effects. Overall, this paper provides a methodological framework for integrating "
                      "physical risk into portfolio decisions, contingent on improvements in data quality and availability, as well as regulatory guidance."       
 ),
    },
    {
        "type": "Work in Progress",
        "title": "Impact of external shocks on agricultural commodities futures",
        "authors": "Bhaugeerutty, M. & Sekine, T.",
        "venue": "Working paper",
        "year": "2026",
        "url": None,
        "abstract": (
            "This paper investigates how exogenous shocks — including natural disasters and "
            "geopolitical tensions — propagate through agricultural commodity futures markets. "
            "Using high-frequency futures data and an event-study approach, we estimate the "
            "magnitude, persistence, and cross-commodity spillovers of supply disruptions, "
            "with a focus on staple crops exposed to climate-related tail risks."
        ),
    },
]

CONFERENCES = [
    {
        "title": "Beyond Decarbonisation: Disentangling Allocation Biases and Global Reallocation in Net Zero Passive Investing",
        "events": [
            {
                "name": "5th ARAE Annual Workshop",
                "location": "Marseille (AMSE)",
                "year": "2025",
                "role": "Presenter",
            },
            {
                "name": "4th Sustainable Finance Research Forum",
                "location": "Paris (emlyon)",
                "year": "2025",
                "role": "Presenter",
            },
        ],
    }, 
]

RESEARCH = [
    {
        "area": "Net Zero Investing",
        "icon": "N",
        "description": (
            "Allocation biases in passive Net Zero strategies: disentangling sectoral "
            "and geographical reallocation, and evaluating their implications "
            "for index construction and portfolio performance."
        ),
    },
    {
        "area": "Physical Climate Risk",
        "icon": "C",
        "description": (
            "Integration of physical climate risk (flood, heat stress, sea-level rise) "
            "in portfolio management frameworks, asset pricing, and risk assessment."
        ),
    },
    {
        "area": "Commodities & Physical Risk",
        "icon": "K",
        "description": (
            "Evaluation of the impact of external shocks (natural disasters, geopolitical tensions) "
            "on the pricing of agricultural commodities."
        ),
    },
    {
        "area": "ESG & Sustainable Finance",
        "icon": "E",
        "description": (
            "Quantitative ESG scoring methodologies, SRI label analysis, green bond "
            "carbon accounting, and the financial materiality of sustainability factors."
        ),
    },
    {
        "area": "Quantitative Asset Management",
        "icon": "Q",
        "description": (
            "Factor investing, portfolio optimisation under ESG constraints, "
            "machine learning for return prediction, and scenario analysis for decarbonisation pathways."
        ),
    },
]
# ─────────────────────────────────────────────
#   GENERATOR  (no need to edit below)
# ─────────────────────────────────────────────

FAVICON_B64 = (
    "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+"
    "CiAgPHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjMyIiByeD0iNiIgZmlsbD0iIzBEMkI0NSIvPgogIDx0"
    "ZXh0IHg9IjE2IiB5PSIyMiIgZm9udC1mYW1pbHk9Ikdlb3JnaWEsc2VyaWYiIGZvbnQtc2l6ZT0iMTgi"
    "IGZvbnQtd2VpZ2h0PSJib2xkIgogICAgZmlsbD0iIzRBQUFGMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+"
    "TTwvdGV4dD4KPC9zdmc+"
)

def badge(text, color_class):
    classes = {
        "wp": "badge-wp", "cp": "badge-cp", "wip": "badge-wip",
        "presenter": "badge-wp", "discussant": "badge-wip",
    }
    return f'<span class="badge {classes.get(color_class, "badge-wp")}">{text}</span>'

def pub_badge(ptype):
    if ptype == "Working Paper":      return badge("Working Paper", "wp")
    elif ptype == "Conference Paper": return badge("Conference", "cp")
    else:                             return badge("In Progress", "wip")

def conf_role_badge(role):
    return badge(role, "presenter" if role.lower() == "presenter" else "discussant")

def timeline_icon(color="blue"):
    if color == "green":
        return """<div class="tl-icon tl-green">
          <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
            <rect x="2" y="4" width="11" height="9" rx="2" fill="#3B6D11" opacity="0.7"/>
            <path d="M5 4V3a2 2 0 0 1 4 0v1" stroke="#3B6D11" stroke-width="1.2"
              stroke-linecap="round" fill="none"/>
          </svg></div>"""
    return """<div class="tl-icon tl-blue">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M8 2L14 5.5V10.5L8 14L2 10.5V5.5L8 2Z" fill="#378ADD" opacity="0.7"/>
      </svg></div>"""

def education_html():
    items = []
    for i, edu in enumerate(EDUCATION):
        connector = "" if i == len(EDUCATION) - 1 else '<div class="tl-connector"></div>'
        grade_badge = (
            f'<span class="edu-grade">{edu["grade"]}</span>' if edu.get("grade") else ""
        )
        city_line = (
            f'<span class="tl-city">{edu["city"]}</span>' if edu.get("city") else ""
        )
        text_block = (
            f'<p class="tl-detail">{edu["text"]}</p>' if edu.get("text") else ""
        )
        list_block = ""
        if edu.get("items"):
            lis = "".join(f'<li class="edu-item">{it}</li>' for it in edu["items"])
            list_block = f'<ul class="edu-list">{lis}</ul>'

        items.append(f"""
        <div class="tl-row">
          <div class="tl-left">
            {timeline_icon("blue")}
          </div>
          <div class="tl-body">
            <div class="tl-header">
              <p class="tl-title">{edu['degree']}</p>
              <span class="tl-year">{edu['years']}</span>
            </div>
            <p class="tl-org">{edu['institution']}{(' ' + grade_badge) if grade_badge else ''} &mdash; <span class="tl-loc">{edu.get('city', '')}</span></p>
            {text_block}
            {list_block}
          </div>
        </div>
        {connector}
        """)
    return "\n".join(items)

def experience_html():
    items = []
    for i, exp in enumerate(EXPERIENCE):
        connector = "" if i == len(EXPERIENCE) - 1 else '<div class="tl-connector tl-connector-green"></div>'
        bullets_html = "".join(f'<li class="exp-bullet">{b}</li>' for b in exp["bullets"])
        items.append(f"""
        <div class="tl-row">
          <div class="tl-left">{timeline_icon("green")}</div>
          <div class="tl-body">
            <div class="tl-header">
              <p class="tl-title">{exp['role']}</p>
              <span class="tl-year">{exp['years']}</span>
            </div>
            <p class="tl-org">{exp['org']} &mdash; <span class="tl-loc">{exp['location']}</span></p>
            <ul class="exp-list">{bullets_html}</ul>
          </div>
        </div>
        {connector}
        """)
    return "\n".join(items)

def research_html():
    cards = []
    for r in RESEARCH:
        cards.append(f"""
        <div class="research-card">
          <div class="research-icon">{r['icon']}</div>
          <p class="research-area">{r['area']}</p>
          <p class="research-desc">{r['description']}</p>
        </div>
        """)
    return "\n".join(cards)

def publications_html():
    items = []
    for idx, pub in enumerate(PUBLICATIONS):
        uid = f"pub-{idx}"
        link_open  = f'<a href="{pub["url"]}" target="_blank" class="pub-link">' if pub.get("url") else ""
        link_close = "</a>" if pub.get("url") else ""
        arrow = (
            '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" class="pub-arrow">'
            '<path d="M2 11L11 2M11 2H5M11 2V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
        ) if pub.get("url") else ""
        abstract_block = ""
        if pub.get("abstract"):
            abstract_block = f"""
            <div class="pub-abstract-wrap" id="{uid}-abstract">
              <p class="pub-abstract">{pub['abstract']}</p>
            </div>
            <button class="abstract-toggle" onclick="toggleAbstract('{uid}')" aria-expanded="false">
              <span class="abstract-toggle-label">Abstract</span>
              <svg class="abstract-chevron" width="12" height="12" viewBox="0 0 12 12" fill="none">
                <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
              </svg>
            </button>"""
        items.append(f"""
        <div class="pub-item" id="{uid}">
          <div class="pub-meta">{pub_badge(pub['type'])}<span class="pub-year">{pub['year']}</span></div>
          <p class="pub-title">{link_open}{pub['title']}{arrow}{link_close}</p>
          <p class="pub-authors">{pub['authors']}</p>
          <p class="pub-venue">{pub['venue']}</p>
          {abstract_block}
        </div>
        """)
    return "\n".join(items)

def conferences_html():
    items = []
    for paper in CONFERENCES:
        events_html = ""
        for ev in paper["events"]:
            events_html += f"""
            <div class="conf-event">
              <div class="conf-event-left">
                <span class="conf-name">{ev['name']}</span>
                <span class="conf-loc"> &mdash; {ev['location']}</span>
              </div>
              <div class="conf-event-right">
                {conf_role_badge(ev['role'])}
                <span class="pub-year">{ev['year']}</span>
              </div>
            </div>"""
        items.append(f"""
        <div class="conf-item">
          <p class="conf-title">"{paper['title']}"</p>
          {events_html}
        </div>
        """)
    return "\n".join(items)

def about_paragraphs():
    return "\n".join(f'<p class="about-p">{p}</p>' for p in PROFILE["about"])

def encode_email(email):
    encoded = "".join(f"&#{ord(c)};" for c in email)
    return f'<a href="&#{ord("m")};ailto:{encoded}" class="sidebar-contact-link">{encoded}</a>'

NAV_ITEMS = [
    ("about",        "About"),
    ("education",    "Education"),
    ("experience",   "Experience"),
    ("publications", "Publications"),
    ("conferences",  "Conferences"),
    ("research",     "Research"),
]

def nav_links():
    return "\n".join(
        f'<a href="#{sid}" class="nav-link" data-section="{sid}">'
        f'<span class="nav-dot"></span>{label}</a>'
        for sid, label in NAV_ITEMS
    )

def mobile_nav_links():
    return "\n".join(
        f'<a href="#{sid}" class="mob-nav-link" onclick="closeMobileMenu()">{label}</a>'
        for sid, label in NAV_ITEMS
    )

def generate_html():
    edu_html   = education_html()
    exp_html   = experience_html()
    res_html   = research_html()
    pub_html   = publications_html()
    conf_html  = conferences_html()
    about_ps   = about_paragraphs()
    nav_html   = nav_links()
    mob_html   = mobile_nav_links()
    initials   = "".join(w[0].upper() for w in PROFILE["name"].split()[:2])
    email_html = encode_email(PROFILE["email"])
    photo_src = PROFILE.get("photo", "")
    if photo_src:
        photo_tag = f'<img src="{photo_src}" alt="{PROFILE["name"]}">' 
    else:
        photo_tag = initials

    gh_link = (
        f'<a href="{PROFILE["github"]}" target="_blank" class="social-link">GitHub</a>'
        if PROFILE.get("github") else ""
    )
    li_link = (
        f'<a href="{PROFILE["linkedin"]}" target="_blank" class="social-link">LinkedIn</a>'
        if PROFILE.get("linkedin") else ""
    )
    social = " &middot; ".join(filter(None, [gh_link, li_link]))

    # Mobile drawer contact icons
    mob_contact_items = []
    if PROFILE.get("email"):
        enc = "".join(f"&#{ord(c)};" for c in PROFILE["email"])
        mob_contact_items.append(
            f'<a href="&#{ord("m")};ailto:{enc}" class="mob-contact-link" title="Email">'
            f'<svg width="18" height="18" viewBox="0 0 16 16" fill="none">'
            f'<rect x="1" y="3" width="14" height="10" rx="2" stroke="currentColor" stroke-width="1.3"/>'
            f'<path d="M1 5l7 5 7-5" stroke="currentColor" stroke-width="1.3"/></svg></a>'
        )
    if PROFILE.get("github"):
        mob_contact_items.append(
            f'<a href="{PROFILE["github"]}" target="_blank" class="mob-contact-link" title="GitHub">'
            f'<svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor">'
            f'<path d="M8 0C3.58 0 0 3.58 0 8a8 8 0 005.47 7.59c.4.07.55-.17.55-.38v-1.34C3.73 14.3 '
            f'3.27 12.9 3.27 12.9c-.36-.92-.88-1.16-.88-1.16-.72-.49.05-.48.05-.48.8.06 1.22.82 '
            f'1.22.82.71 1.21 1.86.86 2.31.66.07-.52.28-.86.5-1.06-1.78-.2-3.64-.89-3.64-3.95 '
            f'0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.62 7.62 0 014 '
            f'0c1.53-1.03 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07'
            f'-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48v2.19c0 .21.15.46.55.38A8 8 0 0016 8c0-4.42-3.58-8-8-8z"/>'
            f'</svg></a>'
        )
    if PROFILE.get("linkedin"):
        mob_contact_items.append(
            f'<a href="{PROFILE["linkedin"]}" target="_blank" class="mob-contact-link" title="LinkedIn">'
            f'<svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor">'
            f'<path d="M0 1.15C0 .51.52 0 1.16 0h13.68C15.48 0 16 .51 16 1.15v13.7c0 .63-.52 '
            f'1.15-1.16 1.15H1.16C.52 16 0 15.49 0 14.85V1.15zM4.8 13.5V6.17H2.4v7.33h2.4zM3.6 '
            f'5.17a1.4 1.4 0 100-2.8 1.4 1.4 0 000 2.8zM13.5 13.5V9.5c0-2.13-.46-3.77-2.95-3.77'
            f'-1.2 0-2 .66-2.33 1.28h-.03V6.17H5.87V13.5h2.4v-3.57c0-1.03.2-2.03 1.47-2.03 '
            f'1.26 0 1.28 1.18 1.28 2.1V13.5h2.48z"/>'
            f'</svg></a>'
        )
    mob_contact_html = (
        f'<div class="mob-contact-row">{"".join(mob_contact_items)}</div>'
        if mob_contact_items else ""
    )

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{PROFILE['name']} – Academic CV</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,{FAVICON_B64}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>

:root, [data-theme="light"] {{
  --c-bg:           #F4F8FD;
  --c-surface:      #FFFFFF;
  --c-sidebar-from: #0D2B45;
  --c-sidebar-to:   #0A253E;
  --c-sidebar-mid:  #103557;
  --c-navy:         #0D2B45;
  --c-blue:         #185FA5;
  --c-mid:          #378ADD;
  --c-pale:         #E6F1FB;
  --c-border:       #C8DFF2;
  --c-muted:        #5a7080;
  --c-text:         #334e60;
  --c-detail:       #5a7080;
  --c-tl-blue-bg:   #E6F1FB;
  --c-tl-blue-br:   #85B7EB;
  --c-tl-green-bg:  #EAF3DE;
  --c-tl-green-br:  #97C459;
  --c-tl-conn:      #B5D4F4;
  --c-tl-conn-g:    #C8DFF2;
  --c-card-hover:   rgba(55,138,221,0.10);
  --c-pub-border:   #85B7EB;
  --c-conf-border:  #9FE1CB;
  --c-conf-ev:      #EEF4FA;
  --c-mob-bg:       #0D2B45;
  --c-mob-link:     #E6F1FB;
  --c-mob-overlay:  rgba(10,30,50,0.55);
  --c-topbar:       #FFFFFF;
  --c-topbar-br:    #C8DFF2;
  --badge-wp-bg:    #E6F1FB; --badge-wp-fg: #185FA5;
  --badge-cp-bg:    #E1F5EE; --badge-cp-fg: #0F6E56;
  --badge-wip-bg:   #FAEEDA; --badge-wip-fg:#854F0B;
  --c-abstract-bg:  #F0F7FF;
  --c-abstract-br:  #C8DFF2;
  --c-edu-grade-bg: #EAF3DE; --c-edu-grade-fg: #2a6020;
}}

[data-theme="dark"] {{
  --c-bg:           #0f1923;
  --c-surface:      #172231;
  --c-sidebar-from: #091420;
  --c-sidebar-to:   #060e18;
  --c-sidebar-mid:  #0c1c2e;
  --c-navy:         #d0e8ff;
  --c-blue:         #5fb3f5;
  --c-mid:          #4AAAF0;
  --c-pale:         #162840;
  --c-border:       #1e3a55;
  --c-muted:        #8aadcc;
  --c-text:         #a8c8e2;
  --c-detail:       #7a9ab5;
  --c-tl-blue-bg:   #162840;
  --c-tl-blue-br:   #2a5a8a;
  --c-tl-green-bg:  #12261a;
  --c-tl-green-br:  #2a5a3a;
  --c-tl-conn:      #1e3a55;
  --c-tl-conn-g:    #1e3a55;
  --c-card-hover:   rgba(74,170,240,0.08);
  --c-pub-border:   #2a5a8a;
  --c-conf-border:  #1a4a38;
  --c-conf-ev:      #111e2d;
  --c-mob-bg:       #091420;
  --c-mob-link:     #c8e4ff;
  --c-mob-overlay:  rgba(0,0,0,0.72);
  --c-topbar:       #111e2d;
  --c-topbar-br:    #1e3a55;
  --badge-wp-bg:    #162840; --badge-wp-fg: #5fb3f5;
  --badge-cp-bg:    #0e2418; --badge-cp-fg: #4db88a;
  --badge-wip-bg:   #271b09; --badge-wip-fg:#e0a052;
  --c-abstract-bg:  #111e2d;
  --c-abstract-br:  #1e3a55;
  --c-edu-grade-bg: #12261a; --c-edu-grade-fg: #6fbc6f;
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'Inter', sans-serif;
  background: var(--c-bg);
  color: var(--c-navy);
  min-height: 100vh;
  display: flex;
  transition: background 0.25s, color 0.25s;
}}

/* SIDEBAR */
#sidebar {{
  width: 272px;
  min-height: 100vh;
  background: linear-gradient(180deg, var(--c-sidebar-from) 0%, var(--c-sidebar-mid) 60%, var(--c-sidebar-to) 100%);
  position: fixed; top: 0; left: 0;
  display: flex; flex-direction: column;
  padding: 36px 0 28px;
  z-index: 200; overflow-y: auto;
  transition: background 0.25s;
}}
.avatar {{
  width: 86px; height: 86px; border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 14px;
  border: 3px solid rgba(181,212,244,0.35);
  flex-shrink: 0;
  background: linear-gradient(135deg, #4AAAF0, #1866B4);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Crimson Pro', serif;
  font-size: 26px; font-weight: 600; color: #fff;
}}
.avatar img {{
  width: 100%; height: 100%;
  object-fit: cover; object-position: center top;
  display: block;
}}
.sidebar-name {{
  font-family: 'Crimson Pro', serif;
  font-size: 17px; font-weight: 600;
  color: #E8F2FF; text-align: center;
  padding: 0 18px; line-height: 1.35; letter-spacing: 0.01em;
}}
.sidebar-title {{
  font-family: 'Inter', sans-serif;
  font-size: 10px; color: #7aaed4;
  text-align: center; padding: 7px 18px 0;
  line-height: 1.7; letter-spacing: 0.06em;
  text-transform: uppercase; font-weight: 500;
}}
.sidebar-divider {{
  height: 1px; background: rgba(181,212,244,0.15);
  margin: 18px 22px; flex-shrink: 0;
}}
.theme-toggle {{
  display: flex; align-items: center;
  justify-content: center; gap: 8px; padding: 0 20px 4px;
}}
.theme-label {{
  font-size: 10.5px; color: #6a9dc0;
  user-select: none; font-family: 'Inter', sans-serif;
  letter-spacing: 0.04em; text-transform: uppercase;
}}
.toggle-track {{
  width: 36px; height: 20px;
  background: rgba(181,212,244,0.2); border-radius: 10px;
  position: relative; cursor: pointer;
  transition: background 0.25s;
  border: 1px solid rgba(181,212,244,0.25); flex-shrink: 0;
}}
.toggle-track.on {{ background: rgba(74,170,240,0.45); }}
.toggle-thumb {{
  width: 14px; height: 14px; background: #fff;
  border-radius: 50%; position: absolute;
  top: 2px; left: 2px; transition: transform 0.22s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}}
.toggle-track.on .toggle-thumb {{ transform: translateX(16px); }}
nav {{ margin-top: 4px; }}
.nav-link {{
  display: flex; align-items: center; gap: 10px;
  padding: 9px 22px;
  font-family: 'Inter', sans-serif;
  font-size: 11px; font-weight: 600;
  color: #85b8d8; text-decoration: none;
  border-left: 3px solid transparent;
  transition: all 0.18s;
  letter-spacing: 0.08em; text-transform: uppercase;
}}
.nav-link:hover, .nav-link.active {{
  color: #E8F2FF;
  background: rgba(181,212,244,0.09);
  border-left-color: #4AAAF0;
}}
.nav-dot {{
  width: 4px; height: 4px; border-radius: 50%;
  background: currentColor; opacity: 0.4; flex-shrink: 0;
}}
.sidebar-contact {{
  margin-top: auto; padding: 0 22px;
  font-size: 10.5px; color: #5e96be;
  line-height: 2.2; flex-shrink: 0;
  font-family: 'Inter', sans-serif;
}}
.sidebar-contact-link, .social-link {{
  color: #7aaed4; text-decoration: none; transition: color 0.15s;
}}
.sidebar-contact-link:hover, .social-link:hover {{ color: #B5D4F4; }}

/* MOBILE TOPBAR */
#topbar {{
  display: none; position: fixed;
  top: 0; left: 0; right: 0; height: 54px;
  background: var(--c-topbar);
  border-bottom: 1px solid var(--c-topbar-br);
  z-index: 300; align-items: center;
  justify-content: space-between; padding: 0 18px;
  transition: background 0.25s;
}}
.topbar-name {{
  font-family: 'Crimson Pro', serif;
  font-size: 16px; font-weight: 600; color: var(--c-navy);
}}
.topbar-right {{ display: flex; align-items: center; gap: 12px; }}
.topbar-toggle {{ display: flex; align-items: center; gap: 6px; cursor: pointer; }}
.topbar-toggle .toggle-track {{
  width: 32px; height: 18px;
  background: var(--c-border); border: 1px solid var(--c-border);
}}
.topbar-toggle .toggle-track.on {{ background: var(--c-mid); }}
.topbar-toggle .toggle-thumb {{ width: 12px; height: 12px; top: 2px; left: 2px; }}
.topbar-toggle .toggle-track.on .toggle-thumb {{ transform: translateX(14px); }}
.topbar-icon {{ font-size: 15px; line-height: 1; color: var(--c-muted); }}
#hamburger {{
  display: flex; flex-direction: column; gap: 5px;
  cursor: pointer; padding: 4px; background: none; border: none;
}}
.ham-bar {{
  width: 22px; height: 2px; background: var(--c-navy);
  border-radius: 2px; transition: all 0.25s;
}}

/* MOBILE DRAWER */
#mob-overlay {{
  display: none; position: fixed; inset: 0;
  background: var(--c-mob-overlay); z-index: 390;
}}
#mob-drawer {{
  position: fixed; top: 0; right: -100%;
  width: min(280px, 80vw); height: 100%;
  background: var(--c-mob-bg); z-index: 400;
  display: flex; flex-direction: column;
  padding: 64px 0 0;
  transition: right 0.28s cubic-bezier(.4,0,.2,1);
  overflow-y: auto;
}}
#mob-drawer.open {{ right: 0; }}
#mob-overlay.open {{ display: block; }}
.mob-nav-link {{
  display: block; padding: 13px 28px;
  font-family: 'Inter', sans-serif;
  font-size: 12px; font-weight: 600;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--c-mob-link); text-decoration: none;
  border-bottom: 1px solid rgba(181,212,244,0.07);
  transition: background 0.15s;
}}
.mob-nav-link:hover {{ background: rgba(181,212,244,0.07); }}
.mob-close {{
  position: absolute; top: 14px; right: 16px;
  background: none; border: none;
  font-size: 24px; color: #94c0e2; cursor: pointer; line-height: 1;
}}
.mob-contact-row {{
  margin-top: auto; padding: 20px 28px;
  display: flex; gap: 22px; align-items: center;
  border-top: 1px solid rgba(181,212,244,0.1);
}}
.mob-contact-link {{
  color: #7aaed4; text-decoration: none;
  display: flex; align-items: center; transition: color 0.15s;
}}
.mob-contact-link:hover {{ color: #B5D4F4; }}

/* MAIN */
#main {{
  margin-left: 272px; flex: 1;
  padding: 48px 54px 80px; max-width: 920px;
  transition: background 0.25s;
}}
.section {{ margin-bottom: 64px; scroll-margin-top: 32px; }}
.section-label {{
  font-size: 10px; font-weight: 600;
  letter-spacing: 0.14em; color: var(--c-mid);
  text-transform: uppercase; margin-bottom: 6px;
  font-family: 'Inter', sans-serif;
}}
.section-title {{
  font-family: 'Crimson Pro', serif;
  font-size: 28px; font-weight: 600;
  color: var(--c-navy); margin-bottom: 28px;
  padding-bottom: 14px; border-bottom: 2px solid var(--c-pale);
  transition: color 0.25s, border-color 0.25s; letter-spacing: -0.01em;
}}

/* HERO */
.hero-tag {{
  display: inline-block; background: var(--c-pale);
  color: var(--c-blue); font-size: 11.5px; font-weight: 500;
  padding: 4px 14px; border-radius: 20px;
  margin-bottom: 18px; border: 1px solid var(--c-border);
  letter-spacing: 0.02em; transition: background 0.25s, color 0.25s;
}}
.hero-name {{
  font-family: 'Crimson Pro', serif;
  font-size: 38px; font-weight: 600; color: var(--c-navy);
  line-height: 1.2; margin-bottom: 10px;
  transition: color 0.25s; letter-spacing: -0.01em;
}}
.hero-tagline {{
  color: var(--c-muted); line-height: 1.75; max-width: 560px;
  margin-bottom: 28px; font-style: italic;
  font-family: 'Crimson Pro', serif; font-size: 17px;
  transition: color 0.25s;
}}
.about-p {{
  margin: 0 0 14px; font-size: 14.5px;
  color: var(--c-text); line-height: 1.8; transition: color 0.25s;
  text-align: justify; hyphens: auto;
}}
.cv-btn {{
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--c-blue); color: #fff;
  font-size: 13px; font-weight: 500;
  padding: 10px 22px; border-radius: 8px;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  border: none; cursor: pointer; margin-top: 8px;
  font-family: 'Inter', sans-serif;
}}
.cv-btn:hover {{ background: var(--c-navy); transform: translateY(-1px); }}

/* TIMELINE */
.tl-row {{ display: flex; gap: 20px; align-items: flex-start; }}
.tl-left {{
  flex-shrink: 0; margin-top: 4px;
}}

.tl-icon {{
  width: 38px; height: 38px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}}
.tl-blue  {{ background: var(--c-tl-blue-bg); border: 2px solid var(--c-tl-blue-br); }}
.tl-green {{ background: var(--c-tl-green-bg); border: 2px solid var(--c-tl-green-br); }}
.tl-connector {{
  width: 2px; height: 30px;
  background: var(--c-tl-conn); margin: 0 0 0 18px;
}}
.tl-connector-green {{ background: var(--c-tl-conn-g); }}
.tl-body {{ padding-bottom: 10px; flex: 1; min-width: 0; }}
.tl-header {{
  display: flex; justify-content: space-between;
  align-items: baseline; flex-wrap: wrap; gap: 6px;
}}
.tl-title {{
  margin: 0; font-size: 15px; font-weight: 600;
  color: var(--c-navy); transition: color 0.25s;
  font-family: 'Inter', sans-serif;
}}
.tl-year {{
  font-size: 11.5px; color: var(--c-blue);
  white-space: nowrap; transition: color 0.25s;
  font-family: 'Inter', sans-serif; font-weight: 500;
  letter-spacing: 0.02em;
}}
.tl-org {{
  margin: 4px 0 6px; font-size: 13.5px;
  color: var(--c-blue); font-weight: 500;
  transition: color 0.25s; font-family: 'Inter', sans-serif;
  display: flex; align-items: center; flex-wrap: wrap; gap: 6px;
}}
.tl-loc {{ color: var(--c-muted); font-weight: 400; }}
.tl-detail {{
  margin: 0 0 8px; font-size: 13.5px;
  color: var(--c-detail); line-height: 1.6; transition: color 0.25s;
}}
.edu-list {{
  margin: 4px 0 0; padding-left: 18px; list-style-type: disc;
}}
.edu-item {{
  font-size: 13px; color: var(--c-detail);
  line-height: 1.7; margin-bottom: 5px; transition: color 0.25s;
}}
.edu-grade {{
  display: inline-block; font-size: 10.5px; font-weight: 600;
  background: var(--c-edu-grade-bg); color: var(--c-edu-grade-fg);
  padding: 2px 9px; border-radius: 20px; letter-spacing: 0.03em;
  font-family: 'Inter', sans-serif; vertical-align: middle;
  transition: background 0.25s, color 0.25s;
}}
.exp-list {{ margin: 4px 0 0; padding-left: 18px; list-style-type: disc; }}
.exp-bullet {{
  font-size: 13px; color: var(--c-detail);
  line-height: 1.65; margin-bottom: 4px; transition: color 0.25s;
}}

/* RESEARCH */
.research-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 16px;
}}
.research-card {{
  background: var(--c-surface); border: 1px solid var(--c-border);
  border-radius: 12px; padding: 20px 22px;
  transition: box-shadow 0.2s, background 0.25s, border-color 0.25s;
  cursor: default;
}}
.research-card:hover {{ box-shadow: 0 4px 18px var(--c-card-hover); }}
.research-icon {{
  width: 36px; height: 36px; border-radius: 10px;
  background: linear-gradient(135deg, #4AAAF0, #1866B4);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Crimson Pro', serif;
  font-weight: 600; font-size: 17px; color: #fff; margin-bottom: 10px;
}}
.research-area {{
  margin: 0 0 6px; font-size: 14px; font-weight: 600;
  color: var(--c-navy); transition: color 0.25s;
  font-family: 'Inter', sans-serif;
}}
.research-desc {{
  margin: 0; font-size: 13px;
  color: var(--c-detail); line-height: 1.65; transition: color 0.25s;
  text-align: justify; hyphens: auto;
}}

/* BADGES */
.badge {{
  display: inline-block; font-size: 10px; font-weight: 700;
  padding: 3px 10px; border-radius: 20px;
  letter-spacing: 0.06em; white-space: nowrap;
  font-family: 'Inter', sans-serif; text-transform: uppercase;
  transition: background 0.25s, color 0.25s;
}}
.badge-wp  {{ background: var(--badge-wp-bg);  color: var(--badge-wp-fg); }}
.badge-cp  {{ background: var(--badge-cp-bg);  color: var(--badge-cp-fg); }}
.badge-wip {{ background: var(--badge-wip-bg); color: var(--badge-wip-fg); }}

/* PUBLICATIONS */
.pub-item {{
  border-left: 3px solid var(--c-pub-border);
  padding: 16px 0 16px 22px; margin-bottom: 8px;
  transition: border-color 0.25s;
}}
.pub-meta {{
  display: flex; align-items: center;
  gap: 10px; margin-bottom: 8px; flex-wrap: wrap;
}}
.pub-year {{ font-size: 12px; color: var(--c-muted); font-family:'Inter',sans-serif; }}
.pub-title {{
  margin: 0 0 4px; font-size: 15px; font-weight: 600;
  color: var(--c-navy); line-height: 1.4;
  transition: color 0.25s; font-family: 'Inter', sans-serif;
}}
.pub-link {{ text-decoration: none; color: inherit; }}
.pub-link:hover {{ text-decoration: underline; text-underline-offset: 3px; }}
.pub-arrow {{ margin-left: 5px; vertical-align: middle; color: var(--c-mid); }}
.pub-authors {{ margin: 0 0 2px; font-size: 13px; color: var(--c-blue); transition: color 0.25s; font-family:'Inter',sans-serif; }}
.pub-venue   {{ margin: 0 0 10px; font-size: 12px; color: var(--c-muted); font-style: italic; font-family:'Inter',sans-serif; }}
.abstract-toggle {{
  display: inline-flex; align-items: center; gap: 5px;
  background: none; border: 1px solid var(--c-border);
  border-radius: 6px; padding: 4px 10px;
  font-size: 11px; font-weight: 600;
  color: var(--c-blue); cursor: pointer;
  font-family: 'Inter', sans-serif;
  transition: background 0.15s, color 0.15s, border-color 0.25s;
  letter-spacing: 0.04em; text-transform: uppercase;
}}
.abstract-toggle:hover {{ background: var(--c-pale); }}
.abstract-toggle-label {{ user-select: none; }}
.abstract-chevron {{ transition: transform 0.25s; flex-shrink: 0; color: var(--c-blue); }}
.abstract-toggle[aria-expanded="true"] .abstract-chevron {{ transform: rotate(180deg); }}
.pub-abstract-wrap {{
  max-height: 0; overflow: hidden;
  transition: max-height 0.35s ease, opacity 0.3s;
  opacity: 0; margin-bottom: 8px;
}}
.pub-abstract-wrap.open {{ max-height: 400px; opacity: 1; }}
.pub-abstract {{
  font-size: 15px; color: var(--c-text); line-height: 1.75;
  background: var(--c-abstract-bg); border: 1px solid var(--c-abstract-br);
  border-radius: 8px; padding: 14px 16px; margin-bottom: 4px;
  font-style: italic; font-family: 'Crimson Pro', serif;
  transition: background 0.25s, border-color 0.25s, color 0.25s;
  text-align: justify; hyphens: auto;
}}

/* CONFERENCES */
.conf-item {{
  border-left: 3px solid var(--c-conf-border);
  padding: 14px 0 14px 22px; margin-bottom: 12px;
  transition: border-color 0.25s;
}}
.conf-title {{
  margin: 0 0 10px; font-size: 14px; font-weight: 600;
  color: var(--c-navy); font-style: italic; line-height: 1.4;
  transition: color 0.25s; font-family: 'Inter', sans-serif;
}}
.conf-event {{
  display: flex; align-items: center;
  gap: 10px; flex-wrap: wrap; padding: 8px 0;
  border-bottom: 1px solid var(--c-conf-ev);
  transition: border-color 0.25s;
}}
.conf-event:last-child {{ border-bottom: none; }}
.conf-event-left {{ flex: 1; min-width: 180px; }}
.conf-event-right {{ display: flex; align-items: center; gap: 8px; flex-shrink: 0; }}
.conf-name {{ font-size: 13.5px; font-weight: 500; color: var(--c-navy); transition: color 0.25s; font-family:'Inter',sans-serif; }}
.conf-loc  {{ font-size: 13px; color: var(--c-muted); font-family:'Inter',sans-serif; }}

/* MOBILE */
@media (max-width: 768px) {{
  #sidebar {{ display: none; }}
  #topbar  {{ display: flex; }}
  #main {{ margin-left: 0; padding: 70px 18px 60px; max-width: 100%; }}
  .hero-name  {{ font-size: 28px; }}
  .section-title {{ font-size: 23px; }}
  .tl-header  {{ flex-direction: column; gap: 2px; }}

  .conf-event {{ flex-direction: column; gap: 6px; }}
  .research-grid {{ grid-template-columns: 1fr; }}
  .pub-item {{ padding-left: 14px; }}
}}
</style>
</head>
<body>

<!-- MOBILE TOPBAR -->
<header id="topbar">
  <span class="topbar-name">{PROFILE['name'].split()[0]} {PROFILE['name'].split()[-1]}</span>
  <div class="topbar-right">
    <div class="topbar-toggle" onclick="toggleTheme()" title="Toggle theme">
      <span class="topbar-icon" id="mob-theme-icon">☀</span>
      <div class="toggle-track" id="mob-track"><div class="toggle-thumb"></div></div>
    </div>
    <button id="hamburger" onclick="openMobileMenu()" aria-label="Open menu">
      <div class="ham-bar"></div><div class="ham-bar"></div><div class="ham-bar"></div>
    </button>
  </div>
</header>

<!-- MOBILE DRAWER -->
<div id="mob-overlay" onclick="closeMobileMenu()"></div>
<nav id="mob-drawer">
  <button class="mob-close" onclick="closeMobileMenu()">&#x2715;</button>
  {mob_html}
  {mob_contact_html}
</nav>

<!-- DESKTOP SIDEBAR -->
<aside id="sidebar">
  <div class="avatar">
    {photo_tag}
  </div>
  <p class="sidebar-name">{PROFILE['name']}</p>
  <p class="sidebar-title">{PROFILE['title']}</p>
  <div class="sidebar-divider"></div>
  <div class="theme-toggle">
    <span class="theme-label" id="theme-label">Light</span>
    <div class="toggle-track" id="desk-track" onclick="toggleTheme()" title="Toggle dark mode">
      <div class="toggle-thumb"></div>
    </div>
    <span class="theme-label" id="desk-theme-icon">☀</span>
  </div>
  <div style="height:8px;"></div>
  <nav>{nav_html}</nav>
  <div class="sidebar-divider"></div>
  <div class="sidebar-contact">
    <div>✉&nbsp;{email_html}</div>
    <div>⌖&nbsp;{PROFILE['location']}</div>
    {f'<div style="margin-top:4px;">{social}</div>' if social else ''}
  </div>
</aside>

<!-- MAIN -->
<main id="main">

  <section class="section" id="about">
    <div class="hero-tag"> PhD Candidate &middot; Quantitative Researcher </div>
    <h1 class="hero-name">{PROFILE['name']}</h1>
    <p class="hero-tagline">{PROFILE['tagline']}</p>
    <div class="section-label">About me</div>
    <div style="border-bottom:2px solid var(--c-pale);padding-bottom:14px;margin-bottom:22px;transition:border-color 0.25s;"></div>
    {about_ps}
    <!-- <a href="{PROFILE['cv_url']}" class="cv-btn" target="_blank">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
        <path d="M3 2h9v11H3V2zm2 3h5M5 8h5M5 11h3" stroke="#fff" stroke-width="1.3" stroke-linecap="round"/>
      </svg>
      Download CV
    </a> -->
  </section>

  <section class="section" id="education">
    <div class="section-label">Academic background</div>
    <h2 class="section-title">Education</h2>
    {edu_html}
  </section>

  <section class="section" id="experience">
    <div class="section-label">Industry &amp; academic roles</div>
    <h2 class="section-title">Professional Experience</h2>
    {exp_html}
  </section>

  <section class="section" id="publications">
    <div class="section-label">Papers &amp; working papers</div>
    <h2 class="section-title">Publications</h2>
    {pub_html}
  </section>

  <section class="section" id="conferences">
    <div class="section-label">Presentations &amp; workshops</div>
    <h2 class="section-title">Conferences</h2>
    {conf_html}
  </section>

  <section class="section" id="research">
    <div class="section-label">Fields of interest</div>
    <h2 class="section-title">Research Interests</h2>
    <div class="research-grid">{res_html}</div>
  </section>

</main>

<script>
function applyTheme(dark) {{
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  ['desk-track','mob-track'].forEach(id => {{
    const t = document.getElementById(id);
    if (t) dark ? t.classList.add('on') : t.classList.remove('on');
  }});
  const di = document.getElementById('desk-theme-icon');
  const mi = document.getElementById('mob-theme-icon');
  const lb = document.getElementById('theme-label');
  if (di) di.textContent = dark ? '🌙' : '☀';
  if (mi) mi.textContent = dark ? '🌙' : '☀';
  if (lb) lb.textContent = dark ? 'Dark' : 'Light';
  localStorage.setItem('theme', dark ? 'dark' : 'light');
}}
function toggleTheme() {{
  applyTheme(document.documentElement.getAttribute('data-theme') !== 'dark');
}}
(function() {{
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  applyTheme(saved ? saved === 'dark' : prefersDark);
}})();

function toggleAbstract(uid) {{
  const wrap = document.getElementById(uid + '-abstract');
  const btn  = wrap.nextElementSibling;
  const open = wrap.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
}}

function openMobileMenu() {{
  document.getElementById('mob-drawer').classList.add('open');
  document.getElementById('mob-overlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}}
function closeMobileMenu() {{
  document.getElementById('mob-drawer').classList.remove('open');
  document.getElementById('mob-overlay').classList.remove('open');
  document.body.style.overflow = '';
}}

const observer = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      document.querySelectorAll('.nav-link').forEach(a => a.classList.remove('active'));
      const a = document.querySelector(`.nav-link[data-section="${{e.target.id}}"]`);
      if (a) a.classList.add('active');
    }}
  }});
}}, {{ rootMargin: '-25% 0px -65% 0px' }});
document.querySelectorAll('.section').forEach(s => observer.observe(s));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    html = generate_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ index.html generated successfully!")
    print("  Open it in your browser, or deploy to GitHub Pages / Netlify.")