#!/usr/bin/env python3
"""
Academic CV Website Generator — Meghna P. Bhaugeerutty
Run:    python3 generate_cv.py
Output: index.html
"""

# ─────────────────────────────────────────────
#   EDIT YOUR CONTENT HERE
# ─────────────────────────────────────────────

PROFILE = {
    "name": "Meghna P. Bhaugeerutty",
    "title": "CIFRE PhD Candidate · Quantitative Researcher",
    "institution": "Université Paris Dauphine – PSL × Amundi",
    "email": "meghna.bhaugeerutty@dauphine.psl.eu",
    # "phone": "+33 (0)6 95 72 14 11",
    "github": "https://github.com/meghna-pb",          
    "linkedin": "https://www.linkedin.com/in/meghna-bhaugeerutty/",   
    "location": "Paris, France",
    "tagline": (
        "CIFRE PhD candidate at Université Paris Dauphine – PSL and Amundi, "
        "researching allocation biases in Net Zero investing, physical climate risk, "
        "and quantitative portfolio management."
    ),
    "about": [
        "I am a PhD candidate in Economics at Université Paris Dauphine - PSL, "
        "in partnership with Amundi Investment Solutions (CIFRE). My doctoral research, co-supervised "
        "by Yannick Le Pen (LEDa-CGEMP) and Thierry Roncalli (Amundi Research Institute), "
        "investigates allocation biases in Net Zero passive investing "
        "and the integration of physical climate risk in portfolio management.",

        "I hold an MSc in Quantitative Finance from Université Paris Dauphine - PSL "
        "and a Double BSc in Applied Economics "
        "from Université Paris Dauphine – PSL and Goethe Universität Frankfurt. My academic work "
        "spans sustainable finance, ESG methodologies,  "
        "and financial econometrics.",

        "Prior to my PhD, I worked as a Quantitative Analyst in ESG Research at Société Générale "
        "Investment Solutions, where I designed proprietary ESG scoring models and built a "
        "Net Zero commitment dashboard. I also interned at ING Wholesale Banking in Frankfurt, "
        "focusing on sustainable finance transactions and ESG client analysis.",
    ],
    "cv_url": "#",  # replace with a path or URL to your PDF CV
}

