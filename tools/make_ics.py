"""Tạo reminders.ics: nhắc việc buổi tối và nhắc đi chợ cho lộ trình ăn dặm 5 tuần của Mochi.

Chạy: python3 tools/make_ics.py  (ghi ra reminders.ics ở thư mục gốc repo)
Ngày 1 = thứ Hai 02/11/2026. Giờ Việt Nam (UTC+7).
"""
import datetime as dt
from pathlib import Path

START = dt.date(2026, 11, 2)
EVENING = dt.time(19, 49)
MORNING = dt.time(7, 46)
TZ = dt.timezone(dt.timedelta(hours=7))


def date_of(n):
    return START + dt.timedelta(days=n - 1)


# Món chính theo ngày (để suy ra cần chuẩn bị gì tối hôm trước)
def meals(n):
    if n <= 9:
        return {"chao": False, "thaw": [], "egg": n >= 10}
    if n <= 14:
        return {"chao": False, "thaw": [], "egg": True}
    if n == 15:
        return {"chao": True, "thaw": [], "egg": True}
    if n <= 18:
        return {"chao": True, "thaw": ["1 phần thịt lợn"], "egg": False}
    if n <= 21:
        return {"chao": True, "thaw": ["1 phần thịt bò"], "egg": False}
    if n <= 24:
        return {"chao": True, "thaw": ["1 phần thịt lợn"], "egg": True}
    if n <= 27:
        return {"chao": True, "thaw": ["1 miếng cá hồi", "1 phần thịt bò"], "egg": False}
    if n == 28:
        return {"chao": True, "thaw": ["1 phần thịt bò", "1 phần thịt lợn"], "egg": False}
    return {"chao": True, "thaw": ["1 phần thịt bò"], "egg": False}


NEW_FOOD = {
    1: "Mai Mochi bắt đầu ăn dặm! Bột HiPP gạo pha sữa HiPP, ngày 1 chỉ 2–3 thìa cà phê.",
    4: "Mai bắt đầu món mới: bí đỏ (hấp sáng mai, 10 g).",
    7: "Mai bắt đầu món mới: khoai lang (hấp sáng mai, 10 g).",
    10: "Mai bắt đầu món mới: lòng đỏ trứng, chỉ ¼ lòng đỏ, luộc chín kỹ 10 phút.",
    13: "Mai bắt đầu món mới: rau ngót.",
    15: "Mai chuyển từ bột sang cháo rây.",
    16: "Mai bắt đầu món mới: thịt lợn, dùng nửa phần.",
    19: "Mai bắt đầu món mới: thịt bò, dùng nửa phần.",
    22: "Mai bắt đầu 2 bữa/ngày và món mới đu đủ (chỉ 1 thìa cà phê sau cháo).",
    25: "Mai bắt đầu món mới: cá hồi, dùng nửa miếng, gỡ kỹ xương.",
    29: "Mai bắt đầu bột Bellamy's táo quế (yến mạch, táo, quế, gluten): theo dõi kỹ 3 ngày.",
}

# Đi chợ: (số ngày của bữa đầu tiên dùng đồ, tiêu đề, danh sách)
SHOP = [
    (0, "Đi chợ tuần 1", "Bột HiPP gạo nhũ nhi 1 hộp; sữa HiPP số 2 nếu sắp hết; bí đỏ 200 g; khoai lang 250 g; dầu ăn dặm 1 chai"),
    (7, "Đi chợ tuần 2", "Trứng gà 6 quả; bí đỏ 100 g"),
    (11, "Đi chợ lần 2 (tuần 2)", "Rau ngót 1 bó nhỏ"),
    (14, "Đi chợ tuần 3", "Gạo tẻ 1 kg; thịt lợn nạc thăn 150 g (chia 7 phần, trữ đông); thịt bò thăn 150 g (chia 7 phần, trữ đông); bí đỏ 100 g; khoai lang 150 g"),
    (21, "Đi chợ tuần 4", "Cá hồi phi lê 100 g (cắt 5 miếng, trữ đông); trứng gà 3 quả; đu đủ chín 150 g; bí đỏ 100 g; rau ngót 1 bó nhỏ"),
    (24, "Đi chợ lần 2 (tuần 4)", "Đu đủ chín 150 g; bí đỏ 100 g; rau ngót 1 bó nhỏ; khoai lang 1 củ nhỏ"),
    (28, "Đi chợ tuần 5", "Thịt bò thăn 100 g (chia 5 phần, trữ đông); bí đỏ 100 g"),
]


