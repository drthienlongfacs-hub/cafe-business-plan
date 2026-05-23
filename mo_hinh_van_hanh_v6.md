# MÔ HÌNH VẬN HÀNH TỐI ƯU — CHỐNG LÃNG PHÍ TOÀN DIỆN

> **Nguyên tắc**: Không thuê rồi ngồi không. Không chi trước khi có khách. Tự động hóa mọi thứ có thể. Mua 1 lần dùng mãi.
> **Scope**: Quán cafe 200m² + sân vườn 30m² + kid zone + mái cong + solar 5kWp

---

## 1. CHI PHÍ ĐIỆN — SOLAR LẮP NGAY TỪ ĐẦU

### Giá điện kinh doanh 2025-2026 (QĐ 1279/QĐ-BCT, cấp <6kV)

| Khung giờ | Thời gian (T2-T7) | Đơn giá (chưa VAT) | + VAT 8% |
|---|---|---|---|
| **Cao điểm** | 17h30-22h30 | 5.422 đ/kWh | **5.856 đ** |
| **Bình thường** | 06h-17h30 + 22h30-24h | 3.152 đ/kWh | **3.404 đ** |
| **Thấp điểm** | 00h-06h | 1.918 đ/kWh | **2.071 đ** |
| CN | 06h-24h = bình thường, 00h-06h = thấp điểm | | |

> **Evidence**: QĐ 1279/QĐ-BCT ngày 09/05/2025, Bộ Công Thương. Khung giờ theo QĐ 963/QĐ-BCT.

### Tải điện THỰC TẾ — phân tích theo cố định vs biến động

#### A. Tải CỐ ĐỊNH (chạy mọi ngày bất kể khách)

| Thiết bị | Công suất | Giờ/ngày | kWh/ngày | kWh/tháng | Ghi chú |
|---|---|---|---|---|---|
| Tủ mát 2 cánh Sanaky | 0,15kW (thực tế) | 24h | 3,6 | 108 | Inverter, chạy 24/7 |
| Tủ bánh trưng bày | 0,12kW | 14h (06h-20h) | 1,7 | 51 | Tắt ban đêm |
| Camera Hikvision × 4 | 0,04kW | 24h | 1,0 | 30 | 10W/cam × 4 |
| Đèn LED chiếu sáng | 0,3kW | 6h (17h-23h) | 1,8 | 54 | Buổi tối, cần thiết |
| String light sân vườn | 0,1kW | 5h (18h-23h) | 0,5 | 15 | Tạo không gian |
| Router WiFi + POS tablet | 0,03kW | 24h | 0,7 | 21 | |
| Máy lọc RO | 0,05kW | 4h | 0,2 | 6 | Chạy gián đoạn |
| **Tổng cố định** | | | **~9,5 kWh/ngày** | **~285 kWh/tháng** | |

#### B. Tải BIẾN ĐỘNG (theo lượng khách + thời tiết)

| Thiết bị | Công suất | Giờ ít khách | Giờ trung bình | Giờ cao điểm | Ghi chú |
|---|---|---|---|---|---|
| **Điều hòa Casper 24K × 2** | 2 × 1,8kW = 3,6kW | 6h (11h-17h) | 10h (10h-20h) | 14h (8h-22h) | Biên Hòa nắng nóng 35-40°C, PHẢI bật |
| Quạt trần × 3 | 0,2kW | 6h | 10h | 14h | Hỗ trợ AC |
| Máy pha CRM 3120 | 1,5kW (thực tế ~0,8kW trung bình) | 3h | 5h | 8h | Không chạy liên tục, gia nhiệt gián đoạn |
| Máy xay sinh tố × 2 | 1kW × 2 | 0,5h | 1h | 2h | Chạy từng lúc |
| Ấm đun gooseneck | 0,8kW | 1h | 2h | 3h | |

| Kịch bản | AC kWh | Quạt | Máy pha | Xay + Ấm | **Tổng biến động/ngày** |
|---|---|---|---|---|---|
| **Ít khách** (5-10 khách) | 21,6 | 1,2 | 2,4 | 1,3 | **~26,5 kWh** |
| **Trung bình** (15-20 khách) | 36,0 | 2,0 | 4,0 | 2,5 | **~44,5 kWh** |
| **Cao điểm** (25-35 khách) | 50,4 | 2,8 | 6,4 | 4,4 | **~64,0 kWh** |