EDUCATION = [
    {
        "degree": "PhD in Economics",
        "institution": "Université Paris Dauphine – PSL × Amundi Investment Solutions",
        "years": "2024 – 2027",
        "details": (
            "Laboratoire d'Economie de Dauphine (LEDa) · "
            "Supervisors: Yannick Le Pen (Dauphine) & Thierry Roncalli (Amundi) · "
            "Research on allocation biases in Net Zero passive investing and physical climate risk "
            "integration in portfolio management"
        ),
    },
    {
        "degree": "MSc in Economic and Financial Engineering - Quantitative Finance (272)",
        "institution": "Université Paris Dauphine – PSL",
        "years": "2022 – 2024",
        "details": (
            "Mention Bien · Quantitative Asset Management, NLP & Machine Learning, "
            "Stochastic Calculus, Derivative Instruments, Econometrics · "

            "M2 Thesis: 'Analysis of current trends in decarbonisation' (18.66/20) · "

            "M1 Thesis: 'SRI label on fund financial performance & ESG breakdown' (16/20)"
        ),
    },
    {
        "degree": "Double BSc in Applied Economics",
        "institution": "Goethe Universität Frankfurt & Université Paris Dauphine – PSL",
        "years": "2019 – 2022",
        "details": (
            "Exchange year at Goethe Universität Frankfurt (2021–2022), grade: Good · "
            "Thesis on KPI selection for Sustainability-linked Products (1.0, highest grade) · "
            "Courses: Economics, Mathematics, Statistics, Python & VBA, "
            "Accounting, Law, Social Sciences · Minor in Psychology "
        ),
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
        "area": "Commodities and physical risk",
        "icon": "C",
        "description": (
            "Evalutation of the impact of external shocks (natural disasters, geopolitical tensions) "
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

PUBLICATIONS = [
    {
        "type": "Working Paper",
        "title": "Beyond Decarbonisation: Disentangling Allocation Biases and Global Reallocation in Net Zero Passive Investing",
        "authors": "Bhaugeerutty, M.",
        "venue": "Working paper",
        "year": "2025",
        "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5958135"
    },
    {
        "type": "Work in Progress",
        "title": "Climate Black-Litterman: physical risk integration in portfolio management",
        "authors": "Bhaugeerutty, M.",
        "venue": "Working paper",
        "year": "2026",
        "url": None,
    },

        {
        "type": "Work in Progress",
        "title": "Impact of external shocks on agricultural commodities futures",
        "authors": "Bhaugeerutty, M. & Sekine, T.",
        "venue": "Working paper",
        "year": "2026",
        "url": None,
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


# ─────────────────────────────────────────────
#   GENERATOR  (no need to edit below)
# ─────────────────────────────────────────────

def badge(text, color_class):
    classes = {
        "wp":        "badge-wp",
        "cp":        "badge-cp",
        "wip":       "badge-wip",
        "presenter": "badge-wp",
        "discussant":"badge-wip",
    }
    cls = classes.get(color_class, "badge-wp")
    return f'<span class="badge {cls}">{text}</span>'

def pub_badge(ptype):
    if ptype == "Working Paper":      return badge("Working Paper", "wp")
    elif ptype == "Conference Paper": return badge("Conference", "cp")
    else:                             return badge("In Progress", "wip")

def conf_role_badge(role):
    key = role.lower()
    return badge(role, "presenter" if key == "presenter" else "discussant")

def timeline_icon(color="blue"):
    if color == "green":
        return """<div class="tl-icon tl-green">
          <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
            <rect x="2" y="4" width="11" height="9" rx="2" fill="#3B6D11" opacity="0.7"/>
            <path d="M5 4V3a2 2 0 0 1 4 0v1" stroke="#3B6D11" stroke-width="1.2" stroke-linecap="round" fill="none"/>
          </svg></div>"""
    return """<div class="tl-icon tl-blue">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M8 2L14 5.5V10.5L8 14L2 10.5V5.5L8 2Z" fill="#378ADD" opacity="0.7"/>
      </svg></div>"""

def education_html():
    items = []
    for i, edu in enumerate(EDUCATION):
        connector = "" if i == len(EDUCATION) - 1 else '<div class="tl-connector"></div>'
        items.append(f"""
        <div class="tl-row">
          <div class="tl-left">{timeline_icon("blue")}</div>
          <div class="tl-body">
            <div class="tl-header">
              <p class="tl-title">{edu['degree']}</p>
              <span class="tl-year">{edu['years']}</span>
            </div>
            <p class="tl-org">{edu['institution']}</p>
            <p class="tl-detail">{edu['details']}</p>
          </div>
        </div>
        {connector}
        """)
    return "\n".join(items)

def experience_html():
    items = []
    for i, exp in enumerate(EXPERIENCE):
        connector = "" if i == len(EXPERIENCE) - 1 else '<div class="tl-connector tl-connector-green"></div>'
        bullets_html = "".join(
            f'<li class="exp-bullet">{b}</li>' for b in exp["bullets"]
        )
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
    for pub in PUBLICATIONS:
        link_open  = f'<a href="{pub["url"]}" target="_blank" class="pub-link">' if pub.get("url") else ""
        link_close = "</a>" if pub.get("url") else ""
        arrow = (
            '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" class="pub-arrow">'
            '<path d="M2 11L11 2M11 2H5M11 2V8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
        ) if pub.get("url") else ""
        items.append(f"""
        <div class="pub-item">
          <div class="pub-meta">{pub_badge(pub['type'])}<span class="pub-year">{pub['year']}</span></div>
          <p class="pub-title">{link_open}{pub['title']}{arrow}{link_close}</p>
          <p class="pub-authors">{pub['authors']}</p>
          <p class="pub-venue">{pub['venue']}</p>
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
            </div>
            """
        items.append(f"""
        <div class="conf-item">
          <p class="conf-title">"{paper['title']}"</p>
          {events_html}
        </div>
        """)
    return "\n".join(items)

def about_paragraphs():
    return "\n".join(
        f'<p class="about-p">{p}</p>' for p in PROFILE["about"]
    )

# ── NAV ITEMS ────────────────────────────────
NAV_ITEMS = [
    ("about",        "About"),
    ("education",    "Education"),
    ("experience",   "Experience"),
    ("research",     "Research"),
    ("publications", "Publications"),
    ("conferences",  "Conferences"),
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
    edu_html  = education_html()
    exp_html  = experience_html()
    res_html  = research_html()
    pub_html  = publications_html()
    conf_html = conferences_html()
    about_ps  = about_paragraphs()
    nav_html  = nav_links()
    mob_html  = mobile_nav_links()
    initials  = "".join(w[0].upper() for w in PROFILE["name"].split()[:2])

    gh_link = (
        f'<a href="{PROFILE["github"]}" target="_blank" class="social-link">GitHub</a>'
        if PROFILE.get("github") else ""
    )
    li_link = (
        f'<a href="{PROFILE["linkedin"]}" target="_blank" class="social-link">LinkedIn</a>'
        if PROFILE.get("linkedin") else ""
    )
    social = " &middot; ".join(filter(None, [gh_link, li_link]))

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{PROFILE['name']} – Academic CV</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>

/* ══════════════════════════════════════════
   THEME TOKENS
══════════════════════════════════════════ */
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
}}

/* ══════════════════════════════════════════
   RESET & BASE
══════════════════════════════════════════ */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: 'DM Sans', sans-serif;
  background: var(--c-bg);
  color: var(--c-navy);
  min-height: 100vh;
  display: flex;
  transition: background 0.25s, color 0.25s;
}}

/* ══════════════════════════════════════════
   SIDEBAR  (desktop)
══════════════════════════════════════════ */
#sidebar {{
  width: 268px;
  min-height: 100vh;
  background: linear-gradient(180deg,
    var(--c-sidebar-from) 0%,
    var(--c-sidebar-mid)  60%,
    var(--c-sidebar-to)   100%);
  position: fixed;
  top: 0; left: 0;
  display: flex;
  flex-direction: column;
  padding: 36px 0 28px;
  z-index: 200;
  overflow-y: auto;
  transition: background 0.25s;
}}
.avatar {{
  width: 68px; height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4AAAF0, #1866B4);
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; font-weight: 600; color: #fff;
  margin: 0 auto 14px;
  border: 3px solid rgba(181,212,244,0.35);
  flex-shrink: 0;
}}
.sidebar-name {{
  font-family: 'Lora', serif;
  font-size: 14.5px; font-weight: 600;
  color: #E6F1FB;
  text-align: center;
  padding: 0 18px;
  line-height: 1.35;
}}
.sidebar-title {{
  font-size: 10.5px; color: #7aaed4;
  text-align: center; padding: 5px 18px 0;
  line-height: 1.55;
}}
.sidebar-divider {{
  height: 1px;
  background: rgba(181,212,244,0.18);
  margin: 18px 20px;
  flex-shrink: 0;
}}

/* Theme toggle inside sidebar */
.theme-toggle {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 0 20px 4px;
}}
.theme-label {{
  font-size: 11px;
  color: #7aaed4;
  user-select: none;
}}
.toggle-track {{
  width: 36px; height: 20px;
  background: rgba(181,212,244,0.2);
  border-radius: 10px;
  position: relative;
  cursor: pointer;
  transition: background 0.25s;
  border: 1px solid rgba(181,212,244,0.3);
  flex-shrink: 0;
}}
.toggle-track.on {{ background: rgba(74,170,240,0.5); }}
.toggle-thumb {{
  width: 14px; height: 14px;
  background: #fff;
  border-radius: 50%;
  position: absolute;
  top: 2px; left: 2px;
  transition: transform 0.22s;
}}
.toggle-track.on .toggle-thumb {{ transform: translateX(16px); }}

