#!/usr/bin/env python3
"""
Academic CV Website Generator for Meghna Bhaugeerutty
Run: python3 generate_cv.py
Output: index.html
"""

# ─────────────────────────────────────────────
#   EDIT YOUR CONTENT HERE
# ─────────────────────────────────────────────

PROFILE = {
    "name": "Meghna Bhaugeerutty",
    "title": "Quantitative Researcher · PhD Candidate",
    "institution": "Université Paris Dauphine – PSL",
    "email": "m.bhaugeerutty@dauphine.psl.eu",
    "location": "Paris, France",
    "tagline": (
        "I study the intersection of financial economics and quantitative methods, "
        "with a focus on market microstructure, asset pricing, and econometric modelling."
    ),
    "about": [
        "I am a PhD student in Economics at Université Paris Dauphine – PSL, "
        "where I work on quantitative methods applied to financial markets. "
        "My doctoral research investigates how information asymmetry shapes price discovery "
        "and liquidity dynamics in modern electronic markets.",

        "Before joining Dauphine, I completed a Master's degree in Applied Mathematics "
        "and Economics, building a strong foundation in stochastic calculus, "
        "time-series econometrics, and statistical learning.",

        "Beyond my thesis, I contribute to collaborative research projects "
        "on algorithmic trading, systemic risk measurement, and the empirical "
        "study of high-frequency data. I welcome opportunities to discuss my work "
        "at conferences and seminars.",
    ],
    "cv_url": "#",  # replace with a link to your PDF CV
}

EDUCATION = [
    {
        "degree": "PhD in Economics",
        "institution": "Université Paris Dauphine – PSL",
        "years": "2022 – present",
        "details": "Thesis: Information Asymmetry and Liquidity in Electronic Markets · Supervisor: Prof. [Name]",
    },
    {
        "degree": "MSc Applied Mathematics & Economics",
        "institution": "Université Paris Dauphine – PSL",
        "years": "2020 – 2022",
        "details": "Graduated with distinction · Major: Stochastic modelling and financial econometrics",
    },
    {
        "degree": "BSc Mathematics",
        "institution": "Université de Maurice",
        "years": "2017 – 2020",
        "details": "First-class honours · Minor: Statistics and Computer Science",
    },
]

RESEARCH = [
    {
        "area": "Market Microstructure",
        "icon": "M",
        "description": (
            "Price discovery, bid-ask spreads, order flow toxicity, and the "
            "effects of information asymmetry on liquidity provision in electronic limit order books."
        ),
    },
    {
        "area": "Asset Pricing",
        "icon": "A",
        "description": (
            "Empirical tests of factor models, risk premia decomposition, "
            "and the role of rare disasters in cross-sectional return variation."
        ),
    },
    {
        "area": "Financial Econometrics",
        "icon": "E",
        "description": (
            "High-frequency data analysis, realized variance estimation, "
            "long-memory processes, and jump detection in continuous-time models."
        ),
    },
    {
        "area": "Algorithmic Trading",
        "icon": "T",
        "description": (
            "Optimal execution strategies, market impact models, and the "
            "interaction between strategic traders and passive market makers."
        ),
    },
]

PUBLICATIONS = [
    {
        "type": "Working Paper",
        "title": "Adverse Selection and Spread Dynamics in High-Frequency Markets",
        "authors": "Bhaugeerutty, M.",
        "venue": "Working paper · Available on SSRN",
        "year": "2024",
        "url": "#",
    },
    {
        "type": "Conference Paper",
        "title": "Realized Variance Under Microstructure Noise: A Kernel Approach",
        "authors": "Bhaugeerutty, M. & [Co-author]",
        "venue": "Proceedings of the 2023 European Finance Association Meeting",
        "year": "2023",
        "url": "#",
    },
    {
        "type": "Work in Progress",
        "title": "Systemic Risk Spillovers and the Role of Market Makers",
        "authors": "Bhaugeerutty, M., [Co-author 1] & [Co-author 2]",
        "venue": "In preparation",
        "year": "2025",
        "url": None,
    },
]

# ─────────────────────────────────────────────
#   GENERATOR  (no need to edit below)
# ─────────────────────────────────────────────