#### C. TỔNG TIÊU THỤ ĐIỆN — 3 KỊCH BẢN

| Kịch bản | Cố định | Biến động | **Tổng/ngày** | **Tổng/tháng** | Tiền điện/tháng (trung bình 3.404đ/kWh) |
|---|---|---|---|---|---|
| **Ít khách** | 9,5 | 26,5 | **36 kWh** | **~1.080 kWh** | **~3,7 tr** |
| **Trung bình** | 9,5 | 44,5 | **54 kWh** | **~1.620 kWh** | **~5,5 tr** |
| **Cao điểm** | 9,5 | 64,0 | **73,5 kWh** | **~2.205 kWh** | **~7,5 tr** |

> **Lưu ý**: Giá trung bình 3.404đ/kWh vì quán chủ yếu hoạt động giờ bình thường (06h-17h30). Buổi tối 17h30-22h30 là giờ cao điểm 5.856đ → đắt hơn 72%. Solar chỉ phát ban ngày → offset phần giá rẻ nhất, nhưng tiết kiệm tuyệt đối vẫn lớn.

### Solar: Sizing tối ưu — TỰ DÙNG HẾT, KHÔNG BÁN LẠI

#### Sản lượng solar tại Biên Hòa (PVGIS data)

| Mùa | kWh/kWp/ngày | Nguồn |
|---|---|---|
| Xuân (T2-T4) | **6,26** | profilesolar.com / PVGIS |
| Hè (T5-T7) | **5,58** | Mùa mưa, mây nhiều |
| Thu (T8-T10) | **4,92** | Mùa mưa chính |
| Đông (T11-T1) | **5,61** | Nắng trở lại |
| **Trung bình năm** | **5,09** | Bức xạ: 1.849 kWh/m²/năm |

> **Evidence**: dongnai.gov.vn, vuphong.vn, profilesolar.com — bức xạ ngang trung bình năm Đồng Nai: 1.849 kWh/m².

#### Tính toán công suất tối ưu

**Mục tiêu**: Solar phát ban ngày = tải ban ngày. Không phát dư (không bán lại), không thiếu (không mua thêm ban ngày).

| Tải ban ngày (06h-17h30 = ~11,5h) | Ít khách | Trung bình | Cao điểm |
|---|---|---|---|
| AC (ban ngày chạy) | 14,4 | 25,2 | 36,0 |
| Tủ mát + tủ bánh + camera + RO | 4,5 | 4,5 | 4,5 |
| Máy pha + xay + ấm | 2,4 | 4,0 | 6,4 |
| Quạt trần | 0,8 | 1,3 | 1,8 |
| **Tổng tải ban ngày** | **~22 kWh** | **~35 kWh** | **~49 kWh** |

| Công suất solar | Sản lượng/ngày (× 5,09) | Khớp kịch bản | Dư/thiếu |
|---|---|---|---|
| 3 kWp | 15,3 kWh | < ít khách (22) | ❌ Thiếu |
| **5 kWp** | **25,5 kWh** | ≈ ít khách (22) | ✅ Vừa đủ khi ít khách, thiếu khi đông |
| **7 kWp** | **35,6 kWh** | ≈ trung bình (35) | ✅✅ **TỐI ƯU** — khớp trung bình, ít dư |
| 10 kWp | 50,9 kWh | > cao điểm (49) | ⚠️ Dư buổi trưa ít khách |

> **Kết luận: Lắp 7 kWp** — khớp tải trung bình 35 kWh/ngày. Ngày ít khách dư ~10 kWh (tủ lạnh + camera dùng hết). Ngày cao điểm thiếu ~14 kWh (mua thêm điện lưới buổi tối).

#### Chi phí solar 7 kWp — lắp ngay từ đầu

