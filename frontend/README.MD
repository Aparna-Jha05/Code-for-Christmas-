# 📁 Frontend – Sybil-Resistant Airdrop Demo

This frontend is a **pure visualization layer** for the **Airdrop Trust Protocol**.

## It Does NOT:
- Make decisions
- Compute scores
- Enforce rules

## It ONLY:
- Sends user input to the backend
- Displays backend outputs exactly as returned

**All authority lives on the backend.**

---

## Tech Stack

- Plain HTML
- Vanilla JavaScript
- CSS
- No frameworks (by design)

### Reason:
- Fast debugging
- No hidden abstractions
- Judge-friendly clarity

---

## Folder Structure
```
frontend/
├── index.html      # Main UI
├── app.js          # UI logic + DOM updates
├── api.js          # Backend communication
├── styles.css      # Styling
└── README.md       # This file
```

---

## How the Frontend Is Served

**IMPORTANT:**
- This frontend **MUST** be served over HTTP
- **DO NOT** open `index.html` using `file://`

### Correct way:
```bash
cd frontend
python -m http.server 5500
```

Open: `http://localhost:5500/index.html`

### Reason:
Browsers restrict `fetch()` from `file://` origins

---

## index.html (UI Structure)

### Purpose
Defines all UI elements and connects them to JavaScript handlers.

### Key Elements

#### Wallet Input
```html
<textarea id="wallets" rows="4"></textarea>
```
- **ID:** `wallets`
- **Input format:** one wallet per line
- **Example:**
```
  0xA1
  0xA2
  0xB1
```

#### Analyze Button
```html
<button onclick="analyze()">Analyze</button>
```
- Calls `analyze()` in `app.js`

#### Analysis Result Table
```html
<table id="analysisTable">
  <thead>
    <tr>
      <th>Wallet</th>
      <th>Sybil Score</th>
      <th>Bucket</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>
```
- **ID:** `analysisTable`
- `<tbody>` is dynamically populated by JS

#### Airdrop Section
```html
<button onclick="runAirdrop()">Run Airdrop</button>

<table id="airdropTable">
  <thead>
    <tr>
      <th>Wallet</th>
      <th>Tokens</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>
```
- **ID:** `airdropTable`
- Populated only after clicking **Run Airdrop**

---

## api.js (Backend Communication)

### Purpose
Centralizes all HTTP calls to backend.

### Configuration
```javascript
const API_BASE = "http://127.0.0.1:8000";
```
⚠️ If backend port changes, update here.

### POST helper
```javascript
post(endpoint, data)
```
Used by:
- `/analyze`

### GET helper
```javascript
get(endpoint)
```
Used by:
- `/airdrop`

---

## app.js (Frontend Logic)

This file contains **ALL frontend behavior**.

### analyze()

**Triggered by:**
```html
<button onclick="analyze()">
```

**Flow:**
1. Read wallet list from textarea `#wallets`
2. POST to `/analyze`
3. Expect response: Array
4. Clear `#analysisTable tbody`
5. Render one row per wallet

**Expected backend response shape:**
```json
[
  {
    "wallet": "0xA1",
    "sybil_score": 0.75,
    "bucket": "HIGH",
    "explanation": "...",
    "confidence": "HIGH",
    "model_version": "sybil-linear-v1",
    "hash": "abc123"
  }
]
```

### runAirdrop()

**Triggered by:**
```html
<button onclick="runAirdrop()">
```

**Flow:**
1. GET `/airdrop`
2. Extract `result.results`
3. Clear `#airdropTable tbody`
4. Render wallet + token rows

**Expected backend response shape:**
```json
{
  "mode": "trust-weighted-airdrop",
  "results": [
    { "wallet": "0xA1", "tokens": 100 },
    { "wallet": "0xA2", "tokens": 10 }
  ]
}
```

---

## Rules (DO NOT BREAK)

1. Frontend **NEVER** computes scores
2. Frontend **NEVER** assigns buckets
3. Frontend **NEVER** decides rewards
4. Frontend **NEVER** modifies backend data

**Frontend = glass box, backend = brain.**

---

## Debugging Tips

- Always check browser **Console**
- If tables don't update, log response shape
- 99% bugs are mismatched JSON structure

---

## One-Sentence Summary

This frontend is a **dumb renderer** that visualizes trust decisions made elsewhere.