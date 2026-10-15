<p align="center"><img src="assets/logo-512.png" width="128" alt="Logo Mochi ăn dặm"></p>

# Mochi ăn dặm

App lịch ăn dặm cho bé Mochi (sinh 02/05/2026), bắt đầu ăn dặm kiểu truyền thống Việt Nam từ thứ Hai 02/11/2026, ngày bé tròn 6 tháng. Một file HTML duy nhất, chạy trên điện thoại, không cần cài đặt.

## Tính năng

- **Hôm nay** — thực đơn từng ngày: công thức, lượng thành phẩm (ml), lượng bé ăn tham khảo; ghi lại từng bữa (ml, bé thích hay từ chối, có phản ứng không, ảnh); nhắc việc cần chuẩn bị tối hôm trước.
- **Lịch** — lộ trình 5 tuần (31 ngày) dạng lịch tháng; **Gợi ý tuần mới** tự lên thực đơn 7 ngày từ các món bé đã ăn ổn, kèm danh sách đi chợ; lịch sử các tuần đã lưu.
- **Đi chợ** — danh sách có ô tick cho từng lần đi chợ (1–2 lần/tuần).
- **Nhật ký** — lịch sử bữa ăn, bảng món đã thử, cân nặng kèm biểu đồ, **báo cáo 1 trang cho bác sĩ** (lưu thành ảnh).
- **Hỏi đáp** — hỏi nhanh về bữa ăn của bé, trả lời dựa trên tuổi, các món đã ăn và nhật ký; cẩm nang nấu nền, nguyên liệu thay thế, dấu hiệu dị ứng, bảo quản, mốc ăn dặm.
- Tuổi bé (tháng, ngày, tuần tuổi) luôn hiện ở đầu app. Hỗ trợ nền sáng và tối.

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

**Qua GitHub Pages.** App chạy đầy đủ lịch, thực đơn, đi chợ, nhật ký, cân nặng, ảnh và báo cáo (lưu ảnh bằng cách nhấn giữ). Bấm nút *Nhật ký chung* ở góc trên → *Tạo nhật ký chung* để dùng chung một nhật ký giữa nhiều máy qua Firebase Firestore, cập nhật trực tiếp; gửi link mời (`?fam=…`) cho người còn lại. Hỏi nhanh chỉ có trong bản Claude. Khi bật GitHub Pages và "Thêm vào Màn hình chính" trên iPhone, app dùng logo Mochi làm icon.

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
tools/make_ics.py       tạo lại reminders.ics
```

## Lưu ý

Thực đơn là hướng dẫn chung cho bé khỏe mạnh, không thay cho tư vấn của bác sĩ nhi. Hỏi bác sĩ về liều sắt bổ sung khi bé bắt đầu ăn thịt bò, lòng đỏ và bột có bổ sung sắt.