| Hạng mục | Chi phí | Ghi chú |
|---|---|---|
| Hệ thống 7 kWp on-grid trọn gói | **70-85 triệu** | QĐ 58/2025/NĐ-CP: tự sản tự tiêu <100kW, thông báo cơ quan |
| Tấm pin (14 tấm × 500Wp) | ~40-45 tr | JA Solar/Longi/Canadian Solar |
| Inverter (Sungrow/Growatt) | ~12-15 tr | |
| Khung, dây, CB, MC4, công lắp | ~18-25 tr | |

> **Evidence**: Giá 2026 Q2: 50-75tr cho 5kWp, 70-100tr cho 7kWp (tăng 5-10% vs 2025 do nhu cầu cao mùa nóng). Nguồn: nhiều đơn vị Biên Hòa/Đồng Nai.

#### Phân tích hoàn vốn chi tiết

| Hạng mục | Giá trị | Cách tính |
|---|---|---|
| Sản lượng solar/tháng | **~1.070 kWh** | 7kWp × 5,09 × 30 |
| Tỷ lệ tự tiêu (ban ngày) | **90-95%** | Không bán lại, dùng hết cho AC + tủ + máy pha |
| kWh tự tiêu thực tế/tháng | **~960-1.020 kWh** | |
| Tiền tiết kiệm/tháng (giờ bình thường) | **~3.270-3.470k** | 960-1.020 × 3.404đ |
| **Hoàn vốn** (với 75tr đầu tư) | **~22-23 tháng** | 75.000k ÷ 3.370k |
| **Từ tháng 24**: tiền điện ban ngày | **≈ 0 đồng** | |

#### Tiền điện sau khi lắp solar — 3 kịch bản

| Kịch bản | Không solar | Có solar 7kWp | **Tiết kiệm** |
|---|---|---|---|
| Ít khách | 3,7 tr | **~700k** (chỉ trả điện tối) | **-3,0 tr** |
| Trung bình | 5,5 tr | **~2,0 tr** | **-3,5 tr** |
| Cao điểm | 7,5 tr | **~4,0 tr** | **-3,5 tr** |

> **Kết luận**: Lắp solar **7 kWp NGAY TỪ ĐẦU** (70-85tr). Hoàn vốn ~22 tháng. Sau đó điện ban ngày = 0 đồng. Tiết kiệm 3,0-3,5tr/tháng mãi mãi. Tuổi thọ panel: 25-30 năm.

#### Kế hoạch mở rộng solar — MỤC TIÊU: TIỀN ĐIỆN < 500k/tháng

> **Nguyên tắc**: Nếu tiền điện lưới > 500k/tháng liên tục 3 tháng → lắp bổ sung.

| Trigger | Nguyên nhân | Giải pháp | Chi phí bổ sung | Kết quả |
|---|---|---|---|---|
| Điện lưới > 500k × 3 tháng | Lượng khách tăng → AC chạy nhiều hơn (kịch bản cao điểm) | Lắp thêm **2-3 kWp** (4-6 tấm) | **20-30 tr** | 9-10 kWp → cover cao điểm |
| Điện lưới > 1tr × 3 tháng | Mở rộng thiết bị (thêm AC, tủ mát) | Lắp thêm **3-5 kWp** | **30-50 tr** | 10-12 kWp → gần tự chủ hoàn toàn |
| Mùa mưa solar giảm 20-30% | Thu (T8-T10): 4,92 kWh/kWp thay vì 5,09 | Không lắp thêm — chấp nhận mua lưới 2-3 tháng mùa mưa | 0 | Tiền lưới mùa mưa ~500-800k OK |

> **Lộ trình**:
> - **Tháng 1-6**: Theo dõi hóa đơn EVN hàng tháng. Ghi nhận kWh mua lưới vs solar sản xuất.
> - **Tháng 7**: Nếu trung bình > 500k → báo giá lắp thêm 2-3 kWp.
> - **Mục tiêu cuối**: Tiền điện lưới **< 500k/tháng** (chỉ trả phần tối + mùa mưa). Inverter Sungrow/Growatt hỗ trợ mở rộng dễ dàng, không cần thay inverter mới.

---

## 2. NHÂN SỰ — THÔNG MINH, KHÔNG LÃNG PHÍ

### Mô hình: Chủ quán + 1 PV full-time + Part-time theo nhu cầu

