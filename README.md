<p align="center"><img src="assets/logo-512.png" width="128" alt="Logo Mochi ăn dặm"></p>

# Mochi ăn dặm

App lịch ăn dặm cho bé Mochi (sinh 02/05/2026), bắt đầu ăn dặm kiểu truyền thống Việt Nam từ thứ Hai 02/11/2026, ngày bé tròn 6 tháng. Một file HTML duy nhất, chạy trên điện thoại, không cần cài đặt.

## Tính năng

- **Hôm nay** — thực đơn từng ngày: công thức, lượng thành phẩm (ml), lượng bé ăn tham khảo. Ghi nhanh một chạm (*Ăn hết / Một nửa / Từ chối*), nút *⋯* để ghi chi tiết (ml, phản ứng, ảnh); bữa đã ghi tự thu gọn. Nút **Đổi** trên mỗi bữa: chọn món gợi ý nhanh từ những gì Mochi đã ăn được, hoặc tự ghép nền, đạm, rau củ, trái cây; công thức và lượng tự tính lại, nhắc rã đông, ngăn đá và chế độ nấu theo món mới. Thẻ **Mochi hôm nay**: tick sắt, D3K2, DHA, men vi sinh và ghi đi ngoài (kèm gợi ý xử lý). Nhắc việc chuẩn bị tối hôm trước.
- **Chế độ nấu** — nút *Nấu* trên mỗi bữa mở từng bước toàn màn hình, chữ to, hẹn giờ có chuông, giữ màn hình sáng.
- **Lịch** — lộ trình 5 tuần (31 ngày); **Gợi ý tuần mới** đến tháng thứ 12, tự đổi số bữa (2 → 3 bữa từ 9 tháng), lượng đạm, độ thô theo tuổi, kèm danh sách đi chợ; lịch sử các tuần đã lưu.
- **Đi chợ** — chỉ hiện các lần đi chợ sắp tới (lần đã qua gom lại); **ngăn đá** một dòng tóm tắt, chạm để chỉnh; tự cộng khi tick thịt cá, tự trừ khi ghi bữa, cảnh báo thiếu cho 7 ngày tới.
- **Nhật ký** — ba mục: *Bữa ăn*, *Cân nặng* (biểu đồ chuẩn WHO bé gái, P3–P97), *Tổng quan* (báo cáo 1 trang cho bác sĩ, lượng ăn 14 ngày, đi ngoài, bổ sung, các món đã thử).
- **Hỏi đáp** — hỏi nhanh (bản Claude) và cẩm nang.
- **Cài đặt** — nhật ký chung của gia đình (Firebase), nhắc việc Lịch iPhone, **sao lưu/khôi phục** ra file JSON.
- Dùng được khi mất mạng (service worker), có màn hình chào khi mở từ màn hình chính. Tuổi bé luôn hiện ở đầu app; nền sáng và tối.

## Lộ trình 5 tuần

| Tuần | Ngày | Nền | Món mới |
| --- | --- | --- | --- |
| 1 | 02–08/11 | Bột HiPP gạo pha sữa HiPP, 1 bữa | Gạo, bí đỏ, khoai lang |
| 2 | 09–15/11 | Bột đặc dần, 1 bữa | Lòng đỏ trứng, rau ngót |
| 3 | 16–22/11 | Cháo rây, 1 bữa | Thịt lợn, thịt bò |
| 4 | 23–29/11 | Cháo đặc, 2 bữa | Đu đủ, cá hồi |
| 5 | 30/11–02/12 | 2 bữa | Bột Bellamy's táo quế |

Ảnh thực đơn từng tuần và bảng nguyên liệu thay thế nằm trong thư mục [`anh/`](anh).

## Cài lên iPhone

Xem [hướng dẫn cài app](huong-dan.html) (bản ảnh: [`anh/huong-dan-cai-app.png`](anh/huong-dan-cai-app.png)). Nhắc việc dùng app Lịch của iPhone qua file [`reminders.ics`](reminders.ics): 19:49 mỗi tối và 7:46 sáng ngày đi chợ, cho lộ trình 02/11 – 02/12/2026. Tạo lại file bằng `python3 tools/make_ics.py`.

## Cách dùng

**Trong Claude (đầy đủ tính năng).** Bản chính chạy dưới dạng artifact trên claude.ai: nhật ký đồng bộ giữa các máy, có hỏi nhanh, đính kèm ảnh và lưu báo cáo. 

**Qua GitHub Pages.** App chạy đầy đủ lịch, thực đơn, đi chợ, nhật ký, cân nặng, ảnh và báo cáo (lưu ảnh bằng cách nhấn giữ). Bấm nút *Cài đặt* ở góc trên → *Tạo nhật ký chung* để dùng chung một nhật ký giữa nhiều máy qua Firebase Firestore, cập nhật trực tiếp; gửi link mời (`?fam=…`) cho người còn lại. Hỏi nhanh chỉ có trong bản Claude. Khi bật GitHub Pages và "Thêm vào Màn hình chính" trên iPhone, app dùng logo Mochi làm icon.

Bật GitHub Pages: Settings → Pages → Source: *Deploy from a branch* → Branch: `main` / `(root)`.

## Cấu trúc

```
index.html              app (HTML, CSS, JS trong một file)
assets/logo.svg         logo vẽ minh họa
assets/logo-512.png     logo PNG
assets/apple-touch-icon.png  icon 180×180 cho iPhone
anh/                    ảnh thực đơn tuần 1–4, bảng thay thế, hướng dẫn cài app
huong-dan.html          hướng dẫn cài app trên iPhone
reminders.ics           nhắc việc cho app Lịch iPhone
manifest.webmanifest    thông tin app khi thêm vào màn hình chính
sw.js                   service worker: mở app khi mất mạng
tools/make_ics.py       tạo lại reminders.ics
```

## Lưu ý

Thực đơn là hướng dẫn chung cho bé khỏe mạnh, không thay cho tư vấn của bác sĩ nhi. Hỏi bác sĩ về liều sắt bổ sung khi bé bắt đầu ăn thịt bò, lòng đỏ và bột có bổ sung sắt.
