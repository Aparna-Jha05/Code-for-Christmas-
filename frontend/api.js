const API_BASE = "http://localhost:8000";

async function post(endpoint, data) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
}

async function get(endpoint) {
  const res = await fetch(`${API_BASE}${endpoint}`);
  return res.json();
}