| Vai trò | Ai | Lương | Giờ | Ghi chú |
|---|---|---|---|---|
| **Chủ quán** (pha chế + quản lý) | Bạn | 0 | 7h-14h (sáng) | Pha chế chính, kiểm soát tài chính |
| **PV full-time** (pha chế + thu ngân + dọn) | 1 người | **6-7 tr** | 14h-22h (chiều-tối) | Đa nhiệm: pha chế + thu ngân + dọn |
| **PV part-time** (phụ trẻ + dọn) | 1-2 sinh viên | **25-30k/giờ** | Chỉ T7-CN + giờ cao điểm 16h-20h | Gọi khi cần, không fix |
| **Người nước ngoài** (trải nghiệm) | Volunteer/intern | **0-3 tr** | Theo lịch booking | Chỉ có khi có khách đăng ký |

### Chi phí nhân sự theo kịch bản

| Kịch bản | Full-time | Part-time | NN | **Tổng/tháng** |
|---|---|---|---|---|
| Tháng ít khách (đầu) | 6,5 tr | 4 ngày × 4h × 25k = 400k | 0 | **~7 tr** |
| Tháng trung bình | 6,5 tr | 8 ngày × 5h × 25k = 1tr | 2 tr | **~9,5 tr** |
| Tháng cao điểm | 6,5 tr | 12 ngày × 6h × 30k = 2,2tr | 3 tr | **~11,7 tr** |

> **Evidence**: Kinh nghiệm thị trường 2025: quán nhỏ/vừa tối ưu = 2 người/ca (1 pha chế, 1 phụ). Chủ quán trực tiếp quản lý/làm = tiết kiệm 8-10tr lương quản lý. Part-time sinh viên = linh hoạt, chỉ gọi khi cần.

### Bài học thất bại cần tránh
- ❌ Thuê 4-5 nhân viên full-time từ đầu khi chưa rõ lượng khách → lãng phí 20-30tr/tháng
- ❌ Không đào tạo đa nhiệm → mỗi người chỉ làm 1 việc
- ❌ Giao phó hoàn toàn cho quản lý → thất thoát không kiểm soát
- ✅ Chủ quán trực tiếp pha chế ca sáng + kiểm soát POS + kho
- ✅ Part-time theo giờ cao điểm (T7-CN 16h-20h)
- ✅ Menu tập trung 4-6 món "đinh" dễ pha = 1 người làm được
---

## 2B. CHƯƠNG TRÌNH "ENGLISH HOST" — NGƯỜI VIỆT NÓI TIẾNG ANH TỐT

> **Mục tiêu**: Tạo nguồn nhân lực nói tiếng Anh tự nhiên, bổ sung/thay thế khi không đủ volunteer nước ngoài. Chi phí gần 0 — chỉ tặng đồ uống/voucher.

### Đối tượng & Điều kiện

| Tiêu chí | Yêu cầu | Lý do |
|---|---|---|
| **IELTS Speaking** | ≥ 7.5 | Giao tiếp tự nhiên như bản xứ, không đọc bài |
| **TOEFL iBT** | ≥ 26 (Speaking) | Tương đương |
| **TOEIC** | ≥ 900 + phỏng vấn nói trực tiếp | TOEIC thiên listening/reading, cần verify nói |
| **Đăng ký** | Qua Google Forms (kèm ảnh chứng chỉ) | Xác minh trước khi chấp nhận |
| **Hoạt động bắt buộc** | Tổ chức ≥1 hoạt động tiếng Anh cho bé (30-45 phút) | Đổi lấy quà tặng |

### Quà tặng & Chi phí

| Quà tặng | Giá trị thực | Chi phí nguyên liệu | Ghi chú |
|---|---|---|---|
| Ly nước thứ 2 **miễn phí** | ~40-60k | ~8-12k (NVL) | Tặng ngay khi đến |
| 1 phần bánh | ~30-40k | ~10-15k (NVL) | Tặng ngay |
| Bốc thăm voucher **100k** sử dụng tại quán | 100k | ~25-35k (NVL khi dùng) | Xác suất trúng ~30-50% |
| **Chi phí/lượt English Host** | | **~30-50k NVL thực** | |

