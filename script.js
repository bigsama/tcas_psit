$(window).on("load",function(){
    $(".loader-container").fadeOut(2000);
});

function select_box_faculty(faculty) {
    switch (faculty) {
        case "คณะวิศวกรรมศาสตร์":
            return ["สาขาวิชาวิศวกรรมโทรคมนาคมและโครงข่าย", "สาขาวิชาวิศวกรรมไฟฟ้า", "สาขาวิชาวิศวกรรมอิเล็กทรอนิกส์", "สาขาวิชาวิศวกรรมคอมพิวเตอร์",
                "สาขาวิชาวิศวกรรมเมคคาทรอนิกส์และออโตเมชัน", "สาขาวิชาวิศวกรรมเคมี", "สาขาวิชาวิศวกรรมเครื่องกล", "สาขาวิชาวิศวกรรมเกษตรอัจฉริยะ", "สาขาวิชาวิศวกรรมโยธา",
                "สาขาวิชาวิศวกรรมอุตสาหการ", "สาขาวิชาวิศวกรรมขนส่งทางราง", "สาขาวิชาวิศวกรรมอาหาร"];
        case "คณะสถาปัตยกรรมศาสตร์":
            return ["สาขาวิชาศิลปอุตสาหกรรม"];
        case "คณะครุศาสตร์อุตสาหกรรม":
            return ["สาขาวิชาสถาปัตยกรรม", "สาขาวิชาการออกแบบสภาพแวดล้อมภายใน", "สาขาวิชาครุศาสตร์การออกแบบ", "สาขาวิชาครุศาสตร์วิศวกรรม", "สาขาวิชาครุศาสตร์เกษตร"];
        case "คณะเทคโนโลยีการเกษตร":
            return ["สาขาวิชาเทคโนโลยีการผลิตพืช", "สาขาวิชาการจัดการฟาร์มอย่างชาญฉลาด", "สาขาวิชาภูมิทัศน์เพื่อสิ่งแวดล้อม", "สาขาวิชาเทคโนโลยีการผลิตสัตว์และวิทยาศาสตร์เนื้อสัตว์",
                "สาขาวิชานวัตกรรมการผลิตสัตว์น้ำและการจัดการทรัพยากรประมง", "สาขาวิชาพัฒนาการเกษตร", "สาขาวิชานิเทศศาสตร์เกษตร"];
        case "คณะวิทยาศาสตร์":
            return ["สาขาวิชาคณิตศาสตร์ประยุกต์", "สาขาวิชาวิทยาการคอมพิวเตอร์", "สาขาวิชาเคมีอุตสาหกรรม", "สาขาวิชาเคมีสิ่งแวดล้อม", "สาขาวิชาเทคโนโลยีชีวภาพ", "สาขาวิชาจุลชีววิทยาอุตสาหกรรม",
                "สาขาวิชาฟิสิกส์อุตสาหกรรม", "สาขาวิชาสถิติประยุกต์", "สาขาวิชาเคมีวิศวกรรมและอุตสาหกรรม (นานาชาติ)"];
        case "คณะเทคโนโลยีสารสนเทศ":
            return ["สาขาวิชาเทคโนโลยสารสนเทศ", "สาขาวิชาวิทยาการข้อมูลและการวิเคราะห์เชิงธุรกิจ", "สาขาวิชาเทคโนโลยสารสนเทศทางธุรกิจ (นานาชาติ)"];
        case "คณะอุตสาหกรรมเกษตร":
            return ["สาขาวิชาวิทยาศาสตร์และเทคโนโลยีการอาหาร", "สาขาวิชาเทคโนโลยีการหมักในอุตสาหกรรมอาหาร", "สาขาวิชาวิศวกรรมแปรรูปอาหาร", "Culinary Science and Foodservice Management (International Program)"];
        case "คณะบริหารธุรกิจ":
            return ["หลักสูตรบริหารธุรกิจ แขนงนวัตกรรมการจัดการอุตสาหกรรม", "หลักสูตรบริหารธุรกิจ แขนงการจัดการและการเป็นผู้ประกอบการนวัตกรรม", "สาขาวิชาเศรษฐศาสตรธุรกิจและการจัดการ"];
        case "คณะศิลปศาสตร์":
            return ["สาขาวิชาภาษาอังกฤษ", "สาขาวิชาภาษาญี่ปุ่น", "สาขาวิชานวัตกรรมการท่องเที่ยวและการบริการ"];
        case "วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง":
            return ["สาขาวิชาวิศวกรรมวัสดุนาโน", "Smart Materials Technology and Engineering Program in Robotics and AI (Dual Degree) (International Program)"];
        case "วิทยาลัยนวัตกรรมการผลิตขั้นสูง":
            return ["สาขาวิชาวิศวกรรมระบบการผลิต", "สาขาวิชาวิศวกรรมการบินและนักบินพาณิชย์ (หลักสูตรนานาชาติ)", "สาขาวิชาการจัดการโลจิสติกส์ (หลักสูตรนานาชาติ)"];
        case "วิทยาเขตชุมพรเขตรอุดมศักดิ์":
            return ["สาขาวิทยาศาสตร์การประมงและทรัพยากรทางน้ำ", "สาขาวิชาสัตวศาสตร์แขนงการผลิตและธุรกิจปศุสัตว์", "สาขาวิชาสัตวศาสตร์แขนงการผลิตและธุรกิจสัตว์เลี้ยง", "สาขาวิชาเทคโนโลยีการจัดการผลิตพืช",
                "สาขาวิชาวิศวกรรมเครื่องกล", "สาขาวิชาวิศวกรรมเครื่องกลแขนงเกษตรอัจฉริยะ", "สาขาวิชาวิศวกรรมเครื่องกลแขนงวิศวกรรมพลังงาน", "สาขาวิชาวิศวกรรมคอมพิวเตอร์", "สาขาวิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมไฟฟ้าสื่อสาร",
                "สาขาวิชาวิศวกรรมไฟฟ้าแขนงวิศวกรรมอิเล็กทรอนิกส์", "สาขาวิชาวิศวกรรมหุ่นยนต์และอิเล็กทรอนิกส์อัจฉริยะ", "สาขาวิชาบริหารธุรกิจและการเป็นผู้ประกอบการ", "สาขาวิชาบริหารธุรกิจและการเป็นผู้ประกอบการ กับ การจัดการการท่องเที่ยวและการบริการ มหาวิทยาลัยรังสิต",
                "สาขาวิชาบริหารธุรกิจและการเป็นผู้ประกอบการ กับ การจัดการธุรกิจการบิน มหาวิทยาลัยรังสิต", "สาขาวิชานวัตกรรมอาหารและการจัดการ"];
        default:
            return ["ไม่พบข้อมูลสาขา"];
    }
}