nav {{ margin-top: 4px; }}
.nav-link {{
  display: flex; align-items: center; gap: 10px;
  padding: 9px 22px;
  font-size: 12.5px; font-weight: 500;
  color: #94c0e2;
  text-decoration: none;
  border-left: 3px solid transparent;
  transition: all 0.18s;
  letter-spacing: 0.02em;
}}
.nav-link:hover, .nav-link.active {{
  color: #E6F1FB;
  background: rgba(181,212,244,0.10);
  border-left-color: #4AAAF0;
}}
.nav-dot {{
  width: 5px; height: 5px;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.5;
  flex-shrink: 0;
}}
.sidebar-contact {{
  margin-top: auto;
  padding: 0 20px;
  font-size: 10.5px;
  color: #5e96be;
  line-height: 2;
  flex-shrink: 0;
}}
.sidebar-contact a, .social-link {{
  color: #7aaed4; text-decoration: none;
}}
.sidebar-contact a:hover, .social-link:hover {{ color: #B5D4F4; }}

/* ══════════════════════════════════════════
   MOBILE TOPBAR
══════════════════════════════════════════ */
#topbar {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 54px;
  background: var(--c-topbar);
  border-bottom: 1px solid var(--c-topbar-br);
  z-index: 300;
  align-items: center;
  justify-content: space-between;
  padding: 0 18px;
  transition: background 0.25s;
}}
.topbar-name {{
  font-family: 'Lora', serif;
  font-size: 15px; font-weight: 600;
  color: var(--c-navy);
}}
.topbar-right {{
  display: flex; align-items: center; gap: 12px;
}}
/* Inline theme toggle for topbar */
.topbar-toggle {{
  display: flex; align-items: center; gap: 6px;
  cursor: pointer;
}}
.topbar-toggle .toggle-track {{
  width: 32px; height: 18px;
  background: var(--c-border);
  border: 1px solid var(--c-border);
}}
.topbar-toggle .toggle-track.on {{
  background: var(--c-mid);
}}
.topbar-toggle .toggle-thumb {{
  width: 12px; height: 12px;
  top: 2px; left: 2px;
  background: #fff;
}}
.topbar-toggle .toggle-track.on .toggle-thumb {{
  transform: translateX(14px);
}}
.topbar-icon {{
  font-size: 15px; line-height: 1;
  color: var(--c-muted);
}}
/* Hamburger */
#hamburger {{
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 4px;
  background: none; border: none;
}}
.ham-bar {{
  width: 22px; height: 2px;
  background: var(--c-navy);
  border-radius: 2px;
  transition: all 0.25s;
}}