### Phân tích tài chính

| Kịch bản | Số lượt/tháng | Chi phí NVL | Doanh thu tăng thêm | Lý do |
|---|---|---|---|---|
| Ít (tháng đầu) | 2 lượt | 60-100k | ~200-400k | Các bé đóng phí workshop |
| Trung bình | 4 lượt | 120-200k | ~500k-1tr | Phụ huynh order thêm + quay lại |
| Cao điểm | 8 lượt | 240-400k | ~1-2tr | Event cuối tuần, sinh nhật |

> **ROI**: Chi 120-400k NVL → thu 500k-2tr doanh thu tăng thêm. **Lãi ròng 300-1.600k/tháng** chỉ riêng phần này.

### Hoạt động khi CÓ khách audience (trẻ em/khách giao tiếp)

| Hoạt động | Thời lượng | Mô tả | Độ tuổi |
|---|---|---|---|
| **Story Time** | 30 phút | Đọc + diễn sách tranh bằng tiếng Anh, bé trả lời câu hỏi | 3-7 tuổi |
| **Game Master** | 45 phút | Quản trò boardgame/LEGO challenge bằng tiếng Anh | 5-12 tuổi |
| **Mini Talk** | 30 phút | Thuyết trình chủ đề đơn giản + Q&A (travel, animals, food) | 8-15 tuổi |
| **Show & Tell** | 30 phút | Bé mang đồ yêu thích, giới thiệu bằng tiếng Anh, Host hỗ trợ | 5-10 tuổi |

### Hoạt động khi KHÔNG CÓ khách audience (Host vẫn nhận quà)

> **Tình huống**: Host đến quán nhưng hôm đó không có trẻ em/khách muốn giao tiếp. Vẫn tạo giá trị marketing cho quán → vẫn nhận quà.

| Hoạt động thay thế | Yêu cầu cụ thể | Giá trị cho quán |
|---|---|---|
| **Video review tiếng Anh** | Quay 60-90s review quán bằng tiếng Anh, nêu cảm nghĩ thật | Content marketing chất lượng cao |
| **Đăng FB cá nhân** | Đăng public, tag quán + tag ≥3 người bạn, giữ public ≥7 ngày | Reach organic miễn phí |
| **Review Google Maps** | Viết review ≥50 từ + ảnh thực tế + rating ≥4 sao | SEO local, tăng uy tín |
| **Video TikTok/Reels** | Quay video ngắn 15-30s trải nghiệm tại quán, tag quán | Viral potential |
| **Phỏng vấn ngắn** | Chủ quán phỏng vấn Host về trải nghiệm (2-3 phút), đồng ý đăng trên page quán | Content cho kênh YouTube/TikTok quán |
| **Mini presentation tự do** | Thuyết trình 5-10 phút trước camera về bất kỳ chủ đề nào bằng tiếng Anh | Content giáo dục cho kênh quán |

> **Điều kiện nhận quà khi không có audience**: Hoàn thành ≥2 trong 6 hoạt động trên. Content phải giữ public ≥7 ngày, không xóa. Quán giữ quyền sử dụng content cho marketing.
> **Giá trị thực**: 1 video review tiếng Anh chất lượng trên TikTok = tương đương 200-500k quảng cáo. 1 review Google Maps = vĩnh viễn.

### Pháp lý — KHÔNG phải quan hệ lao động

| Yếu tố | Phân tích | Kết luận |
|---|---|---|
| **Quan hệ** | Khách hàng tham gia chương trình khuyến mại | ✅ KHÔNG phải lao động |
| **Lương** | Không trả lương — tặng đồ uống/voucher | ✅ Quà tặng khuyến mại |
| **Thời gian** | Tự do đăng ký, không cam kết giờ | ✅ Không ràng buộc |
| **Căn cứ** | Luật Thương mại 2005, NĐ 81/2018/NĐ-CP | Tổng quà <100tr/năm → không cần thông báo Sở CT |
| **Hồ sơ cần** | Thể lệ chương trình nội bộ + danh sách khách tham gia | Lưu Google Sheets |

### So sánh: English Host VN vs Volunteer Nước ngoài