$(document).ready(function () {
    //force input only number and dot
    $('input').keypress(function(evt){
        return (/^[0-9]*\.?[0-9]*$/).test($(this).val()+evt.key);
    });

    const stepper = new mdb.Stepper(document.getElementById('stepper-buttons'));

    document.getElementById('next-step').addEventListener('click', () => {
        stepper.nextStep();
    });

    document.getElementById('prev-step').addEventListener('click', () => {
        stepper.previousStep();
    });

    $('.select.faculty_1').on('change', function () {
        var this_obj = $(this);
        $('.select.major_1 > option').remove();
        $.each(select_box_faculty(this_obj.val()), function (i, item) {
            $('.select.major_1').append('<option value="' + item + '">' + item + '</option>');
        });
    });
    $('.select.faculty_2').on('change', function () {
        var this_obj = $(this);
        $('.select.major_2 > option').remove();
        $.each(select_box_faculty(this_obj.val()), function (i, item) {
            $('.select.major_2').append('<option value="' + item + '">' + item + '</option>');
        });
    });
    $('.select.faculty_3').on('change', function () {
        var this_obj = $(this);
        $('.select.major_3 > option').remove();
        $.each(select_box_faculty(this_obj.val()), function (i, item) {
            $('.select.major_3').append('<option value="' + item + '">' + item + '</option>');
        });
    });
    $('.select.faculty_4').on('change', function () {
        var this_obj = $(this);
        $('.select.major_4 > option').remove();
        $.each(select_box_faculty(this_obj.val()), function (i, item) {
            $('.select.major_4').append('<option value="' + item + '">' + item + '</option>');
        });
    });
    $('.select.faculty_5').on('change', function () {
        var this_obj = $(this);
        $('.select.major_5 > option').remove();
        $.each(select_box_faculty(this_obj.val()), function (i, item) {
            $('.select.major_5').append('<option value="' + item + '">' + item + '</option>');
        });
    });
});

