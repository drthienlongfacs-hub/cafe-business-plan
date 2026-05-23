# AUDIT V7 - DU TOAN MAI CONG & NOI THAT

Ngay audit: 2026-05-23  
Pham vi audit: noi dung paste "DỰ TOÁN CHI PHÍ BÓC TÁCH - AUDIT MÁI CONG & NỘI THẤT V7", doi chieu voi:

- `/Users/mac/.gemini/antigravity/brain/f1c1aeef-6911-497f-9300-8dcc0ef1bd66/walkthrough.md`
- `/Users/mac/.gemini/antigravity/brain/f1c1aeef-6911-497f-9300-8dcc0ef1bd66/implementation_plan.md`
- `/Users/mac/Projects/kid-cafe-blueprint/cost_price_audit_2026-05-23.md`
- Nguon gia/thi cong hien hanh 2025-2026 tren web.

## 1. Verdict

**V7 chua dat chuan "BOQ day du".** Ban nay co tien bo vi da thua nhan moc 366 trieu la sai scope, nhung no lai tron 3 lop du toan khac nhau trong cung mot tai lieu:

1. Lop cu: thiet bi pha che 54,5 tr, noi that 48 tr, sua sang 200 tr.
2. Lop v5/v5.2: mua gia thanh ly, GĐ1 430-451 tr.
3. Lop V7/walkthrough hien hanh: mai cong phu nha 10x20m, tran 5m, keo go lo, cua kinh xep truot 3,5m, vach kinh 10ly, Montessori house, san vuon 15x35m.

Ket luan dau file **950 tr - 1,28 ty** co the la huong an toan hon so voi 451 tr, nhung trong file hien tai **chua co BOQ chung minh con so 950 tr - 1,28 ty**. Nguoc lai, bang "v5.2 BOQ day du" van tinh theo scope nho hon va bo sot nhieu hang muc cua V7.

**Trang thai audit:** `FAIL - NOT DECISION READY`

## 2. Loi so hoc va mau thuan noi bo

### 2.1. Bang chi tiet v5.2 khong cong ra 451 tr

Cong cac dong trong bang "GIAI DOAN 1: XAY DUNG + SETUP":

| Nhom | Gia tri |
|---|---:|
| Tong cac dong A den G, tru du phong | 408,7 tr |
| Du phong H theo file | 21,5 tr |
| **Tong theo dong chi tiet** | **430,2 tr** |

Trong khi file ghi **~451 tr**. Con so 451 tr chi khop voi bang tong hop trong `walkthrough.md` neu cong them cac nhom khac nhu `Giay phep 8 tr` va/hoac PCCC theo cach tach rieng. Nhưng o bang chi tiet, dong F3 lai ghi **"Camera + do choi + PCCC + GP = 32 tr"**. Nhu vay V7 dang bi **khong nhat quan category**: hoac F3 da gom PCCC+giay phep, hoac PCCC+giay phep phai tach rieng. Khong duoc vua gom vua cong rieng.

### 2.2. Tong GĐ2 cung bi lech theo cach cong

Neu lay bang chi tiet V5.2:

| Scope | Tong |
|---|---:|
| GĐ1 theo dong chi tiet | ~430 tr |
| GĐ2 solar + cua vom | 85-95 tr |
| **Tong 2 giai doan** | **515-525 tr** |

File lai ghi **536-546 tr**, khop hon voi moc GĐ1 451 tr. Can chon mot cach tinh duy nhat.

### 2.3. Ket luan dau file mau thuan voi bang chinh

File noi scope hien hanh can **950 tr - 1,28 ty**, nhung bang chinh lai ket luan GĐ1 **451 tr**, GĐ2 **85-95 tr**, tong **536-546 tr**. Hai ket luan nay khong cung scope. Neu giu ca hai, phai ghi ro:

- `451 tr`: chi la **minimum salvage/DIY scope**, chua cover V7 full walkthrough.
- `950 tr - 1,28 ty`: la **full current scope**, can BOQ moi.

## 3. Evidence ledger

