import eel
import faculty as fac

## Initilization
eel.init('static')

@eel.expose
def calculate(gpax, oth, osc, oeng, omath, oscience, gat, gatth, gateng, pat1, pat2, pat3, pat4, pat5, pat6, pat71, pat72, pat73, pat74, pat75, pat76, fac1, maj1, fac2, maj2, fac3, maj3, fac4, maj4, fac5, maj5):
    """ Recieve A Score """
    gpax = float(gpax)
    onet = {
        "THAI": float(oth),
        "SOCIAL": float(osc),
        "ENGLISH": float(oeng),
        "MATH": float(omath),
        "SCIENCE": float(oscience)
    }
    score = {
        "GAT": float(gat),
        "GAT TH": float(gatth),
        "GAT ENG": float(gateng),
        "PAT1": float(pat1),
        "PAT2": float(pat2),
        "PAT3": float(pat3),
        "PAT4": float(pat4),
        "PAT5": float(pat5),
        "PAT6": float(pat6),
        "PAT7.1": float(pat71),
        "PAT7.2": float(pat72),
        "PAT7.3": float(pat73),
        "PAT7.4": float(pat74),
        "PAT7.5": float(pat75),
        "PAT7.6": float(pat76),
    }
    faculty_branch = {
        "Order 1": [fac1, maj1],
        "Order 2": [fac2, maj2],
        "Order 3": [fac3, maj3],
        "Order 4": [fac4, maj4],
        "Order 5": [fac5, maj5]
    }
    faculty_score = []

    score_gpax = gpax * 1500
    sumscore_onet = onet["THAI"] + onet["SOCIAL"] + onet["ENGLISH"] + onet["MATH"] + onet["SCIENCE"]
    score_onet = sumscore_onet * 18
    result = []

    for order in faculty_branch:
        if faculty_branch[order][0] == "คณะวิศวกรรมศาสตร์":
            gat_pat = fac.engineering(score["GAT"], score["PAT2"], score["PAT3"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะสถาปัตยกรรมศาสตร์":
            gat_pat = fac.architecture(score["GAT"], score["PAT4"])
            result = score_onet + score_gpax + gat_pat
            condition = onet["ENGLISH"] >= 30 and score["PAT4"] >= 120 and gpax >= 2.75
            chance = ((result / 30000) * 100) * condition
        elif faculty_branch[order][0] == "คณะครุศาสตร์อุตสาหกรรม":
            gat_pat = fac.industrial_education(score["GAT"], score["PAT2"], score["PAT3"], score["PAT4"], score["PAT5"], faculty_branch[order][1])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะเทคโนโลยีการเกษตร":
            gat_pat = fac.agricultural_technology(score["GAT"], score["PAT1"], score["PAT2"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะวิทยาศาสตร์":
            gat_pat = fac.science(score["GAT"], score["PAT1"], score["PAT2"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะเทคโนโลยีสารสนเทศ":
            gat_pat = fac.information_technology(score["GAT"], score["PAT1"], score["PAT2"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะอุตสาหกรรมเกษตร":
            gat_pat = fac.agro_industry(score["GAT"], score["PAT1"], score["PAT2"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะบริหารธุรกิจ":
            gat_pat = fac.business_administration(score["GAT"], score["PAT1"])
            result = score_onet + score_gpax + gat_pat
            condition1 = faculty_branch[order][1] == "วิชาเศรษฐศาสตรธุรกิจและการจัดการ" and score["GAT"] >= 110
            condition2 = score["PAT1"] >= 50 and gpax >= 2.75
            chance = ((result / 30000) * 100) * (condition1 and condition2)
        elif faculty_branch[order][0] == "วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง":
            gat_pat = fac.nano_kmitl(score["GAT"], score["PAT2"], score["PAT3"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "วิทยาลัยนวัตกรรมการผลิตขั้นสูง":
            gat_pat = fac.engineering_manufacturing(score["GAT"], score["PAT2"], score["PAT3"])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "วิทยาลัยอุตสาหกรรมการบินนานาชาติ":
            gat_pat = fac.aviation_industry(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][1])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        elif faculty_branch[order][0] == "คณะศิลปศาสตร์":
            if faculty_branch[order][1] in "สาขาวิชาภาษาญี่ปุ่น":
                gat_pat = fac.liberal_arts(score["GAT"], score["PAT7.3"], faculty_branch[order][1])
            else:
                gat_pat = fac.liberal_arts(score["GAT"], 0, faculty_branch[order][1])
            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        else:
            if faculty_branch[order][1] in "วิทยาศาสตร์การประมงและทรัพยากรทางน้ำ วิชาสัตวศาสตร์แขนงการผลิตและธุรกิจปศุสัตว์ \
                วิชาสัตวศาสตร์แขนงการผลิตและธุรกิจสัตว์เลี้ยง วิชาเทคโนโลยีการจัดการผลิตพืช วิชานวัตกรรมอาหารและการจัดการ":
                gat_pat = fac.pcc_kmitl(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][1])
            elif faculty_branch[order][1] in "วิชาวิศวกรรมเครื่องกล วิชาวิศวกรรมเครื่องกลแขนงเกษตรอัจฉริยะ \
                วิชาวิศวกรรมเครื่องกลแขนงวิศวกรรมพลังงาน วิชาวิศวกรรมคอมพิวเตอร์ วิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมไฟฟ้าสื่อสาร \
                    วิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมอิเล็กทรอนิกส์ วิชาวิศวกรรมหุ่นยนต์และอิเล็กทรอนิกส์อัจฉริยะ":
                gat_pat = fac.pcc_kmitl(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][1])
            else:
                gat_pat = fac.pcc_kmitl(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][1])

            result = score_onet + score_gpax + gat_pat
            chance = (result / 30000) * 100
        faculty_score.append([faculty_branch[order][0], faculty_branch[order][1], chance])
    #eel.process(faculty_score)
    print(faculty_score)
    return faculty_score

## Starting UI
eel.start('index.html', size=(1500, 910))