function process() {
    var [gpa, gat, gatth, gateng] = [parseFloat($("#gpa").val()) || 0, parseFloat($("#gat").val()) || 0, parseFloat($("#gatth").val()) || 0, parseFloat($("#gateng").val()) || 0];
    var [oth, osc, oeng, omath, osci] = [parseFloat($("#oth").val()) || 0, parseFloat($("#osc").val()) || 0, parseFloat($("#oeng").val()) || 0, parseFloat($("#omath").val()) || 0, parseFloat($("#osci").val()) || 0];
    var [pat1, pat2, pat3, pat4, pat5, pat6] = [parseFloat($("#pat1").val()) || 0, parseFloat($("#pat2").val()) || 0, parseFloat($("#pat3").val()) || 0, parseFloat($("#pat4").val()) || 0, parseFloat($("#pat5").val()) || 0, parseFloat($("#pat6").val()) || 0];
    var [pat71, pat72, pat73, pat74, pat75, pat76] = [parseFloat($("#pat71").val()) || 0, parseFloat($("#pat72").val()) || 0, parseFloat($("#pat73").val()) || 0, parseFloat($("#pat74").val()) || 0, parseFloat($("#pat75").val()) || 0, parseFloat($("#pat76").val()) || 0];
    var [fac1, fac2, fac3, fac4, fac5] = [$(".select.faculty_1").val() || "ไม่พบข้อมูล", $(".select.faculty_2").val() || "ไม่พบข้อมูล", $(".select.faculty_3").val() || "ไม่พบข้อมูล", $(".select.faculty_4").val() || "ไม่พบข้อมูล", $(".select.faculty_5").val() || "ไม่พบข้อมูล"];
    var [maj1, maj2, maj3, maj4, maj5] = [$(".select.major_1").val() || "ไม่พบข้อมูล", $(".select.major_2").val() || "ไม่พบข้อมูล", $(".select.major_3").val() || "ไม่พบข้อมูล", $(".select.major_4").val() || "ไม่พบข้อมูล", $(".select.major_5").val() || "ไม่พบข้อมูล"];
    $('#process tbody').empty();
    eel.calculate(gpa, gat, gatth, gateng, oth, osc, oeng, omath, osci, pat1, pat2, pat3, pat4, pat5, pat6, pat71, pat72, pat73, pat74, pat75, pat76, fac1, maj1, fac2, maj2, fac3, maj3, fac4, maj4, fac5, maj5)(process_2);
}

function process_2(process_result) {
    $(".top-text").text("โอกาศติด");
    $.each(process_result, function (i, item) {
        $('#process > tbody').append('<tr><td>' + parseInt(i+1) + '</td><td>' + item[0] + '</td><td>' + item[1] + '</td><td>' + parseFloat(item[2]).toFixed(2) + '%</td></tr>');
    });
    var chance = parseFloat(process_result[0][2]);
    $("#score").text(chance.toFixed(2) + "%");
    $("#fac_major_first").text(process_result[0][0] + " " + process_result[0][1]);
    
    if(chance > 80) {
        $(".emotion").fadeOut(function(){
            $(this).attr("src", "https://www.flaticon.com/svg/static/icons/svg/3706/3706784.svg").fadeIn();
        });
        $("#process_desc").text("ผลจากการคำนวณเป็นเปอร์เซ็ตแล้ว โอกาศติดมากกว่า 80% ถือว่าโอกาศเยอะมากในการติดคณะนี้ เหมาะแก่การเสี่ยง! ขอให้ติดสาธุจ้า. 🙏");
    } else if(chance > 60 && chance < 80) {
        $(".emotion").fadeOut(function(){
            $(this).attr("src", "https://www.flaticon.com/svg/static/icons/svg/3706/3706769.svg").fadeIn();
        });
        $("#process_desc").text("ผลจากการคำนวณเป็นเปอร์เซ็ตแล้ว ถือว่าโอกาศติดยังเยอะอยู่ ลองยื่นคณะนี้ดูได้.");
    } else if(chance > 50 && chance < 60) {
        $(".emotion").fadeOut(function(){
            $(this).attr("src", "https://www.flaticon.com/svg/static/icons/svg/3707/3707027.svg").fadeIn();
        });
        $("#process_desc").text("ผลจากการคำนวณเป็นเปอร์เซ็ตแล้ว โอกาศในการติดประมาณ 50% ลองดูไม่เสียหาย แต่ถ้าอยากติดก็อ่านหนังสือสักหน่อย.");
    } else if(chance > 40 && chance < 50) {
        $(".emotion").fadeOut(function(){
            $(this).attr("src", "https://www.flaticon.com/svg/static/icons/svg/3706/3706997.svg").fadeIn();
        });
        $("#process_desc").text('ผลจากการคำนวณเป็นเปอร์เซ็ตแล้ว โอกาศในการติดนั้น ถือว่า "หวาดเสี่ยว" มากแต่ก็ยังมีโอกาศติดนะ แต่ก็เสี่ยงหน่อย.');
    } else {
        $(".emotion").fadeOut(function(){
            $(this).attr("src", "https://www.flaticon.com/svg/static/icons/svg/3707/3707024.svg").fadeIn();
        });
        $("#process_desc").text("ผลจากการคำนวณเป็นเปอร์เซ็ตแล้ว โอกาศในการติดนั้น ถือว่าต่ำมาก ลองเปลี่ยนคณะอื่นดูดีกว่า หรือไม่ก็ ไปไหว้พระขอพรขอให้ติด. 🙏");
    }
}