| | English Host VN (IELTS ≥7.5) | Volunteer Nước ngoài |
|---|---|---|
| **Chi phí** | ~30-50k NVL/lượt | 0-3tr/tháng + ăn ở |
| **Nguồn** | Sinh viên, giáo viên Anh ngữ, freelancer | Backpacker, intern, cultural guest |
| **Pháp lý** | ✅ Đơn giản (khuyến mại) | ⚠️ Phức tạp (Work Permit, tạm trú) |
| **Ổn định** | ✅ Dễ tìm (Biên Hòa/HCM) | ❌ Không ổn định, mùa vụ |
| **Phát âm** | Tốt nhưng có accent VN | Bản xứ (nếu Anh/Mỹ/Úc) |
| **Kết hợp** | ✅ **Kết hợp cả 2 = tối ưu** | ✅ |

### Kênh tuyển English Host

| Kênh | Cách tiếp cận | Chi phí |
|---|---|---|
| FB Groups "IELTS Vietnam", "IELTS Speaking Practice" | Post tuyển volunteer, nêu rõ quà tặng | 0 |
| Zalo nhóm "English Teachers Biên Hòa" | Liên hệ trực tiếp | 0 |
| Đại học Lạc Hồng / ĐH Đồng Nai | Liên hệ CLB tiếng Anh, đề xuất hợp tác | 0 |
| TikTok/Instagram của quán | Content "Tìm English Host — nói tiếng Anh nhận quà" | 0 |

> **Kết luận**: ✅ **RẤT PHÙ HỢP**. Chi phí gần 0. Pháp lý đơn giản. Nguồn dồi dào. Bổ sung hoàn hảo cho volunteer nước ngoài. Triển khai ngay từ tuần mở cửa.

---

## 3. BOOKING ONLINE + ĐỒNG THUẬN PHÁP LÝ

### Giải pháp: Google Forms + Google Calendar (MIỄN PHÍ)

| Bước | Chi tiết | Chi phí |
|---|---|---|
| 1. Tạo form đăng ký | Google Forms: tên, SĐT/Gmail, ngày, số bé, tuổi bé | 0 |
| 2. Checkbox đồng thuận | "Tôi đồng ý với [Nội quy an toàn] và [Chính sách quyền riêng tư]" — bắt buộc tích | 0 |
| 3. Xác nhận tự động | Google Forms → tự gửi email xác nhận | 0 |
| 4. Lịch tự động | Zapier free / Google Apps Script → đẩy vào Calendar | 0 |
| 5. Nhắc nhở | Google Calendar nhắc trước 1 ngày | 0 |

### Giá trị pháp lý của checkbox online

> **Căn cứ**: Luật Giao dịch điện tử 2023 (Luật 20/2023/QH15), Điều 8-9: Giao dịch điện tử có giá trị pháp lý tương đương văn bản giấy nếu có đủ thông tin xác định người ký (email/SĐT), nội dung đồng thuận rõ ràng, và lưu trữ được.
> 
> **Yêu cầu tối thiểu**: 
> - ✅ Có thông tin định danh (Gmail hoặc SĐT)
> - ✅ Nội dung đồng thuận hiển thị rõ ràng trước khi tích
> - ✅ Bắt buộc tích mới submit được
> - ✅ Dữ liệu lưu trên Google Sheets (chứng minh được)

---

## 4. HỌC CỤ MONTESSORI — NGUỒN RẺ NHẤT

| Nguồn | Loại | Giá | Từ khóa/Link |
|---|---|---|---|
| **1688 sỉ** | Giáo cụ gỗ Montessori mới | **5-30 CNY/bộ** (18-108k) | "Montessori 教具", "蒙氏教具 批发" |
| **FB Groups thanh lý** | Giáo cụ cũ theo lô | **200-500k/lô 10-20 món** | "Thanh lý giáo cụ Montessori", "đồ chơi gỗ cũ" |
| **Shopee thanh lý** | Đồ chơi gỗ theo combo | **150-300k/combo** | "Montessori thanh lý", "đồ chơi gỗ giáo dục" |
| **LEGO theo ký** | LEGO cũ đổ đống | **150-200k/kg** | FB "LEGO theo ký Sài Gòn" |
| **Boardgame 2nd** | Boardgame cũ còn tốt | **30-100k/bộ** | Chợ Tốt "boardgame cũ" |
| **Tự làm DIY** | Bảng cảm giác, hộp xếp hình | **50-100k/bộ** | Gỗ vụn + sơn an toàn |