| Ma | Nguon | Dung de audit |
|---|---|---|
| E01 | Audit truoc: `/Users/mac/Projects/kid-cafe-blueprint/cost_price_audit_2026-05-23.md` | Gia dien, solar, mai ngoi, Appia II, ton lanh, PCCC, loi tong 399->415,5 tr. |
| E02 | `walkthrough.md` local | v5.2 goc ghi phat sinh 45,6 tr va tong GĐ1 451 tr. |
| E03 | Bo Cong Thuong QD 1279/QD-BCT 2025: https://vbpl.ts24.com.vn/support/solutions/articles/16000212528-quy%E1%BA%BFt-%C4%91%E1%BB%8Bnh-1279-q%C4%91-bct-ng%C3%A0y-09-05-2025-quy-%C4%91%E1%BB%8Bnh-v%E1%BB%81-gi%C3%A1-b%C3%A1n-%C4%91i%E1%BB%87n | Gia dien kinh doanh duoi 6kV: gio binh thuong 3.152 d/kWh chua VAT, 3.467 d/kWh sau VAT. |
| E04 | JRC PVGIS API docs: https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system-pvgis/using-pvgis-5/api-non-interactive-service_en | San luong solar 5 kWp tai Bien Hoa da tinh: ~7.095 kWh/nam. |
| E05 | Gia lap solar 2026: https://solarbrano.vn/chi-phi-lap-dien-mat-troi-tron-goi/ va https://dienmattroi24h.com.vn/gia-lap-dien-mat-troi-2026-la-bao-nhieu/ | He 5 kW hoa luoi thuong 50-85 tr/50-65 tr tuy cau hinh. |
| E06 | Kinh cuong luc/vach kinh 10mm: https://kinhdaiduong.com/bao-gia-vach-ngan-kinh/ va https://cuavip.com.vn/bao-gia-cua-kinh-cuong-luc-2 | Vach/kich 10mm thuong 750k/m2 rieng kinh; vách hoàn thiện còn phụ kiện, khoan khoét, ray, công. |
| E07 | Cua nhom Xingfa 2026: https://cuanhomkinhhn.com/cua-nhom-xingfa/ va https://asnwindoor.com/cua-nhom-xingfa-kinh-cuong-luc/ | Cua nhom Xingfa moi co the 1,4-3,8 tr/m2; cua di Xingfa 10mm co moc 2,4-2,8 tr/m2. |
| E08 | Dieu hoa 24.000 BTU: https://www.panasonic.com/vn/air-solutions/learn-more/cong-suat-dieu-hoa.html va https://homecare24h.com/kien-thuc-chung/dieu-hoa-24000btu-dung-cho-phong-bao-nhieu-m2 | 24.000 BTU thuong phu hop khoang 30-40m2/80-120m3; tran 5m va 200m2 khong the dung 2 may 24K lam baseline. |
| E09 | Kids cafe/playground cost: https://h3group.com.vn/tu-van-quan-cafe/chi-phi-mo-quan-cafe-co-khu-vui-choi-tre-em/ | Thiet bi khu vui choi kids cafe co moc tham khao 300-600 tr, hoac 2,5-5 tr/m2 tuy loai. |
| E10 | Thi cong cafe san vuon 2026: https://xaydungminhduy.com/thiet-ke-thi-cong-tron-goi-quan-cafe.html va https://noithatdiemnhan.vn/bao-gia-thiet-ke-thi-cong-quan-cafe/ | Cafe san vuon/thi cong quan cafe thuong tinh theo m2 o muc trieu dong/m2, khong phu hop voi san vuon 525m2 chi 5,5-14 tr. |
| E11 | San vuon/san ngoai troi: https://vtvgarden.com/bao-gia-thi-cong-san-nha/ | Thi cong san ngoai troi co moc 350k-1,2 tr/m2 tuy vat lieu; chua tinh het canh quan, thoat nuoc, den, tuoi. |
| E12 | Dinh muc ngoi lop BXD/QD 1329: https://vatlieuxaydung.org.vn/Upload/48/Nam_2016/Tai_lieu/Chuong_II_DM_su_dung_VLXD_trong_xay_trat_hoan_thien_QD_1329_BXD_19122016.pdf | Ngoi 22: 22 vien/m2; neu 120m2 + 15% hao hut can ~3.036 vien. |

## 4. Findings

### F1 - Claim "v5.2 BOQ day du - khong con sot" la sai

Bang v5.2 chi cover mot scope gon: nha 10x20m, 61m2 nhom kinh, mai cong 120m2, san vuon nho. No **khong cover** day du cac item V7 da noi o dau file:

- Tran cao 5m va he treo/khung tran.
- Kiem dinh/ban ve ket cau cho mai cong phu nha 10x20m.
- Cua kinh xep truot cao 3,5m, khong phai cua lùa thong dung 3m.
- Vach kinh 10ly trong khu tre em voi yeu cau an toan.
- Montessori house.
- San vuon 15x35m = **525m2**, khong phai 30m2 san lap hay 5,5 tr cay/da.
- Dieu hoa cho the tich 200m2 x 5m = **1.000m3**.
- He thong thoat nuoc san vuon, chong ngap, chieu sang ngoai troi, camera ngoai troi.
- Bao tri/bao hanh va VAT/hoa don cho cac hang muc an toan.

**Impact:** Khong duoc goi 451 tr la full BOQ cho V7.

### F2 - He dieu hoa 13 tr la underquote nghiem trong