def badge(text, color_class):
    colors = {
        "wp":  ("E6F1FB", "185FA5"),
        "cp":  ("E1F5EE", "0F6E56"),
        "wip": ("FAEEDA", "854F0B"),
    }
    bg, fg = colors.get(color_class, ("F1EFE8", "5F5E5A"))
    return (
        f'<span style="background:#{bg};color:#{fg};font-size:11px;'
        f'font-weight:500;padding:3px 10px;border-radius:20px;'
        f'letter-spacing:0.03em;white-space:nowrap;">{text}</span>'
    )

def pub_badge(ptype):
    if ptype == "Working Paper":
        return badge("Working Paper", "wp")
    elif ptype == "Conference Paper":
        return badge("Conference", "cp")
    else:
        return badge("In Progress", "wip")

def education_html():
    items = []
    for i, edu in enumerate(EDUCATION):
        connector = "" if i == len(EDUCATION) - 1 else (
            '<div style="width:2px;height:32px;background:#B5D4F4;'
            'margin:0 0 0 18px;"></div>'
        )
        items.append(f"""
        <div style="display:flex;gap:20px;align-items:flex-start;">
          <div style="flex-shrink:0;margin-top:4px;">
            <div style="width:38px;height:38px;border-radius:50%;
              background:#E6F1FB;border:2px solid #85B7EB;
              display:flex;align-items:center;justify-content:center;">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M8 2L14 5.5V10.5L8 14L2 10.5V5.5L8 2Z"
                  fill="#378ADD" opacity="0.7"/>
              </svg>
            </div>
          </div>
          <div style="padding-bottom:8px;flex:1;">
            <div style="display:flex;justify-content:space-between;
              align-items:baseline;flex-wrap:wrap;gap:6px;">
              <p style="margin:0;font-size:15px;font-weight:600;
                color:#0D2B45;">{edu['degree']}</p>
              <span style="font-size:12px;color:#5A8AB5;
                white-space:nowrap;">{edu['years']}</span>
            </div>
            <p style="margin:4px 0 2px;font-size:13.5px;
              color:#185FA5;font-weight:500;">{edu['institution']}</p>
            <p style="margin:0;font-size:13px;color:#5a7080;
              line-height:1.5;">{edu['details']}</p>
          </div>
        </div>
        {connector}
        """)
    return "\n".join(items)

def research_html():
    cards = []
    for r in RESEARCH:
        cards.append(f"""
        <div style="background:#fff;border:1px solid #C8DFF2;
          border-radius:12px;padding:20px 22px;
          transition:box-shadow 0.2s;cursor:default;"
          onmouseover="this.style.boxShadow='0 4px 18px rgba(55,138,221,0.12)'"
          onmouseout="this.style.boxShadow='none'">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
            <div style="width:36px;height:36px;border-radius:10px;
              background:linear-gradient(135deg,#4AAAF0,#1866B4);
              display:flex;align-items:center;justify-content:center;
              font-weight:700;font-size:15px;color:#fff;flex-shrink:0;">
              {r['icon']}
            </div>
            <p style="margin:0;font-size:14.5px;font-weight:600;
              color:#0D2B45;">{r['area']}</p>
          </div>
          <p style="margin:0;font-size:13.5px;color:#4a6678;
            line-height:1.65;">{r['description']}</p>
        </div>
        """)
    return "\n".join(cards)

def publications_html():
    items = []
    for pub in PUBLICATIONS:
        link_open = f'<a href="{pub["url"]}" target="_blank" style="text-decoration:none;">' if pub["url"] else ""
        link_close = "</a>" if pub["url"] else ""
        arrow = (
            '<svg width="13" height="13" viewBox="0 0 13 13" fill="none" style="margin-left:5px;vertical-align:middle;">'
            '<path d="M2 11L11 2M11 2H5M11 2V8" stroke="#378ADD" stroke-width="1.5" stroke-linecap="round"/></svg>'
        ) if pub["url"] else ""
        items.append(f"""
        <div style="border-left:3px solid #85B7EB;padding:14px 0 14px 20px;margin-bottom:6px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap;">
            {pub_badge(pub['type'])}
            <span style="font-size:12px;color:#7a96aa;">{pub['year']}</span>
          </div>
          <p style="margin:0 0 4px;font-size:14.5px;font-weight:600;color:#0D2B45;line-height:1.4;">
            {link_open}{pub['title']}{arrow}{link_close}
          </p>
          <p style="margin:0 0 2px;font-size:13px;color:#185FA5;">{pub['authors']}</p>
          <p style="margin:0;font-size:12.5px;color:#7a96aa;font-style:italic;">{pub['venue']}</p>
        </div>
        """)
    return "\n".join(items)