### Budget học cụ tối ưu

| Hạng mục | SL | Đơn giá | Tổng |
|---|---|---|---|
| Giáo cụ gỗ 1688 (1 lô 20 bộ) | 20 | 50k | 1 tr |
| LEGO theo ký | 5 kg | 180k | 900k |
| Boardgame 2nd | 10 bộ | 50k | 500k |
| Sách thiếu nhi 2nd | 20 cuốn | 15k | 300k |
| DIY bảng cảm giác | 3 bộ | 100k | 300k |
| **TỔNG HỌC CỤ** | | | **3 tr** |

---

## 5. TỰ ĐỘNG HÓA — ĐIỀU KHIỂN QUA ĐIỆN THOẠI

### Hệ thống Tuya/Sonoff (rẻ nhất thị trường)

| Thiết bị | Chức năng | Giá (1688) | SL | Tổng |
|---|---|---|---|---|
| Ổ cắm thông minh Tuya WiFi | Bật/tắt đèn sân, máy bơm tưới | 35k/cái | 5 | 175k |
| Van điện từ 12V + timer Tuya | Tưới cây tự động theo lịch | 120k/bộ | 2 | 240k |
| Cảm biến độ ẩm đất Zigbee | Tưới khi đất khô tự động | 80k/cái | 2 | 160k |
| Gateway Zigbee (Tuya) | Hub trung tâm | 200k | 1 | 200k |
| Ống PE 16mm + béc nhỏ giọt | Hệ thống tưới vật lý | — | — | 300k |
| **TỔNG TỰ ĐỘNG HÓA** | | | | **~1,1 tr** |

> **Cách dùng**: Tải app Smart Life (miễn phí) → kết nối WiFi → hẹn giờ tưới 6h sáng + 17h chiều → cảm biến tự skip nếu đất ướt.
> **Tiết kiệm**: Không cần người tưới mỗi ngày = tiết kiệm 30 phút/ngày × 30 = 15 giờ/tháng

---

## 6. DUY TRÌ + VỆ SINH + MUỖI

### Chi phí duy trì hàng tháng

| Hạng mục | Chi phí/tháng | Cách tối ưu |
|---|---|---|
| **Diệt muỗi** | **100-200k** | Bã cà phê đốt (miễn phí), cây sả + hương thảo (đã trồng), đèn bắt muỗi 1688 (150k/cái, 1 lần) |
| Vệ sinh chung | 0 | PV full-time dọn cuối ngày + chủ quán sáng |
| Vệ sinh kid zone | 0 | PV/chủ quán lau thảm + đồ chơi bằng dung dịch sát khuẩn |
| Cắt tỉa cây | 0 | Tự làm 2 lần/tháng |
| Bảo trì mái | 100k | Kiểm tra ngói/tôn mùa mưa, seal khe hở |
| Bảo trì điện nước | 100k | Kiểm tra CB, van, bơm hàng tháng |
| Bảo trì ML | 200k | Vệ sinh filter 2 tuần/lần (tự làm) |
| Tinh dầu sả/oải hương | 100k | Máy xông 1688 (200k, 1 lần) + refill tinh dầu |
| Hóa chất vệ sinh | 200k | Nước lau sàn, sát khuẩn, giấy vệ sinh |
| Phun muỗi chuyên nghiệp | 250k/tháng (1 lần/3 tháng = 750k) | Chỉ mùa mưa |
| **TỔNG DUY TRÌ** | **~1-1,5 tr/tháng** | |

### Chiến lược muỗi "miễn phí"
1. **Trồng sẵn**: Sả chanh, hương thảo, húng quế quanh bàn khách (đã tính trong sân vườn)
2. **Bã cà phê**: Phơi khô bã từ quán → đốt buổi chiều tối = 0 đồng
3. **Không nước đọng**: Thiết kế thoát nước tốt từ đầu, không chậu đọng nước
4. **Đèn bắt muỗi**: 1688, 150k/cái × 3 = 450k (1 lần)