/* ══════════════════════════════════════════
   MOBILE DRAWER
══════════════════════════════════════════ */
#mob-overlay {{
  display: none;
  position: fixed; inset: 0;
  background: var(--c-mob-overlay);
  z-index: 390;
}}
#mob-drawer {{
  position: fixed;
  top: 0; right: -100%;
  width: min(280px, 80vw);
  height: 100%;
  background: var(--c-mob-bg);
  z-index: 400;
  display: flex;
  flex-direction: column;
  padding: 64px 0 32px;
  transition: right 0.28s cubic-bezier(.4,0,.2,1);
  overflow-y: auto;
}}
#mob-drawer.open {{ right: 0; }}
#mob-overlay.open {{ display: block; }}
.mob-nav-link {{
  display: block;
  padding: 13px 28px;
  font-size: 15px; font-weight: 500;
  color: var(--c-mob-link);
  text-decoration: none;
  border-bottom: 1px solid rgba(181,212,244,0.08);
  transition: background 0.15s;
}}
.mob-nav-link:hover {{ background: rgba(181,212,244,0.08); }}
.mob-close {{
  position: absolute;
  top: 14px; right: 16px;
  background: none; border: none;
  font-size: 24px;
  color: #94c0e2;
  cursor: pointer;
  line-height: 1;
}}

/* ══════════════════════════════════════════
   MAIN CONTENT
══════════════════════════════════════════ */
#main {{
  margin-left: 268px;
  flex: 1;
  padding: 48px 52px 80px;
  max-width: 900px;
  transition: background 0.25s;
}}

/* ── Sections ── */
.section {{ margin-bottom: 60px; scroll-margin-top: 32px; }}
.section-label {{
  font-size: 10.5px; font-weight: 600;
  letter-spacing: 0.12em;
  color: var(--c-mid);
  text-transform: uppercase;
  margin-bottom: 6px;
}}
.section-title {{
  font-family: 'Lora', serif;
  font-size: 26px; font-weight: 600;
  color: var(--c-navy);
  margin-bottom: 28px;
  padding-bottom: 14px;
  border-bottom: 2px solid var(--c-pale);
  transition: color 0.25s, border-color 0.25s;
}}

