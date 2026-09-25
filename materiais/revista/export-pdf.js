// export-pdf.js — exporta as duas revistas em PDF (1 spread por página A4 paisagem).
//
// Uso, da raiz do repo:
//   node materiais/revista/export-pdf.js
//
// O que faz: sobe um `python3 -m http.server` temporário na raiz do repo (as
// revistas carregam fotos de ../../assets e ../assets, então precisam de servidor),
// abre cada HTML no Chromium headless do Playwright, espera as fontes do Google
// terminarem de carregar e chama page.pdf com preferCSSPageSize — o @page do
// revista.css (A4 landscape, margin 0) manda no tamanho da folha.
//
// Requisitos: Node 22 + Playwright global e Chromium já baixado (caminhos abaixo;
// ajustar as duas constantes se a máquina for outra). Precisa de internet só pras
// fontes — sem rede, o PDF sai com Georgia/Arial/Courier no lugar.

const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

const PLAYWRIGHT = process.env.PLAYWRIGHT_PATH || '/opt/node22/lib/node_modules/playwright';
const CHROME = process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
const PORT = Number(process.env.PORT) || 4179;

const REPO = path.resolve(__dirname, '..', '..');
const OUT = __dirname;
const PIECES = [
  { html: 'materiais/revista/visita.html', pdf: 'visita.pdf' },
  { html: 'materiais/revista/formacion.html', pdf: 'formacion.pdf' },
];

const { chromium } = require(PLAYWRIGHT);

function waitForServer(url, tries = 40) {
  return new Promise((resolve, reject) => {
    const http = require('http');
    const tick = (n) => {
      http.get(url, (res) => { res.resume(); resolve(); })
        .on('error', () => n > 0 ? setTimeout(() => tick(n - 1), 250) : reject(new Error('servidor não subiu')));
    };
    tick(tries);
  });
}

// Conta páginas lendo os objetos /Type /Page do PDF (sem depender de pypdf).
function countPages(file) {
  const buf = fs.readFileSync(file, 'latin1');
  const m = buf.match(/\/Type\s*\/Page(?![s])/g);
  return m ? m.length : 0;
}

(async () => {
  const server = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: REPO, stdio: 'ignore' });
  try {
    await waitForServer(`http://127.0.0.1:${PORT}/`);
    const browser = await chromium.launch({ executablePath: CHROME });
    const page = await browser.newPage({ viewport: { width: 1400, height: 990 } });

    for (const piece of PIECES) {
      const url = `http://127.0.0.1:${PORT}/${piece.html}`;
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.emulateMedia({ media: 'print' });
      await page.evaluate(() => document.fonts.ready);
      // garante que todas as imagens decodificaram antes de imprimir
      await page.evaluate(() => Promise.all(
        Array.from(document.images).map((img) => img.complete ? Promise.resolve() : new Promise((r) => { img.onload = img.onerror = r; }))
      ));
      const out = path.join(OUT, piece.pdf);
      await page.pdf({ path: out, format: 'A4', landscape: true, printBackground: true, preferCSSPageSize: true });
      const spreads = await page.evaluate(() => document.querySelectorAll('.spread').length);
      const pages = countPages(out);
      const kb = Math.round(fs.statSync(out).size / 1024);
      console.log(`${piece.pdf}: ${pages} páginas (${spreads} spreads no HTML) · ${kb} KB`);
      if (pages !== spreads) console.warn(`  AVISO: número de páginas difere do número de spreads — conferir overflow.`);
    }
    await browser.close();
  } finally {
    server.kill();
  }
})().catch((err) => { console.error(err); process.exit(1); });
