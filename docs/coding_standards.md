# 🏛️ HealthLens AI Mandatory Architecture, UI/UX & Readability Standards

> Every developer, reviewer, or judge opening any folder or file should understand its purpose within 30 seconds.

---

## 📱 Section A: Mandatory UI/UX & Web Application Rules

### 1. Mobile-First Web Application
- **Mobile-First Design**: Every page is designed for mobile screens first (320px, 375px, 390px), scaling gracefully to tablets (768px) and desktops (1024px, 1440px).
- **No Horizontal Scrolling**: Strict container boundaries with zero overflow.
- **Touch-Friendly Controls**: Minimum touch target height of `44px` (`min-h-[44px]`) for buttons, inputs, and links.

### 2. Light Theme First
- **Primary Design Language**: Clean, minimal, modern, medical, premium light mode.
- **Color Palette**: White card backgrounds (`#ffffff`), soft slate body backgrounds (`bg-slate-50`), healthcare teal (`#0d9488`), indigo accents, soft shadows (`card-shadow`).
- **Readability**: High contrast text ratios adhering to WCAG AA guidelines.

### 3. Premium UI/UX Aesthetic
- **Visual Quality Benchmark**: Apple Health, Google Fit, Notion, Linear, Stripe Dashboard.
- **Zero Clutter**: Generous whitespace, subtle card borders, no heavy blur/glassmorphism.

### 4. Component Reusability & Consistent Design System
- **No Code Duplication**: Extracted reusable primitives in `components/ui/` (`Container`, `Button`, `Card`, `Input`, `Modal`, `Table`, `Badge`, `Typography`, `LoadingSpinner`, `ErrorAlert`, `EmptyState`).
- **Design System Tokens**: Unified border radius (`rounded-2xl`), consistent card shadows, standardized typography.

---

## 🏛️ Section B: Mandatory Code Readability & Repository Rules

### 1. Feature-First Structure
Organize folders by **Features & Modules**, never by generic dump names (`misc/`, `utils2/`).

### 2. File Responsibility & 30-Second Rule
One file = One clear responsibility. Filenames describe their exact purpose (`health_score.py`, `report_repository.py`).
> *"Can a new developer locate any feature in under 30 seconds?"* If no, reorganize before writing code.

### 3. Header Block Standards
- Python files: `# --------------------------------------------------` header comment block.
- TypeScript/React files: `/* -------------------------------------------------- */` block comment.

### 4. Self-Explanatory Variable & Function Names
Never use vague single-letter variables (`x`, `a`, `temp`, `val`). Use `extracted_report`, `health_score`, `normalized_parameter`, `critical_alert`.
