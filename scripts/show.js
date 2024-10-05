$(document).ready(function () {
    $('#homeBtn').click(function () {
        window.scrollTo(0, 0);
        $('#homeBtn').addClass('active');
        $('#homeBtn').attr("aria-current", "page");
        $('#secondBtn').removeClass('active');
        $('#thirdBtn').removeClass('active');
        $('#home').removeClass('d-none');
        $('#second').addClass('d-none');
    });
});

$(document).ready(function () {
    $('#secondBtn').click(function () {
        window.scrollTo(0, 0);
        $('#secondBtn').addClass('active');
        $('#secondBtn').attr("aria-current", "page");
        $('#homeBtn').removeClass('active');
        $('#thirdBtn').removeClass('active');
        $('#home').addClass('d-none');
        $('#second').removeClass('d-none');
    });
});

$(document).ready(function () {
    $('#thirdBtn').click(function () {
        window.scrollTo(0, 0);
        $('#thirdBtn').addClass('active');
        $('#thirdBtn').attr("aria-current", "page");
        $('#homeBtn').removeClass('active');
        $('#secondBtn').removeClass('active');
        $('#thirdBtn').addClass('active');
        $('#home').addClass('d-none');
        $('#second').addClass('d-none');
    });
});