V7 ghi `Casper Inverter 24K x 2 = 13 tr`. Nguon thi truong 2026 cho thay may 24.000 BTU moi thuong khong o muc 6,5 tr/cai neu la hang chinh hang/inverter/cong suat lon. Quan trong hon, **2 may 24K chi phu hop khoang 60-80m2 tran thong thuong**, trong khi V7 noi tran 5m, dien tich 200m2, the tich 1.000m3.

**Audit range tam thoi:** neu lam that cho lounge + kid zone, nen reserve **45-120 tr** tuy zoning, cassette/treo tuong, so may, ong dong, thoat nuoc ngung, tu dien rieng. Con so 13 tr chi co the la placeholder cho 2 may gia re, khong phai giai phap lam mat.

### F3 - Nhom kinh 61m2 = 56 tr chi dung cho scope rui ro cao

V7 dung 56 tr cho 61m2 bang phuong an ket hop moi + 2nd. Neu chi la frame 2nd + thay kinh co chon loc thi co the dat, nhung no khong phu hop voi claim:

- `cua kinh xep truot 3,5m`
- `vach kinh 10ly`
- khu tre em can an toan, can tem/nguon kinh, phu kien, ray, khoa, chan gio, chong ket tay.

Nguon gia 2026 cho cua nhom Xingfa moi co the 1,4-3,8 tr/m2; kinh 10mm rieng da co moc ~750k/m2 chua tinh he ray/phu kien/cua. Vi vay 61m2 voi mot phan moi + mot phan 2nd nen dat **80-140 tr** neu can an toan va do cao 3,5m.

### F4 - San vuon 15x35m dang bi tinh nhu san vuon mini

`walkthrough.md` chi tinh san lap 30m2 = 2,4 tr va ngoai that san vuon 14 tr. V7 dau file lai noi **san vuon 15x35m = 525m2**. Hai scope khac nhau.

Ngay ca lam rat toi gian, 525m2 van can:

- lam phang/san lap/thoat nuoc;
- loi di, vat lieu nen, chong tron;
- cay, chau, bon, dat trong;
- chieu sang ngoai troi;
- ban ghe ngoai troi/dù/mai che;
- rao/phan luong an toan tre em;
- bao tri cay va tuoi.

**Audit range tam thoi:** **120-300 tr** cho san vuon 525m2 muc tiet kiem; co canh quan dep/quy hoach cafe san vuon co the cao hon. Con so **5,5-14 tr** la khong dung scope.

### F5 - Montessori house/khu vui choi premium chua duoc tinh

File chi co `do choi 2nd 5-9 tr` hoac `F3 camera + do choi + PCCC + GP = 32 tr`. Neu V7 thuc su co Montessori house, khu vui choi premium, kid zone co vách kính 10ly, thi con so nay thieu.

Nguon kids cafe 2026 cho thay thiet bi/khu vui choi co the tinh **2,5-5 tr/m2** hoac 300-600 tr cho cau hinh day du. Neu chi lam kid zone nho 35m2, reserve an toan cung nen **80-180 tr** tuy muc do. Neu lam "Montessori house" ngoai troi/indoor custom, can BOQ rieng: go/khung, san dem, lan can, chong kep tay, son an toan, lap dat.

### F6 - Mai cong 100-110 tr van sat day

Bang mai cong da sua nhieu loi dung: 3.036 vien ngoi, ton lanh khong goi la cach nhiet, bo sung phu kien/gian giao. Tuy nhien tong **101-149 tr** ma lai chon **110 tr** la chon sat day trong khi scope V7 co:

- mai phu nha 10x20m;
- tran 5m;
- keo go lo yeu cau tham my;
- go mit chua co bien ban do kho/moi mot/quy cach;
- chua co ban ve ket cau.

**Audit range tam thoi:** **130-180 tr** truoc khi co ban ve/bao gia 3 thau. 110 tr chi dung nhu target negotiation, khong dung lam ngan sach cam ket.

### F7 - PCCC + giay phep dang bi tron va co nguy co thieu

File co 3 moc khac nhau:

- D1 giay phep: 6,2-10,7 tr.
- D2 PCCC: 12,2-23,8 tr.
- v3 audit: PCCC 19 tr.
- v5.2 F3: camera + do choi + PCCC + GP = 32 tr.

Neu cafe 200m2, tran 5m, co khu tre em, co bep/quay pha che va dong nguoi, PCCC phai co scope ho so + thiet bi + nghiem thu theo yeu cau dia phuong. Khong nen gop nhieu hang muc vao F3 vi mat kha nang audit.

**Audit range tam thoi:** giay phep + ATTP + PCCC + ANTT + camera toi thieu **40-70 tr** neu lam ho so that va co yeu cau PC07/ATTP. Can tach line item.

### F8 - May pha/section A van la noi dung cu, mau thuan voi v5.2

Phan A van khuyen nghi Appia II 28-32 tr va tong A 54,5 tr. Nhưng v5/v5.2 lai dung `CRM 3120` va tong thiet bi pha che thanh ly **20,5 tr**. Hai phuong an nay khac nhau.

