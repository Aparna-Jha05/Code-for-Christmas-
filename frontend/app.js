const loader = document.getElementById("loader");
const statusText = document.getElementById("statusText");
const analysisSection = document.getElementById("analysisSection");
const airdropSection = document.getElementById("airdropSection");
const textarea = document.getElementById("wallets");

let debounceTimer = null;

textarea.addEventListener("input", () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(runPipeline, 600);
});

async function runPipeline() {
  const wallets = textarea.value
    .split("\n")
    .map(w => w.trim())
    .filter(Boolean);

  if (wallets.length === 0) return;

  resetUI();
  showLoader("Analyzing wallets…");

  // ---- ANALYZE ----
  const analyzeRes = await post("/analyze", { wallets });
  renderAnalysis(analyzeRes.results);   // ✅ FIX

  hideLoader();
  analysisSection.classList.remove("hidden");

  await delay(600);

  // ---- AIRDROP ----
  showLoader("Running airdrop distribution…");
  const airdropRes = await get("/airdrop");
  renderAirdrop(airdropRes.results);

  hideLoader();
  airdropSection.classList.remove("hidden");
}

function renderAnalysis(data) {
  const tbody = document.querySelector("#analysisTable tbody");
  tbody.innerHTML = "";

  data.forEach(r => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${r.wallet}</td>
      <td>${r.sybil_score}</td>
      <td>${r.bucket}</td>
      <td>${r.explanation}</td>
    `;
    tbody.appendChild(row);
  });
}

function renderAirdrop(data) {
  const tbody = document.querySelector("#airdropTable tbody");
  tbody.innerHTML = "";

  data.forEach(r => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${r.wallet}</td>
      <td>${r.bucket}</td>
      <td>${r.tokens}</td>
    `;
    tbody.appendChild(row);
  });
}

function resetUI() {
  analysisSection.classList.add("hidden");
  airdropSection.classList.add("hidden");
  statusText.textContent = "";
}

function showLoader(text) {
  loader.classList.remove("hidden");
  statusText.textContent = text;
}

function hideLoader() {
  loader.classList.add("hidden");
  statusText.textContent = "";
}

function delay(ms) {
  return new Promise(res => setTimeout(res, ms));
}