---

## 7. TỔNG CHI PHÍ VẬN HÀNH — 3 KỊCH BẢN

### Kịch bản A: Tháng đầu (ít khách)

| Hạng mục | Chi phí |
|---|---|
| Nhân sự (chủ + 1 FT + ít PT) | 7 tr |
| Điện (CÓ solar 7kWp từ đầu) | **700k** |
| Nước | 1 tr |
| Nguyên vật liệu F&B | 5 tr |
| Duy trì + vệ sinh + muỗi | 1,2 tr |
| Internet + SĐT | 500k |
| Gas (bếp nhỏ) | 300k |
| Thuê đất (trả ba mẹ) | 3 tr |
| Dự phòng | 1 tr |
| **TỔNG A** | **~19,7 tr/tháng** |

### Kịch bản B: Tháng trung bình (có khách)

| Hạng mục | Chi phí |
|---|---|
| Nhân sự (+ PT + NN/English Host) | 9,5 tr |
| Điện (CÓ solar 7kWp) | **2 tr** |
| Nước | 1,2 tr |
| Nguyên vật liệu F&B | 10 tr |
| Duy trì + vệ sinh | 1,5 tr |
| Internet + SĐT | 500k |
| Gas | 400k |
| Thuê đất | 3 tr |
| Marketing boost | 500k |
| Dự phòng | 1 tr |
| **TỔNG B** | **~29,6 tr/tháng** |

### Kịch bản C: Tháng cao điểm

| Hạng mục | Chi phí |
|---|---|
| Nhân sự (đủ PT + NN/English Host) | 11,7 tr |
| Điện (CÓ solar 7kWp) | **4 tr** |
| Nước | 1,5 tr |
| Nguyên vật liệu F&B | 18 tr |
| Duy trì + vệ sinh | 1,5 tr |
| Internet + SĐT | 500k |
| Gas | 500k |
| Thuê đất | 3 tr |
| Marketing boost | 1 tr |
| Dự phòng | 1,5 tr |
| **TỔNG C** | **~43,2 tr/tháng** |

### So sánh với bản cũ trên live site

| | Live site cũ | **v6 tối ưu** | Tiết kiệm |
|---|---|---|---|
| Chi phí vận hành/tháng | 125-155 tr | **20-43 tr** | **-82 đến -135 tr** |
| Nhân sự | 5-8 người fix | **2 fix + PT + English Host** | Linh hoạt |
| Điện | Chưa tối ưu | **Solar 7kWp từ đầu, offset 60-80%** | -3,0 đến -3,5 tr/tháng |

> **Lý do site cũ quá cao**: Site cũ tính theo scope v7 full (200m² trần 5m, 5-8 nhân viên, 525m² sân, điều hòa trung tâm). v6 scope nhỏ hơn + tự vận hành + part-time linh hoạt.

---

## 8. MARKETING: YOUTUBE + TIKTOK (0-500k/tháng)

### Chiến lược content

| Nền tảng | Content | Tần suất | Chi phí |
|---|---|---|---|
| TikTok | Video ngắn bé chơi học cụ, pha cafe, sân vườn | 3-5 video/tuần | 0 (tự quay bằng điện thoại) |
| YouTube | Vlog dài: "1 ngày ở quán cafe học cụ cho bé", review học cụ | 1-2 video/tuần | 0 |
| Facebook/Zalo | Post ảnh, event, booking link | Hàng ngày | 0 |
| Google Maps | Review + ảnh | Khuyến khích khách review | 0 |
| Boost ads (khi cần) | TikTok/FB ads khu vực Biên Hòa | Khi cần | 300-500k/tháng |

### USP (Unique Selling Point)
> **"Quán cafe kèm không gian học mà chơi, chơi mà học cho bé — phù hợp mọi lứa tuổi"**
> - Học cụ Montessori + LEGO + Boardgame + Sách
> - Trải nghiệm văn hóa quốc tế (khi có volunteer)
> - Sân vườn mái cong, visual Instagram
> - Booking online, an toàn, có đồng thuận pháp lý