Can quyet dinh:

- `Premium espresso`: Appia II/Appia Life, reserve **50-65 tr** cho may + grinder + ro + phu kien + dọn máy.
- `Lean launch`: CRM/Gemilai, reserve **20-30 tr**, chap nhan nang cap sau.

Khong duoc de ca hai trong cung mot "tong".

### F9 - Thu hoi va cho thue nguyen trang la assumption, khong phai evidence

File ghi:

- thiet bi di dong mua 85 tr, ban lai 60-70 tr;
- cho thue nguyen trang 15-25 tr/thang;
- hoan von 18-30 thang.

Khong co evidence giao dich/bao gia/tham dinh cho thue. Day la scenario, khong phai co so ra quyet dinh dau tu. Nen dua vao phan "upside/exit assumption", khong dua vao bang tai chinh chinh.

### F10 - "Danh sach nguon mua da xac minh" chua du tieu chuan xac minh

Neu chi co website/SĐT/ten shop thi moi la **lead list**, chua phai "da xac minh". De goi la xac minh can co it nhat:

- anh hang/thong so/model;
- gia tai ngay bao;
- dieu kien bao hanh;
- tinh trang VAT/hoa don;
- chi phi van chuyen/lap dat;
- screenshot/bao gia/Zalo quote.

## 5. Budget audit - cach dung so nao

### 5.1. Neu chi lam scope v5.2 toi gian

Dung bang chi tiet hien co, sau khi sua cach cong:

| Muc | Range audit |
|---|---:|
| Tong GĐ1 theo dong chi tiet | ~430 tr |
| Neu tach lai PCCC/GP cho dung va khong double count | ~430-460 tr |
| GĐ2 solar + cua vom | +85-95 tr |
| **Tong toi gian 2 giai doan** | **515-555 tr** |

Day **khong phai** V7 full walkthrough. Day la minimum salvage/DIY launch.

### 5.2. Neu lam dung scope V7 da ghi o dau file

Them cac khoang thieu lon:

| Hang muc | Chenh/bo sung so voi v5.2 |
|---|---:|
| Dieu hoa dung scope tran 5m/200m2 | +35-100 tr |
| Kinh/cua xep truot/vach 10ly dung an toan | +25-85 tr |
| Mai cong/kết cấu/gian giao/bao ve chong dot | +20-70 tr |
| San vuon 525m2 | +100-280 tr |
| Montessori house/kid zone premium | +80-250 tr |
| PCCC/ATTP/ho so/camera ngoai troi tach dung | +10-40 tr |
| Du phong 10-15% thay vi 5% | +35-100 tr |

**Muc ra quyet dinh hop ly:** **900 tr - 1,35 ty**. Do do ket luan dau file **950 tr - 1,28 ty** la **co huong dung**, nhung can thay bang BOQ chi tiet thay vi chi gan vao tai lieu v5.2.

## 6. Sua file V7 nhu the nao

1. Tach thanh 2 tai lieu:
   - `V5.2_MINIMUM_LAUNCH_BOQ`: scope toi gian, 430-460 tr GĐ1, 515-555 tr ca solar+cua.
   - `V7_FULL_WALKTHROUGH_BOQ`: full scope, 900 tr-1,35 ty, co BOQ rieng.
2. Xoa hoac dem section A/B/C/D cu vao phu luc lich su; khong de cung "tong" voi v5.2.
3. Sua "BOQ day du - khong con sot" thanh "BOQ toi gian, con pending V7 full scope".
4. Tach F3 thanh 4 dong: giay phep, PCCC, camera, do choi. Khong gop.
5. Lap BOQ moi cho:
   - dieu hoa/thermal load;
   - nhom kinh/cua xep truot/vach 10ly;
   - Montessori house/kid zone;
   - san vuon 525m2;
   - ket cau mai cong/tran 5m;
   - PCCC/ATTP/thoat hiem.
6. Doi "da xac minh" thanh "lead can quote" neu chua co bao gia/screenshot.
7. Dua thu hoi/cho thue vao phan scenario rieng, khong tinh vao budget.

## 7. Ket luan ngan

V7 da sua dung mot viec quan trong: **366 tr la sai neu scope hien hanh co mai cong, kinh, san vuon va kid zone that**. Tuy nhien file hien tai van **chua the dung de ra quyet dinh thi cong** vi con tron nhieu phien ban va chua co BOQ cho full scope.

Moc dung de thao luan hien tai:

- **Minimum launch**: 430-460 tr GĐ1, 515-555 tr neu cong GĐ2.
- **Full V7 walkthrough**: 900 tr-1,35 ty.
- **951 tr-1,28 ty**: tam chap nhan nhu khung canh bao, nhung chua du evidence den tung hang muc.
