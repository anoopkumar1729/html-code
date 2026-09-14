/* ==========================================
   CYBER BLUEPRINT BACKGROUND STYLES
   ========================================== */

/* 1. Base Background & Tech Grid */
body {
  margin: 0;
  padding: 0;
  background-color: #080c14; /* Deep Cyber Dark Theme */
  
  /* High-Tech Grid Pattern */
  background-image: 
    linear-gradient(rgba(0, 243, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 243, 255, 0.05) 1px, transparent 1px);
  background-size: 40px 40px; /* Grid Box Size */
  background-position: -1px -1px;
  background-attachment: fixed; /* Scrolling par grid fixed rahegi */

  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  color: #f0f6fc;
}

/* 2. Ambient Neon Glow Spheres (Soft Lights) */
.bg-glow-cyan {
  position: fixed;
  top: -150px;
  left: -150px;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 243, 255, 0.09) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.bg-glow-purple {
  position: fixed;
  bottom: -150px;
  right: -150px;
  width: 700px;
  height: 700px;
  background: radial-gradient(circle, rgba(176, 38, 255, 0.08) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

/* 3. Typography Watermark Texts */
.bg-watermark {
  position: fixed;
  font-family: 'Space Grotesk', 'Impact', sans-serif;
  font-weight: 900;
  font-size: clamp(4rem, 12vw, 9rem);
  color: rgba(255, 255, 255, 0.02); /* Very faint & clean opacity */
  letter-spacing: 12px;
  user-select: none;
  pointer-events: none;
  text-transform: uppercase;
  z-index: 0;
  white-space: nowrap;
}

.wm-top-left {
  top: 10px;
  left: -10px;
}

.wm-bottom-right {
  bottom: 10px;
  right: -10px;
}

/* 4. Ensure Your Main Portfolio Content Stays Above Background */
.main-content {
  position: relative;
  z-index: 1; /* Keep text/cards above the background */
}