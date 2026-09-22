
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI/ML Engineer Profile</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    /* ========== RESET & BASE ========== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --bg: #0d1117;
      --bg-elevated: #161b22;
      --bg-cell: #0f1419;
      --border: #21262d;
      --border-hover: #30363d;
      --text: #e6edf3;
      --text-muted: #8b949e;
      --text-dim: #6e7681;
      --orange: #f78166;
      --pink: #f778ba;
      --blue: #58a6ff;
      --gray: #8b949e;
      --green: #3fb950;
      --purple: #a371f7;
      --cyan: #39c5cf;
      --radius: 12px;
      --radius-sm: 8px;
      --transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Subtle noise / gradient for depth */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(88, 166, 255, 0.08), transparent),
        radial-gradient(ellipse 60% 40% at 80% 60%, rgba(247, 129, 102, 0.05), transparent);
      pointer-events: none;
      z-index: 0;
    }

    .container {
      position: relative;
      z-index: 1;
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 24px 80px;
    }

    /* ========== TYPEWRITER HERO ========== */
    .hero {
      min-height: 42vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 80px 20px 60px;
      text-align: center;
    }

    .hero-label {
      font-size: 0.8rem;
      font-weight: 500;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-bottom: 24px;
      opacity: 0;
      animation: fadeUp 0.6s ease forwards 0.2s;
    }

    .typewriter-wrap {
      min-height: 3.2em;
      display: flex;
      align-items: center;
      justify-content: center;
      max-width: 900px;
    }

    .typewriter {
      font-size: clamp(1.5rem, 4vw, 2.35rem);
      font-weight: 600;
      letter-spacing: -0.02em;
      color: var(--text);
      line-height: 1.35;
      position: relative;
      opacity: 0;
      transform: scale(0.98);
      transition: opacity 0.35s ease, transform 0.35s ease;
    }

    .typewriter.visible {
      opacity: 1;
      transform: scale(1);
    }

    .typewriter .cursor {
      display: inline-block;
      width: 2px;
      height: 1.1em;
      background: var(--orange);
      margin-left: 3px;
      vertical-align: text-bottom;
      animation: blink 0.85s step-end infinite;
      border-radius: 1px;
    }

    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }

    @keyframes fadeUp {
      from {
        opacity: 0;
        transform: translateY(16px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* ========== SECTION COMMON ========== */
    section {
      margin-top: 64px;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 28px;
      opacity: 0;
      transform: translateY(20px) scale(0.98);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .section-header.in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    .section-header .icon {
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      background: rgba(247, 129, 102, 0.12);
      color: var(--orange);
      flex-shrink: 0;
    }

    .section-header .icon svg {
      width: 16px;
      height: 16px;
    }

    .section-header h2 {
      font-size: 1.25rem;
      font-weight: 600;
      letter-spacing: -0.01em;
      color: var(--text);
    }

    /* ========== AREAS OF FOCUS ========== */
    .focus-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }

    .focus-card {
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px 22px;
      position: relative;
      overflow: hidden;
      opacity: 0;
      transform: translateY(24px) scale(0.97);
      transition:
        opacity 0.5s ease,
        transform 0.5s ease,
        border-color var(--transition),
        box-shadow var(--transition);
    }

    .focus-card.in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    .focus-card::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 3px;
      background: var(--accent);
      transform: scaleY(0.4);
      transform-origin: center;
      transition: transform 0.3s ease;
      border-radius: 0 2px 2px 0;
    }

    .focus-card:hover {
      border-color: var(--border-hover);
      box-shadow: 0 8px 24px -8px rgba(0, 0, 0, 0.4),
                  0 0 0 1px rgba(255, 255, 255, 0.03);
      transform: translateY(-3px);
    }

    .focus-card:hover::before {
      transform: scaleY(1);
    }

    .focus-card[data-accent="pink"] { --accent: var(--pink); }
    .focus-card[data-accent="gray"] { --accent: var(--gray); }
    .focus-card[data-accent="blue"] { --accent: var(--blue); }

    .focus-card h3 {
      font-size: 0.95rem;
      font-weight: 600;
      margin-bottom: 14px;
      color: var(--accent);
      letter-spacing: -0.01em;
    }

    .focus-card ul {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .focus-card li {
      font-size: 0.875rem;
      color: var(--text-muted);
      padding-left: 14px;
      position: relative;
    }

    .focus-card li::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0.55em;
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--accent);
      opacity: 0.7;
    }

    /* ========== TECH STACK ========== */
    .stack-categories {
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .stack-category {
      opacity: 0;
      transform: translateY(20px) scale(0.98);
      transition: opacity 0.5s ease, transform 0.5s ease;
    }

    .stack-category.in-view {
      opacity: 1;
      transform: translateY(0) scale(1);
    }

    .stack-category h3 {
      font-size: 0.8rem;
      font-weight: 500;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-bottom: 14px;
      text-align: center;
    }

    .badges {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 7px 14px;
      font-size: 0.8125rem;
      font-weight: 500;
      border-radius: 999px;
      background: var(--bg-elevated);
      border: 1px solid var(--border);
      color: var(--text);
      transition:
        transform var(--transition),
        box-shadow var(--transition),
        border-color var(--transition),
        background var(--transition);
      cursor: default;
      letter-spacing: -0.01em;
    }

    .badge:hover {
      transform: translateY(-2px);
      border-color: var(--badge-color, var(--border-hover));
      box-shadow: 0 4px 16px -4px color-mix(in srgb, var(--badge-color, #58a6ff) 35%, transparent);
      background: color-mix(in srgb, var(--badge-color, #58a6ff) 8%, var(--bg-elevated));
    }

    /* Brand-ish colors for badges */
    .badge[data-color="python"]   { --badge-color: #3776ab; }
    .badge[data-color="c"]        { --badge-color: #a8b9cc; }
    .badge[data-color="csharp"]   { --badge-color: #68217a; }
    .badge[data-color="go"]       { --badge-color: #00add8; }
    .badge[data-color="numpy"]    { --badge-color: #4dabcf; }
    .badge[data-color="pandas"]   { --badge-color: #150458; }
    .badge[data-color="matplotlib"]{ --badge-color: #11557c; }
    .badge[data-color="seaborn"]  { --badge-color: #4c72b0; }
    .badge[data-color="sklearn"]  { --badge-color: #f7931e; }
    .badge[data-color="tf"]       { --badge-color: #ff6f00; }
    .badge[data-color="pytorch"]  { --badge-color: #ee4c2c; }
    .badge[data-color="opencv"]   { --badge-color: #5c3ee8; }
    .badge[data-color="xgboost"]  { --badge-color: #1a73e8; }
    .badge[data-color="langchain"]{ --badge-color: #1c3c3c; }
    .badge[data-color="langgraph"]{ --badge-color: #2d6a4f; }
    .badge[data-color="transformers"]{ --badge-color: #ffd21e; }
    .badge[data-color="hf"]       { --badge-color: #ffd21e; }
    .badge[data-color="mongo"]    { --badge-color: #47a248; }
    .badge[data-color="redis"]    { --badge-color: #dc382d; }
    .badge[data-color="docker"]   { --badge-color: #2496ed; }
    .badge[data-color="k8s"]      { --badge-color: #326ce5; }
    .badge[data-color="aws"]      { --badge-color: #ff9900; }
    .badge[data-color="postman"]  { --badge-color: #ff6c37; }
    .badge[data-color="github"]   { --badge-color: #e6edf3; }
    .badge[data-color="vscode"]   { --badge-color: #007acc; }
    .badge[data-color="cursor"]   { --badge-color: #7c3aed; }

    /* ========== FOOTER NOTE ========== */
    .footer-note {
      margin-top: 72px;
      text-align: center;
      font-size: 0.8rem;
      color: var(--text-dim);
      opacity: 0;
      transition: opacity 0.5s ease;
    }

    .footer-note.in-view {
      opacity: 1;
    }

    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {
      .focus-grid {
        grid-template-columns: 1fr;
        gap: 12px;
      }

      .hero {
        min-height: 36vh;
        padding: 60px 16px 48px;
      }

      .typewriter {
        font-size: clamp(1.25rem, 5vw, 1.75rem);
      }

      section {
        margin-top: 48px;
      }
    }

    @media (max-width: 480px) {
      .container {
        padding: 0 16px 60px;
      }

      .badge {
        padding: 6px 12px;
        font-size: 0.78rem;
      }
    }

    /* Reduced motion */
    @media (prefers-reduced-motion: reduce) {
      .typewriter .cursor {
        animation: none;
        opacity: 1;
      }
      .focus-card,
      .stack-category,
      .section-header,
      .footer-note {
        transition: none;
        opacity: 1;
        transform: none;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- ========== TYPEWRITER HERO ========== -->
    <header class="hero">
      <p class="hero-label">Senior AI / ML Engineer</p>
      <div class="typewriter-wrap">
        <h1 class="typewriter" id="typewriter" aria-live="polite">
          <span class="text"></span><span class="cursor" aria-hidden="true"></span>
        </h1>
      </div>
    </header>

    <!-- ========== AREAS OF FOCUS ========== -->
    <section id="focus" aria-labelledby="focus-heading">
      <div class="section-header" data-animate>
        <div class="icon" aria-hidden="true">
          <!-- Target / compass icon -->
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>
          </svg>
        </div>
        <h2 id="focus-heading">Areas of Focus</h2>
      </div>

      <div class="focus-grid">
        <article class="focus-card" data-accent="pink" data-animate data-delay="0">
          <h3>AI / ML</h3>
          <ul>
            <li>Machine Learning</li>
            <li>Deep Learning</li>
            <li>Computer Vision</li>
            <li>LLMs &amp; Agentic AI</li>
          </ul>
        </article>

        <article class="focus-card" data-accent="gray" data-animate data-delay="80">
          <h3>Backend</h3>
          <ul>
            <li>REST API Design</li>
            <li>System Design</li>
            <li>Distributed Systems</li>
            <li>Database Engineering</li>
          </ul>
        </article>

        <article class="focus-card" data-accent="blue" data-animate data-delay="160">
          <h3>Cloud &amp; MLOps</h3>
          <ul>
            <li>AWS</li>
            <li>Docker &amp; Kubernetes</li>
            <li>CI/CD Pipelines</li>
            <li>MLOps Workflows</li>
          </ul>
        </article>
      </div>
    </section>

    <!-- ========== TECH STACK ========== -->
    <section id="stack" aria-labelledby="stack-heading">
      <div class="section-header" data-animate>
        <div class="icon" aria-hidden="true">
          <!-- Wrench / tools icon -->
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
          </svg>
        </div>
        <h2 id="stack-heading">Tech Stack</h2>
      </div>

      <div class="stack-categories">
        <!-- Languages -->
        <div class="stack-category" data-animate data-delay="0">
          <h3>Languages</h3>
          <div class="badges">
            <span class="badge" data-color="python">Python</span>
            <span class="badge" data-color="c">C</span>
            <span class="badge" data-color="csharp">C#</span>
            <span class="badge" data-color="go">Go</span>
          </div>
        </div>

        <!-- AI / ML -->
        <div class="stack-category" data-animate data-delay="60">
          <h3>AI / Machine Learning</h3>
          <div class="badges">
            <span class="badge" data-color="numpy">NumPy</span>
            <span class="badge" data-color="pandas">Pandas</span>
            <span class="badge" data-color="matplotlib">Matplotlib</span>
            <span class="badge" data-color="seaborn">Seaborn</span>
            <span class="badge" data-color="sklearn">Scikit-learn</span>
            <span class="badge" data-color="tf">TensorFlow</span>
            <span class="badge" data-color="pytorch">PyTorch</span>
            <span class="badge" data-color="opencv">OpenCV</span>
            <span class="badge" data-color="xgboost">XGBoost</span>
            <span class="badge" data-color="langchain">LangChain</span>
            <span class="badge" data-color="langgraph">LangGraph</span>
            <span class="badge" data-color="transformers">Transformers</span>
            <span class="badge" data-color="hf">Hugging Face</span>
          </div>
        </div>

        <!-- Data & Infrastructure -->
        <div class="stack-category" data-animate data-delay="120">
          <h3>Data &amp; Infrastructure</h3>
          <div class="badges">
            <span class="badge" data-color="mongo">MongoDB</span>
            <span class="badge" data-color="redis">Redis</span>
            <span class="badge" data-color="docker">Docker</span>
            <span class="badge" data-color="k8s">Kubernetes</span>
            <span class="badge" data-color="aws">AWS</span>
          </div>
        </div>

        <!-- Tooling -->
        <div class="stack-category" data-animate data-delay="180">
          <h3>Tooling</h3>
          <div class="badges">
            <span class="badge" data-color="postman">Postman</span>
            <span class="badge" data-color="github">GitHub</span>
            <span class="badge" data-color="vscode">VS Code</span>
            <span class="badge" data-color="cursor">Cursor</span>
          </div>
        </div>
      </div>
    </section>

    <p class="footer-note" data-animate>
      Production-minded · Research-aware · Cloud-native
    </p>
  </div>

  <script>
    /* ========== TYPEWRITER ENGINE ========== */
    (function () {
      const lines = [
        "Building production-grade applications with AI & ML",
        "Designing scalable systems powered by Deep Learning",
        "Engineering intelligent solutions with LLMs & Agentic AI",
        "Shipping robust ML pipelines from research to production",
        "Architecting end-to-end AI systems on Cloud & MLOps"
      ];

      const el = document.getElementById("typewriter");
      const textEl = el.querySelector(".text");
      let lineIndex = 0;
      let charIndex = 0;
      let isDeleting = false;
      let isPaused = false;

      // Timing (ms) — tuned for a senior, deliberate feel
      const TYPE_SPEED = 42;
      const DELETE_SPEED = 28;
      const PAUSE_AFTER_TYPE = 2200;
      const PAUSE_AFTER_DELETE = 400;

      function setVisible(state) {
        if (state) el.classList.add("visible");
        else el.classList.remove("visible");
      }

      function tick() {
        const current = lines[lineIndex];

        if (!isDeleting && !isPaused) {
          // Typing
          charIndex++;
          textEl.textContent = current.slice(0, charIndex);
          setVisible(true);

          if (charIndex === current.length) {
            isPaused = true;
            setTimeout(() => {
              isPaused = false;
              isDeleting = true;
              tick();
            }, PAUSE_AFTER_TYPE);
            return;
          }
          setTimeout(tick, TYPE_SPEED + Math.random() * 18);
        } else if (isDeleting && !isPaused) {
          // Deleting
          charIndex--;
          textEl.textContent = current.slice(0, charIndex);

          if (charIndex === 0) {
            isDeleting = false;
            isPaused = true;
            // Subtle scale fade between lines
            setVisible(false);
            setTimeout(() => {
              lineIndex = (lineIndex + 1) % lines.length;
              isPaused = false;
              setVisible(true);
              tick();
            }, PAUSE_AFTER_DELETE);
            return;
          }
          setTimeout(tick, DELETE_SPEED);
        }
      }

      // Kick off after a short delay so the page feels settled
      setTimeout(tick, 600);
    })();

    /* ========== SCROLL-TRIGGERED ENTRANCE ========== */
    (function () {
      const items = document.querySelectorAll("[data-animate]");

      if (!("IntersectionObserver" in window)) {
        items.forEach((el) => el.classList.add("in-view"));
        return;
      }

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const delay = parseInt(entry.target.dataset.delay || "0", 10);
              setTimeout(() => {
                entry.target.classList.add("in-view");
              }, delay);
              observer.unobserve(entry.target);
            }
          });
        },
        {
          threshold: 0.12,
          rootMargin: "0px 0px -40px 0px"
        }
      );

      items.forEach((el) => observer.observe(el));
    })();
  </script>
</body>
</html>