def about_paragraphs():
    return "\n".join(
        f'<p style="margin:0 0 14px;font-size:14.5px;color:#334e60;line-height:1.75;">{p}</p>'
        for p in PROFILE["about"]
    )

def generate_html():
    edu_html = education_html()
    res_html = research_html()
    pub_html = publications_html()
    about_ps = about_paragraphs()
    initials = "".join(w[0].upper() for w in PROFILE["name"].split()[:2])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{PROFILE['name']} – Academic CV</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  :root {{
    --navy:    #0D2B45;
    --blue:    #185FA5;
    --mid:     #378ADD;
    --light:   #B5D4F4;
    --pale:    #E6F1FB;
    --muted:   #5a7080;
    --border:  #C8DFF2;
    --bg:      #F4F8FD;
    --white:   #FFFFFF;
    --sidebar: 260px;
  }}

  html {{ scroll-behavior: smooth; }}

  body {{
    font-family: 'DM Sans', sans-serif;
    background: var(--bg);
    color: var(--navy);
    min-height: 100vh;
    display: flex;
  }}

  /* ── Sidebar ── */
  #sidebar {{
    width: var(--sidebar);
    min-height: 100vh;
    background: linear-gradient(180deg, #0D2B45 0%, #103557 60%, #0A253E 100%);
    position: fixed;
    top: 0; left: 0;
    display: flex;
    flex-direction: column;
    padding: 40px 0 32px;
    z-index: 100;
  }}

  .avatar {{
    width: 72px; height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4AAAF0, #1866B4);
    display: flex; align-items: center; justify-content: center;
    font-size: 24px; font-weight: 600; color: #fff;
    margin: 0 auto 16px;
    border: 3px solid rgba(181,212,244,0.35);
  }}

  .sidebar-name {{
    font-family: 'Lora', serif;
    font-size: 15px; font-weight: 600;
    color: #E6F1FB;
    text-align: center;
    padding: 0 20px;
    line-height: 1.3;
  }}

  .sidebar-title {{
    font-size: 11.5px; color: #7aaed4;
    text-align: center; padding: 6px 20px 0;
    line-height: 1.4;
  }}

  .sidebar-divider {{
    height: 1px;
    background: rgba(181,212,244,0.18);
    margin: 24px 20px;
  }}

  nav a {{
    display: flex; align-items: center; gap: 10px;
    padding: 10px 24px;
    font-size: 13px; font-weight: 500;
    color: #94c0e2;
    text-decoration: none;
    border-left: 3px solid transparent;
    transition: all 0.2s;
    letter-spacing: 0.02em;
  }}
  nav a:hover, nav a.active {{
    color: #E6F1FB;
    background: rgba(181,212,244,0.10);
    border-left-color: #4AAAF0;
  }}

  .nav-dot {{
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    opacity: 0.5;
    flex-shrink: 0;
  }}

  .sidebar-contact {{
    margin-top: auto;
    padding: 0 20px;
    font-size: 11.5px;
    color: #5e96be;
    line-height: 1.8;
  }}

  .sidebar-contact a {{
    color: #7aaed4;
    text-decoration: none;
  }}
  .sidebar-contact a:hover {{ color: #B5D4F4; }}

  /* ── Main content ── */
  #main {{
    margin-left: var(--sidebar);
    flex: 1;
    padding: 48px 52px 80px;
    max-width: 900px;
  }}

  /* ── Section ── */
  .section {{
    margin-bottom: 60px;
    scroll-margin-top: 32px;
  }}

  .section-label {{
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: var(--mid);
    text-transform: uppercase;
    margin-bottom: 6px;
  }}

  .section-title {{
    font-family: 'Lora', serif;
    font-size: 26px; font-weight: 600;
    color: var(--navy);
    margin-bottom: 28px;
    padding-bottom: 14px;
    border-bottom: 2px solid var(--pale);
  }}

  /* ── Hero / About ── */
  .hero-tag {{
    display: inline-block;
    background: var(--pale);
    color: var(--blue);
    font-size: 12px; font-weight: 500;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 18px;
    border: 1px solid var(--border);
  }}

  .hero-name {{
    font-family: 'Lora', serif;
    font-size: 36px; font-weight: 600;
    color: var(--navy);
    line-height: 1.2;
    margin-bottom: 10px;
  }}

  .hero-tagline {{
    font-size: 15px; color: var(--muted);
    line-height: 1.7; max-width: 560px;
    margin-bottom: 28px;
    font-style: italic;
    font-family: 'Lora', serif;
  }}

  .cv-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    background: var(--blue);
    color: #fff;
    font-size: 13px; font-weight: 500;
    padding: 10px 22px;
    border-radius: 8px;
    text-decoration: none;
    transition: background 0.2s, transform 0.15s;
    border: none; cursor: pointer;
  }}
  .cv-btn:hover {{ background: #0D2B45; transform: translateY(-1px); }}

  /* ── Research grid ── */
  .research-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
  }}

  /* ── Responsive ── */
  @media (max-width: 740px) {{
    :root {{ --sidebar: 0px; }}
    #sidebar {{ position: relative; width: 100%; min-height: auto; }}
    #main {{ margin-left: 0; padding: 28px 20px 60px; }}
    .hero-name {{ font-size: 26px; }}
  }}
