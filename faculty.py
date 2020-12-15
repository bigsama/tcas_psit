""" Probability Calculation Into Faculties's KMITL """
def engineering(gat, pat2, pat3):
    """ Calculate Score For Engineering Faculty """
    score_gat = (gat / 300) * 15
    score_pat2 = (pat2 / 300) * 15
    score_pat3 = (pat3 / 300) * 20
    total_score = ((score_gat + score_pat2 + score_pat3) / 50) * 15000
    return total_score

def architecture(gat, pat4):
    """ Calculate Score For Architecture Faculty """
    score_gat = (gat / 300) * 10
    score_pat4 = (pat4 / 300) * 40
    total_score = ((score_gat + score_pat4) / 50) * 15000
    return total_score

def industrial_education(gat, pat2, pat3, pat4, pat5, sub):
    """ Calculate Score For Industrial Education Faculty """
    score = lambda x, y, z: ((x / 300) * 10) + ((y / 300) * 20) + ((z / 300) * 20)
    if sub in "วิชาสถาปัตยกรรม วิชาการออกแบบสภาพแวดล้อมภายใน วิชาครุศาสตร์การออกแบบ":
        total_score = (score(gat, pat5, pat4) / 50) * 15000
        return total_score
    elif sub in "วิชาครุศาสตร์วิศวกรรม":
        total_score = (score(gat, pat5, pat3) / 50) * 15000
        return total_score
    else:
        total_score = (score(gat, pat5, pat2) / 50) * 15000
        return total_score

def agricultural_technology(gat, pat1, pat2):
    """ Calculate Score For Agricultural Technology Faculty """
    score_gat = (gat / 300) * 10
    score_pat1 = (pat1 / 300) * 20
    score_pat2 = (pat2 / 300) * 20
    total_score = ((score_gat + score_pat1 + score_pat2) / 50) * 15000
    return total_score

def science(gat, pat1, pat2):
    """ Calculate Score For Science Faculty """
    score_gat = (gat / 300) * 10
    score_pat1 = (pat1 / 300) * 10
    score_pat2 = (pat2 / 300) * 30
    total_score = ((score_gat + score_pat1 + score_pat2) / 50) * 15000
    return total_score

def information_technology(gat, pat1, pat2):
    """ Calculate Score For Information Technology Faculty """
    score_gat = (gat / 300) * 10
    score_pat1 = (pat1 / 300) * 20
    score_pat2 = (pat2 / 300) * 20
    total_score = ((score_gat + score_pat1 + score_pat2) / 50) * 15000
    return total_score

def agro_industry(gat, pat1, pat2):
    """ Calculate Score For Agro-Industry Faculty """
    score_gat = (gat / 300) * 10
    score_pat1 = (pat1 / 300) * 10
    score_pat2 = (pat2 / 300) * 30
    total_score = ((score_gat + score_pat1 + score_pat2) / 50) * 15000
    return total_score

def business_administration(gat, pat1):
    """ Calculate Score For Business Administration Faculty """
    score_gat = (gat / 300) * 30
    score_pat1 = (pat1/ 300) * 20
    total_score = ((score_gat + score_pat1) / 50) * 15000
    return total_score

def nano_kmitl(gat, pat2, pat3):
    """ Calculate Score For Nanotechnology KMITL """
    score_gat = (gat / 300) * 15
    score_pat2 = (pat2 / 300) * 15
    score_pat3 = (pat3 / 300) * 20
    total_score = ((score_gat + score_pat2 + score_pat3) / 50) * 15000
    return total_score

def engineering_manufacturing(gat, pat2, pat3):
    """ Calculate Score For Engineering Manufacturing """
    score_gat = (gat / 300) * 15
    score_pat2 = (pat2 / 300) * 15
    score_pat3 = (pat3 / 300) * 20
    total_score = ((score_gat + score_pat2 + score_pat3) / 50) * 15000
    return total_score

def aviation_industry(gat, pat1, pat2, pat3, sub):
    """ Calculate Score For Aviation Industry """
    engineer_aviation = lambda x, y, z: ((x / 300) * 15) + ((y / 300) * 15) + ((z / 300) * 20)
    logistic_aviation = lambda x, y: ((x / 300) * 30) + ((y / 300) * 20)
    if sub == "สาขาวิชาวิศวกรรมการบินและนักบินพาณิชย์(หลักสูตรนานาชาติ)":
        total_score = (engineer_aviation(gat, pat2, pat3) / 50) * 15000
        return total_score
    else:
        total_score = (logistic_aviation(gat, pat1) / 50) * 15000
        return total_score

def liberal_arts(gat, pat7, sub):
    """ Calculate Score For Liberal Arts Faculty """
    english = (gat / 300) * 50
    japan = lambda x, y: ((x / 300) * 30) + ((y / 300) * 20)
    if sub in "วิชาภาษาอังกฤษ วิชานวัตกรรมการท่องเที่ยวและการบริการ":
        total_score = (english / 50) * 15000
        return total_score
    else:
        total_score = (japan(gat, pat7) / 50) * 15000
        return total_score

def pcc_kmitl(gat, pat1, pat2, pat3, sub):
    """ Calculate Score For PCC KMITL """
    sci = lambda x, y, z: ((x / 300) * 10) + ((y / 300) * 10) + ((z / 300) * 30)
    engineering = lambda x, y, z: ((x / 300) * 15) + ((y / 300) * 15) + ((z / 300) * 20)
    business = lambda x, y: ((x / 300) * 30) + ((y / 300) * 20)

    if sub in "วิทยาศาสตร์การประมงและทรัพยากรทางน้ำ วิชาสัตวศาสตร์แขนงการผลิตและธุรกิจปศุสัตว์ \
        วิชาสัตวศาสตร์แขนงการผลิตและธุรกิจสัตว์เลี้ยง วิชาเทคโนโลยีการจัดการผลิตพืช วิชานวัตกรรมอาหารและการจัดการ":
        total_score = (sci(gat, pat1, pat2) / 50) * 15000
        return total_score
    elif sub in "วิชาวิศวกรรมเครื่องกล วิชาวิศวกรรมเครื่องกลแขนงเกษตรอัจฉริยะ \
        วิชาวิศวกรรมเครื่องกลแขนงวิศวกรรมพลังงาน วิชาวิศวกรรมคอมพิวเตอร์ วิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมไฟฟ้าสื่อสาร \
            วิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมอิเล็กทรอนิกส์ วิชาวิศวกรรมหุ่นยนต์และอิเล็กทรอนิกส์อัจฉริยะ":
        total_score = (engineering(gat, pat2, pat3) / 50) * 15000
        return total_score
    else:
        total_score = (business(gat, pat1) / 50) * 15000
        return total_score