/* ── Hero ── */
.hero-tag {{
  display: inline-block;
  background: var(--c-pale);
  color: var(--c-blue);
  font-size: 12px; font-weight: 500;
  padding: 4px 14px;
  border-radius: 20px;
  margin-bottom: 18px;
  border: 1px solid var(--c-border);
  transition: background 0.25s, color 0.25s;
}}
.hero-name {{
  font-family: 'Lora', serif;
  font-size: 36px; font-weight: 600;
  color: var(--c-navy);
  line-height: 1.2;
  margin-bottom: 10px;
  transition: color 0.25s;
}}
.hero-tagline {{
  font-size: 15px; color: var(--c-muted);
  line-height: 1.7; max-width: 560px;
  margin-bottom: 28px;
  font-style: italic;
  font-family: 'Lora', serif;
  transition: color 0.25s;
}}
.about-p {{
  margin: 0 0 14px;
  font-size: 14.5px;
  color: var(--c-text);
  line-height: 1.75;
  transition: color 0.25s;
}}
.cv-btn {{
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--c-blue); color: #fff;
  font-size: 13px; font-weight: 500;
  padding: 10px 22px; border-radius: 8px;
  text-decoration: none;
  transition: background 0.2s, transform 0.15s;
  border: none; cursor: pointer;
  margin-top: 8px;
}}
.cv-btn:hover {{ background: var(--c-navy); transform: translateY(-1px); }}

/* ── Timeline ── */
.tl-row {{ display: flex; gap: 20px; align-items: flex-start; }}
.tl-left {{ flex-shrink: 0; margin-top: 4px; }}
.tl-icon {{
  width: 38px; height: 38px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}}
.tl-blue  {{ background: var(--c-tl-blue-bg);  border: 2px solid var(--c-tl-blue-br); }}
.tl-green {{ background: var(--c-tl-green-bg); border: 2px solid var(--c-tl-green-br); }}
.tl-connector {{
  width: 2px; height: 30px;
  background: var(--c-tl-conn);
  margin: 0 0 0 18px;
}}
.tl-connector-green {{ background: var(--c-tl-conn-g); }}
.tl-body {{ padding-bottom: 8px; flex: 1; }}
.tl-header {{
  display: flex; justify-content: space-between;
  align-items: baseline; flex-wrap: wrap; gap: 6px;
}}
.tl-title {{
  margin: 0; font-size: 15px; font-weight: 600;
  color: var(--c-navy); transition: color 0.25s;
}}
.tl-year {{
  font-size: 12px; color: var(--c-blue);
  white-space: nowrap; transition: color 0.25s;
}}
.tl-org {{
  margin: 4px 0 2px; font-size: 13.5px;
  color: var(--c-blue); font-weight: 500;
  transition: color 0.25s;
}}
.tl-loc {{ color: var(--c-muted); font-weight: 400; }}
.tl-detail {{
  margin: 0; font-size: 13px;
  color: var(--c-detail); line-height: 1.55;
  transition: color 0.25s;
}}
.exp-list {{ margin: 4px 0 0; padding-left: 16px; }}
.exp-bullet {{
  font-size: 13px; color: var(--c-detail);
  line-height: 1.6; margin-bottom: 3px;
  transition: color 0.25s;
}}

