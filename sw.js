// Service worker: app mở được khi mất mạng.
// Trang chính: lấy bản mới từ mạng trước, mất mạng thì dùng bản đã lưu (bỏ qua ?fam=…).
// Thư viện Firebase, html2canvas, phông chữ: lưu lại sau lần tải đầu.
// Không chặn kết nối Firestore (googleapis), Firebase tự lo phần ngoại tuyến.
const CACHE = "mochi-v4";
const CORE = ["./", "./index.html", "./manifest.webmanifest", "./assets/apple-touch-icon.png", "./assets/logo-512.png", "./assets/icon-192.png", "./reminders.ics"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.hostname.endsWith("googleapis.com") && !url.hostname.startsWith("fonts.")) return;
  if (req.mode === "navigate") {
    e.respondWith(
      fetch(req).then(res => {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put("./index.html", copy));
        return res;
      }).catch(() => caches.match("./index.html").then(r => r || caches.match("./")))
    );
    return;
  }
  const cdn = ["www.gstatic.com", "cdnjs.cloudflare.com", "fonts.googleapis.com", "fonts.gstatic.com"].includes(url.hostname);
  if (cdn || url.origin === self.location.origin) {
    e.respondWith(
      caches.match(req, { ignoreSearch: url.origin === self.location.origin }).then(hit => {
        const net = fetch(req).then(res => {
          if (res && (res.ok || res.type === "opaque")) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
          return res;
        }).catch(() => hit);
        return hit || net;
      })
    );
  }
});