def evenings():
    out = []
    # Hai ngày trước khi bắt đầu
    out.append((date_of(1) - dt.timedelta(days=2), "Mochi: còn 2 ngày nữa ăn dặm",
                "Thứ Hai 02/11 Mochi bắt đầu ăn dặm. Chủ nhật 01/11 đi chợ tuần 1."))
    shop_next = {date_of(d) + dt.timedelta(days=0): (t, items) for d, t, items in SHOP}
    for n in range(1, 32):
        m = meals(n)
        parts = []
        if n in NEW_FOOD:
            parts.append(NEW_FOOD[n])
        if n == 1:
            parts.append("Chuẩn bị thìa silicone, ghế ăn, cốc có vạch ml.")
        if m["thaw"]:
            parts.append("Rã đông " + " + ".join(m["thaw"]) + " (để ngăn mát qua đêm).")
        if m["chao"]:
            parts.append("Vo và ngâm gạo cho cháo sáng mai.")
        if n in (10, 15, 22):
            parts.append("Kiểm tra còn trứng.")
        tomorrow = date_of(n)
        if tomorrow in shop_next and tomorrow.weekday() != 6:
            t, items = shop_next[tomorrow]
            parts.append(f"Mai {t.lower()}: {items}.")
        if not parts:
            continue
        evening = date_of(n) - dt.timedelta(days=1)
        title = "Mochi: chuẩn bị cho mai" if not (n in NEW_FOOD) else "Mochi: mai có món mới"
        out.append((evening, title, " ".join(parts)))
    return out


def esc(s):
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line):
    b = line.encode("utf-8")
    if len(b) <= 75:
        return line
    chunks, cur = [], b""
    for ch in line:
        e = ch.encode("utf-8")
        if len(cur) + len(e) > (75 if not chunks else 74):
            chunks.append(cur.decode("utf-8"))
            cur = b""
        cur += e
    chunks.append(cur.decode("utf-8"))
    return "\r\n ".join(chunks)


def utc(d, t):
    return dt.datetime.combine(d, t, TZ).astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def event(uid, d, t, title, desc, minutes=15):
    start = dt.datetime.combine(d, t, TZ)
    end = start + dt.timedelta(minutes=minutes)
    return [
        "BEGIN:VEVENT",
        f"UID:{uid}@mochi-andam",
        "DTSTAMP:20261015T000000Z",
        f"DTSTART:{utc(d, t)}",
        f"DTEND:{end.astimezone(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
        f"SUMMARY:{esc(title)}",
        f"DESCRIPTION:{esc(desc)}",
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        f"DESCRIPTION:{esc(title)}",
        "TRIGGER:PT0M",
        "END:VALARM",
        "END:VEVENT",
    ]


def build():
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Mochi an dam//VI", "CALSCALE:GREGORIAN",
             "METHOD:PUBLISH", "X-WR-CALNAME:Mochi ăn dặm", "X-WR-TIMEZONE:Asia/Ho_Chi_Minh"]
    for i, (d, title, desc) in enumerate(evenings()):
        lines += event(f"toi-{d.isoformat()}-{i}", d, EVENING, title, desc)
    for d0, title, items in SHOP:
        d = date_of(d0) if d0 > 0 else date_of(0)
        if d.weekday() != 6:  # đi chợ giữa tuần: nhắc sáng hôm đó
            pass
        lines += event(f"cho-{d.isoformat()}", d, MORNING, f"Mochi: {title.lower()}",
                       items + ". Thịt cá chia phần, trữ đông ngay khi về.", 30)
    lines.append("END:VCALENDAR")
    return "\r\n".join(fold(l) for l in lines) + "\r\n"


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    (root / "reminders.ics").write_text(build(), encoding="utf-8", newline="")
    for d, t, desc in evenings():
        print(d.strftime("%a %d/%m"), "|", desc)
    for d0, t, items in SHOP:
        print(date_of(d0).strftime("%a %d/%m"), "07:46 |", t)
