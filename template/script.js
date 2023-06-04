$(document).ready(function () {
    loadData();
    $(window).scroll(function () {
        // sticky navbar on scroll script
        if (this.scrollY > 20) {
            $('.navbar').addClass("sticky");
        } else {
            $('.navbar').removeClass("sticky");
        }

        // scroll-up button show/hide script
        if (this.scrollY > 500) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    });

    // slide-up script
    $('.scroll-up-btn').click(function () {
        $('html').animate({ scrollTop: 0 });
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function () {
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });

    // toggle menu/navbar script
    $('.menu-btn').click(function () {
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3,
                nav: false
            }
        }
    });
});

var loadData = function () {

    name1 = $(".nametext").eq(0);
    name2 = $(".nametext").eq(1);
    name3 = $(".nametext").eq(2);
    hireme = $("#mailto");
    aboutme = $("#about-me");
    cv = $("#cv");
    projects_ele = $("#projects");
    skills_experience = $("#skills-experience");
    skills_ele = $("#skills");
    references_ele = $("#references");

    get_in_touch_info = $("#get-in-touch-info");

    address = $("#address");
    email = $("#email");

    var flickerAPI = "data.json";
    $.getJSON(flickerAPI, {
        tagmode: "any",
        format: "json"
    }).done(function (data) {
        name1.text(data.name);
        name2.text("I'm " + data.name + " and");
        name3.text(data.name);
        hireme.attr("href", data.emailid);
        aboutme.text(data.aboutme);
        cv.attr("href", data.cv_link);

        projects = data.projects;

        for (const project of projects) {
            let project_name = project[0];
            let project_desc = project[1];
            let project_ele = `<div class="card"><div class="box"><div class="text">${project_name}</div><p>${project_desc}</p></div></div>`;

            projects_ele.append(project_ele);
        }

        skills_experience.text(data.skills_experience);
        skills = data.skills;

        for (const skill of skills) {
            let skill_name = skill[0];
            let skill_perc = skill[1];

            let skill_ele = `<div class="bars"><div class="info"><span>${skill_name}</span><span>${skill_perc}%</span></div><div class="line html"></div></div>`;

            skills_ele.append(skill_ele);
        }


        references = data.references;

        for (const reference of references) {
            let reference_name = reference[0];
            let reference_desc = reference[1];
            let reference_linkedin = reference[2];

            let reference_ele = `<div class="card"><div class="box"><img src="images/profile-1.jpeg"><div class="text">${reference_name}</div><p>${reference_desc}</p><a href="${reference_linkedin}"><i id="linkedin-icon" class='fab fa-linkedin-in'></i></a></div></div>`;

            references_ele.append(reference_ele);
        }

        get_in_touch_info.text(data.get_in_touch);
        address.text(data.address);
        email.text(data.emailid);

        typo_skills = data.typo_skills;

        // typing text animation script
        var typed = new Typed(".typing", {
            strings: typo_skills,
            typeSpeed: 100,
            backSpeed: 60,
            loop: true
        });

        var typed = new Typed(".typing-2", {
            strings: typo_skills,
            typeSpeed: 100,
            backSpeed: 60,
            loop: true
        });

    });
} 