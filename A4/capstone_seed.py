"""My capstone's data on top of the course kit's fin_payables sandbox.

The kit's Ledgerline is unchanged; this only rewrites the records my tool reads, so they tell the
Northbridge Cycles story from A1/CAPSTONE.md (Pune, Rs., GST). Everything here is made up.

    from ledgerline.erp import ERP
    from capstone_seed import apply_capstone
    erp = ERP(modules=["fin_payables"])
    apply_capstone(erp)
    s = erp.session("PSHAH")

The sandbox clock stays on the kit's date, Monday 26 October 2026 (the day Emma asks about 4471).
"""


def apply_capstone(erp):
    x = erp.x

    # Suppliers: Indian GSTINs. Voltway Paints & Coatings gets the code used in my A3 document set.
    x("UPDATE supplier SET name='Voltway Cells Pvt. Ltd.', vat_no='24AABCV4471K1Z2', state='GJ', city='Ahmedabad' "
      "WHERE sup_cd='VC-EIN-0042'")
    for t in ("supplier", "ap_vbank", "ap_inv", "ap_ledger"):
        x(f"UPDATE {t} SET sup_cd='VP-PNT-0107' WHERE sup_cd='VPC-ROT-0107'")
    x("UPDATE supplier SET vat_no='24AAEFV2207M1Z5', state='GJ', city='Vadodara' WHERE sup_cd='VP-PNT-0107'")
    x("UPDATE ap_vbank SET msme='N' WHERE sup_cd='VC-EIN-0042'")          # capstone change 9: Voltway is not an MSME

    # The order and the goods receipt: 18,000 packs at Rs.1,276.80; 260 damaged + 40 defective, 17,700 accepted.
    x("UPDATE po_line SET qty=18000, rate=1276.80 WHERE po_no='PO/2026/01120'")
    x("UPDATE ap_grn SET qty_acc=17700 WHERE grn_no='GRN/2026/07804'")

    # Voltway Cells' invoice 4471: 18,000 x Rs.1,332.80 + IGST 18%, held twice (quantity first, as ap_save would).
    x("UPDATE ap_inv SET rate=1332.80, basic=23990400.0, tax_cd='IGST18', tax=4318272.0, gross=28308672.0, "
      "hold_cd='H-QTY' WHERE ap_no='AP/2026/03390'")
    x("DELETE FROM ap_hold_log WHERE ap_no='AP/2026/03390'")
    for cd, detail in (("H-QTY", "QTY 18000 VS OPEN 17700"), ("H-PRC", "RATE 1332.80 VS PO 1276.80 (+4.39%)")):
        x("INSERT INTO ap_hold_log(ap_no,hold_cd,detail,put_on) VALUES ('AP/2026/03390',?,?,'2026-10-05T15:05:00')",
          cd, detail)

    # Voltway Paints & Coatings' invoice, also numbered 4471 (the near-match trap).
    x("UPDATE ap_inv SET inv_dt='2026-10-20', basic=184000.0, tax_cd='IGST18', tax=33120.0, gross=217120.0, "
      "due_dt='2026-11-19', entered_on='2026-10-22T11:10:00' WHERE ap_no='AP/2026/03409'")
    x("UPDATE ap_ledger SET dt='2026-10-22', cr=217120.0 WHERE ref='AP/2026/03409'")
    x("UPDATE ap_gst SET vat_no='24AAEFV2207M1Z5', tax_cd='IGST18', itc_amt=33120.0 WHERE ap_no='AP/2026/03409'")

    # People: the plant is in Pune; Ganesh Pawar is stores (he releases quantity holds).
    x("UPDATE app_user SET ou_cd='NBC-PUN-01' WHERE ou_cd='NBC-MAN-01'")
    x("INSERT INTO app_user VALUES ('GPAWAR','Ganesh Pawar','STORES','NBC-PUN-01',0,'DOKAFOR','ganesh@123','PRD-05',"
      "'ganesh.pawar@northbridgecycles.example','@ganesh')")
    erp.db.commit()
