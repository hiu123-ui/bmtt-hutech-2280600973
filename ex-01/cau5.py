sogiolam=float(input("Nhap so gio lam viec: "))
luonggio=float(input("Nhap luong 1 gio lam viec: "))
giotieuchuan=4
giovuotchan=max(sogiolam-giotieuchuan,0)
thuclinhtieuchuan=luonggio*giotieuchuan+giovuotchan*luonggio*1.5
print(f"Luong cua ban la: {thuclinhtieuchuan}")