/* ── Research cards ── */
.research-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 16px;
}}
.research-card {{
  background: var(--c-surface);
  border: 1px solid var(--c-border);
  border-radius: 12px;
  padding: 20px 22px;
  transition: box-shadow 0.2s, background 0.25s, border-color 0.25s;
  cursor: default;
}}
.research-card:hover {{ box-shadow: 0 4px 18px var(--c-card-hover); }}
.research-icon {{
  width: 36px; height: 36px; border-radius: 10px;
  background: linear-gradient(135deg, #4AAAF0, #1866B4);
  display: flex; align-items: center; justify-content: center;
  font-weight: 700; font-size: 15px; color: #fff;
  margin-bottom: 10px;
}}
.research-area {{
  margin: 0 0 6px; font-size: 14.5px; font-weight: 600;
  color: var(--c-navy); transition: color 0.25s;
}}
.research-desc {{
  margin: 0; font-size: 13.5px;
  color: var(--c-detail); line-height: 1.65;
  transition: color 0.25s;
}}

/* ── Badges ── */
.badge {{
  display: inline-block;
  font-size: 11px; font-weight: 500;
  padding: 3px 10px; border-radius: 20px;
  letter-spacing: 0.03em; white-space: nowrap;
  transition: background 0.25s, color 0.25s;
}}
.badge-wp  {{ background: var(--badge-wp-bg);  color: var(--badge-wp-fg); }}
.badge-cp  {{ background: var(--badge-cp-bg);  color: var(--badge-cp-fg); }}
.badge-wip {{ background: var(--badge-wip-bg); color: var(--badge-wip-fg); }}

/* ── Publications ── */
.pub-item {{
  border-left: 3px solid var(--c-pub-border);
  padding: 14px 0 14px 20px;
  margin-bottom: 6px;
  transition: border-color 0.25s;
}}
.pub-meta {{
  display: flex; align-items: center;
  gap: 10px; margin-bottom: 8px; flex-wrap: wrap;
}}
.pub-year  {{ font-size: 12px; color: var(--c-muted); }}
.pub-title {{
  margin: 0 0 4px; font-size: 14.5px; font-weight: 600;
  color: var(--c-navy); line-height: 1.4;
  transition: color 0.25s;
}}
.pub-link  {{ text-decoration: none; color: inherit; }}
.pub-arrow {{ margin-left: 5px; vertical-align: middle; color: var(--c-mid); }}
.pub-authors {{ margin: 0 0 2px; font-size: 13px; color: var(--c-blue); transition: color 0.25s; }}
.pub-venue   {{ margin: 0; font-size: 12.5px; color: var(--c-muted); font-style: italic; }}

/* ── Conferences ── */
.conf-item {{
  border-left: 3px solid var(--c-conf-border);
  padding: 14px 0 14px 20px;
  margin-bottom: 12px;
  transition: border-color 0.25s;
}}
.conf-title {{
  margin: 0 0 10px; font-size: 14px; font-weight: 600;
  color: var(--c-navy); font-style: italic; line-height: 1.4;
  transition: color 0.25s;
}}
.conf-event {{
  display: flex; align-items: baseline;
  gap: 10px; flex-wrap: wrap;
  padding: 8px 0;
  border-bottom: 1px solid var(--c-conf-ev);
  transition: border-color 0.25s;
}}
.conf-event-left  {{ flex: 1; min-width: 180px; }}
.conf-event-right {{ display: flex; align-items: center; gap: 8px; }}
.conf-name {{ font-size: 13.5px; font-weight: 500; color: var(--c-navy); transition: color 0.25s; }}
.conf-loc  {{ font-size: 13px; color: var(--c-muted); }}

/* ══════════════════════════════════════════
   RESPONSIVE — MOBILE
══════════════════════════════════════════ */
@media (max-width: 768px) {{
  #sidebar {{ display: none; }}
  #topbar  {{ display: flex; }}
  #main {{
    margin-left: 0;
    padding: 72px 20px 60px;
    max-width: 100%;
  }}
  .hero-name  {{ font-size: 26px; }}
  .section-title {{ font-size: 22px; }}
  .tl-header  {{ flex-direction: column; gap: 2px; }}
  .conf-event {{ flex-direction: column; gap: 6px; }}
  .research-grid {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>

<!-- ════ MOBILE TOPBAR ════ -->
<header id="topbar">
  <span class="topbar-name">{PROFILE['name'].split()[0]} {PROFILE['name'].split()[-1]}</span>
  <div class="topbar-right">
    <!-- inline theme toggle -->
    <div class="topbar-toggle" onclick="toggleTheme()" title="Toggle theme">
      <span class="topbar-icon" id="mob-theme-icon">☀</span>
      <div class="toggle-track" id="mob-track">
        <div class="toggle-thumb"></div>
      </div>
    </div>
    <!-- hamburger -->
    <button id="hamburger" onclick="openMobileMenu()" aria-label="Open menu">
      <div class="ham-bar"></div>
      <div class="ham-bar"></div>
      <div class="ham-bar"></div>
    </button>
  </div>
</header>

<!-- ════ MOBILE DRAWER ════ -->
<div id="mob-overlay" onclick="closeMobileMenu()"></div>
<nav id="mob-drawer">
  <button class="mob-close" onclick="closeMobileMenu()">&#x2715;</button>
  {mob_html}
</nav>

<!-- ════ DESKTOP SIDEBAR ════ -->
<aside id="sidebar">
  <div class="avatar">{initials}</div>
  <p class="sidebar-name">{PROFILE['name']}</p>
  <p class="sidebar-title">{PROFILE['title']}<br>{PROFILE['institution']}</p>
  <div class="sidebar-divider"></div>

  <!-- Theme toggle -->
  <div class="theme-toggle">
    <span class="theme-label" id="theme-label">Light</span>
    <div class="toggle-track" id="desk-track" onclick="toggleTheme()" title="Toggle dark mode">
      <div class="toggle-thumb"></div>
    </div>
    <span class="theme-label" id="desk-theme-icon">☀</span>
  </div>
  <div style="height:10px;"></div>

  <nav>
    {nav_html}
  </nav>
  <div class="sidebar-divider"></div>
  <div class="sidebar-contact">
    <div>✉&nbsp;<a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a></div>
    <div>⌖&nbsp;{PROFILE['location']}</div>
    {f'<div style="margin-top:4px;">{social}</div>' if social else ''}
  </div>
</aside>

<!-- ════ MAIN CONTENT ════ -->
<main id="main">

  <!-- About -->
  <section class="section" id="about">
    <div class="hero-tag">CIFRE PhD &middot; Quantitative Researcher</div>
    <h1 class="hero-name">{PROFILE['name']}</h1>
    <p class="hero-tagline">{PROFILE['tagline']}</p>
    <div class="section-label">About me</div>
    <div style="border-bottom:2px solid var(--c-pale);padding-bottom:14px;margin-bottom:22px;transition:border-color 0.25s;"></div>
    {about_ps}
    <a href="{PROFILE['cv_url']}" class="cv-btn" target="_blank">
      <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
        <path d="M3 2h9v11H3V2zm2 3h5M5 8h5M5 11h3" stroke="#fff" stroke-width="1.3" stroke-linecap="round"/>
      </svg>
      Download CV
    </a>
  </section>

  <!-- Education -->
  <section class="section" id="education">
    <div class="section-label">Academic background</div>
    <h2 class="section-title">Education</h2>
    {edu_html}
  </section>

  <!-- Experience -->
  <section class="section" id="experience">
    <div class="section-label">Industry &amp; academic roles</div>
    <h2 class="section-title">Professional Experience</h2>
    {exp_html}
  </section>

  <!-- Research -->
  <section class="section" id="research">
    <div class="section-label">Fields of interest</div>
    <h2 class="section-title">Research</h2>
    <div class="research-grid">{res_html}</div>
  </section>

  <!-- Publications -->
  <section class="section" id="publications">
    <div class="section-label">Papers &amp; working papers</div>
    <h2 class="section-title">Publications</h2>
    {pub_html}
  </section>

  <!-- Conferences -->
  <section class="section" id="conferences">
    <div class="section-label">Presentations &amp; workshops</div>
    <h2 class="section-title">Conferences</h2>
    {conf_html}
  </section>

</main>

<script>
/* ── Theme ── */
function applyTheme(dark) {{
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
  const tracks = [document.getElementById('desk-track'), document.getElementById('mob-track')];
  tracks.forEach(t => {{ if (t) dark ? t.classList.add('on') : t.classList.remove('on'); }});
  const deskIcon = document.getElementById('desk-theme-icon');
  const mobIcon  = document.getElementById('mob-theme-icon');
  const label    = document.getElementById('theme-label');
  if (deskIcon) deskIcon.textContent = dark ? '🌙' : '☀';
  if (mobIcon)  mobIcon.textContent  = dark ? '🌙' : '☀';
  if (label)    label.textContent    = dark ? 'Dark' : 'Light';
  localStorage.setItem('theme', dark ? 'dark' : 'light');
}}
function toggleTheme() {{
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  applyTheme(!isDark);
}}
// Restore saved preference
(function() {{
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  applyTheme(saved ? saved === 'dark' : prefersDark);
}})();

/* ── Mobile drawer ── */
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

/* ── Active nav on scroll ── */
const sections = document.querySelectorAll('.section');
const navLinks = document.querySelectorAll('.nav-link');
const observer = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      navLinks.forEach(a => a.classList.remove('active'));
      const active = document.querySelector(`.nav-link[data-section="${{e.target.id}}"]`);
      if (active) active.classList.add('active');
    }}
  }});
}}, {{ rootMargin: '-25% 0px -65% 0px' }});
sections.forEach(s => observer.observe(s));
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