</style>
</head>
<body>

<!-- ═══════════ SIDEBAR ═══════════ -->
<aside id="sidebar">
  <div class="avatar">{initials}</div>
  <p class="sidebar-name">{PROFILE['name']}</p>
  <p class="sidebar-title">{PROFILE['title']}<br>{PROFILE['institution']}</p>

  <div class="sidebar-divider"></div>

  <nav>
    <a href="#about" class="active"><span class="nav-dot"></span>About</a>
    <a href="#education"><span class="nav-dot"></span>Education</a>
    <a href="#research"><span class="nav-dot"></span>Research</a>
    <a href="#publications"><span class="nav-dot"></span>Publications</a>
  </nav>

  <div class="sidebar-divider"></div>

  <div class="sidebar-contact">
    <div style="margin-bottom:6px;">
      <span style="color:#4a7fa0;">✉</span>&nbsp;
      <a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a>
    </div>
    <div>
      <span style="color:#4a7fa0;">⌖</span>&nbsp;{PROFILE['location']}
    </div>
  </div>
</aside>

<!-- ═══════════ MAIN ═══════════ -->
<main id="main">

  <!-- About -->
  <section class="section" id="about">
    <div class="hero-tag">Economist &amp; Quantitative Researcher</div>
    <h1 class="hero-name">{PROFILE['name']}</h1>
    <p class="hero-tagline">{PROFILE['tagline']}</p>

    <div class="section-label">About me</div>
    <div style="border-bottom:2px solid var(--pale);padding-bottom:14px;margin-bottom:22px;"></div>

    {about_ps}

    <div style="margin-top:24px;">
      <a href="{PROFILE['cv_url']}" class="cv-btn" target="_blank">
        <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
          <path d="M3 2h9v11H3V2zm2 3h5M5 8h5M5 11h3" stroke="#fff" stroke-width="1.3" stroke-linecap="round"/>
        </svg>
        Download CV
      </a>
    </div>
  </section>

  <!-- Education -->
  <section class="section" id="education">
    <div class="section-label">Academic background</div>
    <h2 class="section-title">Education</h2>
    {edu_html}
  </section>

  <!-- Research -->
  <section class="section" id="research">
    <div class="section-label">Fields of interest</div>
    <h2 class="section-title">Research</h2>
    <div class="research-grid">
      {res_html}
    </div>
  </section>

  <!-- Publications -->
  <section class="section" id="publications">
    <div class="section-label">Papers &amp; working papers</div>
    <h2 class="section-title">Publications</h2>
    {pub_html}
  </section>

</main>

<script>
  // Highlight active nav link on scroll
  const sections = document.querySelectorAll('.section');
  const navLinks = document.querySelectorAll('nav a');
  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(e => {{
      if (e.isIntersecting) {{
        navLinks.forEach(a => a.classList.remove('active'));
        const active = document.querySelector(`nav a[href="#${{e.target.id}}"]`);
        if (active) active.classList.add('active');
      }}
    }});
  }}, {{ rootMargin: '-30% 0px -60% 0px' }});
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
