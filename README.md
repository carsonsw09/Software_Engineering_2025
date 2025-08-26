# CMU Campus Events 🎓📅

An open-source event planner for **Colorado Mesa University (CMU)** that helps students discover what’s happening across campus — from **clubs** and **sports** to **talks**, **meetups**, and more. Browse events on a calendar, save your favorites, get notifications, and see where everything is on a **live map**.

> Find it. Save it. Show up. 🙌

---

## ✨ Features

- **Campus-wide events feed**: Clubs, athletics, departments, and community partners.
- **Interactive calendar**: List, day, week, and month views.
- **Saved events & reminders**: Bookmark events and get notified before they start.
- **Geo map**: Pinpoint event locations across campus with routing-friendly links.
- **Smart filters**: By category (club/sports/academic), date, location, or tags.
- **Search**: Fuzzy, fast, and typo-tolerant.
- **Mobile-friendly**: Works great on phones and desktops.
- **Role-based admin**: Event creators can submit and manage listings (optional approval workflow).

---

## 🧱 Tech Stack (suggested)

- **Frontend**: React (Vite) or Next.js, Tailwind CSS, Map library (Leaflet/Mapbox GL)
- **Backend**: Node.js + Express (or FastAPI), REST/GraphQL
- **Database**: PostgreSQL (or SQLite for dev)
- **Auth**: JWT or university SSO integration
- **Notifications**: Web Push + Email (e.g., Firebase/OneSignal/SendGrid)
- **Maps/Geocoding**: OpenStreetMap + Nominatim (or Mapbox/Google Maps)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker + docker-compose

> Swap components as needed — this README focuses on behavior, not strict implementations.

---

## 🗺️ Core Concepts

### Events
- **Fields**: `title`, `description`, `start_time`, `end_time`, `category`, `location_name`, `lat`, `lng`, `organizer`, `tags`, `image_url`, `capacity` (optional), `rsvp_link` (optional)
- **Status**: `scheduled`, `canceled`, `postponed`

### Users
- **Fields**: `email`, `name`, `role` (`student`, `organizer`, `admin`)
- **Prefs**: categories of interest, notification settings, time zone

### Saved & Notifications
- Users can **save** an event ⭐ and opt-in to **notifications** 🔔:
  - `24h` before
  - `2h` before
  - `15m` before

---

## 📸 Screens (planned)

- **Calendar View** (month/week/day)  
- **Event Details** (title, description, map, save button, share)  
- **Map View** (clustered markers, filter chips)  
- **My Saved** (upcoming reminders)  
- **Admin Panel** (create/edit events)  

> Add screenshots to `/docs/screens/` and link them here when ready.

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ & npm (or pnpm/yarn)
- Docker & docker-compose (for DB and easy dev)
- (Optional) Map/Email/Push provider API keys

### Clone
```bash
git clone https://github.com/your-org/cmu-campus-events.git
cd cmu-campus-events
