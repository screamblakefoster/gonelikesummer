BASE_CSS = '''
    :root {
      --bg: #f7f5f0;
      --fg: #1a1a1a;
      --muted: #767267;
      --card-bg: #eae6dc;
      --line: #e2ddd0;
    }

    * {
      box-sizing: border-box;
    }

    html,
    body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--fg);
    }

    body {
      font-family: "Times New Roman", Times, serif;
      font-weight: 400;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    header {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 65px 30px 50px;
      text-align: center;
    }

    .site-title {
      font-size: 44px;
      letter-spacing: 0.01em;
      margin: 0;
      font-weight: 400;
    }

    .site-title a {
      display: inline-block;
    }

    .logo-img {
      height: 90px;
      width: auto;
      display: block;
    }

    .site-subtitle {
      color: var(--muted);
      font-size: 15px;
      margin-top: 10px;
      font-style: italic;
    }

    nav {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 34px;
      font-size: 18px;
      line-height: 1;
      margin-top: 26px;
    }

    nav a {
      color: var(--fg);
      opacity: 0.55;
      text-decoration: none;
      transition: opacity 0.2s ease;
    }

    nav a:hover {
      opacity: 1;
    }

    nav a.active {
      opacity: 1;
      text-decoration: underline;
      text-underline-offset: 6px;
      text-decoration-thickness: 1px;
    }

    footer {
      padding: 40px 30px;
      color: var(--muted);
      font-size: 12px;
      text-align: center;
      border-top: 1px solid var(--line);
      margin-top: 20px;
    }

    @media (max-width: 900px) {
      header {
        padding: 50px 20px 40px;
      }
      .site-title {
        font-size: 36px;
      }
      .logo-img {
        height: 72px;
      }
      nav {
        gap: 24px;
        font-size: 16px;
      }
    }

    @media (max-width: 650px) {
      header {
        padding: 40px 18px 30px;
      }
      .site-title {
        font-size: 30px;
      }
      .logo-img {
        height: 60px;
      }
      nav {
        gap: 16px;
        flex-wrap: wrap;
        font-size: 15px;
      }
    }
'''

SHOP_URL = "https://wun6e0-uf.myshopify.com"

def nav(active):
    items = [
        ("music", "music.html", False),
        ("shows", "shows.html", False),
        ("about", "about.html", False),
        ("videos", "videos.html", False),
        ("panda", "panda.html", False),
        ("shop", SHOP_URL, False),
    ]
    links = []
    for label, href, external in items:
        extra = ' target="_blank" rel="noopener noreferrer"' if external else ''
        if label == active:
            links.append(f'<a class="active" href="{href}" aria-current="page"{extra}>{label}</a>')
        else:
            links.append(f'<a href="{href}"{extra}>{label}</a>')
    return "\n      ".join(links)

def header(active, subtitle=None):
    return f'''  <header>
    <h1 class="site-title"><a href="index.html"><img class="logo-img" src="logo.png" alt="gone like summer"></a></h1>

    <nav aria-label="Main navigation">
      {nav(active)}
    </nav>
  </header>'''

FOOTER = '''  <footer>
    © 2026 gone like summer
  </footer>'''
