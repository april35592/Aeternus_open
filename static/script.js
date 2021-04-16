// diary toggle

const image_delete = document.querySelectorAll(".image_delete span")
const image_delete_form = document.querySelectorAll(".image_delete form")
const reply_delete = document.querySelectorAll(".reply_delete span")
const reply_delete_form = document.querySelectorAll(".reply_delete form")
const reply_create = document.querySelectorAll(".reply_button")
const reply_create_form = document.querySelectorAll(".input_reply")

for (let i = 0; i < image_delete.length; i++) {
    image_delete[i].addEventListener("click", function(event) {
        image_delete[i].style.display = "none";
        image_delete_form[i].classList.remove("hidden");
    });
};

for (let i = 0; i < reply_delete.length; i++) {
    reply_delete[i].addEventListener("click", function(event) {
        reply_delete[i].style.display = "none";
        reply_delete_form[i].classList.remove("hidden");
    });
};

for (let i = 0; i < reply_create.length; i++) {
    reply_create[i].addEventListener("click", function(event) {
        reply_create[i].style.display = "none";
        reply_create_form[i].classList.remove("hidden");
    });
};


// bbs reply toggle

const reply_h3 = document.querySelectorAll(".reply_list h3");
const reply_diraction = document.querySelectorAll(".reply_list span");
const reply_p = document.querySelectorAll(".reply_list p");

for (let i = 0; i < reply_h3.length; i++) {
    reply_h3[i].addEventListener("click", function(event) {
        if(reply_p[i].style.display == "none") {
            reply_p[i].style.display = "block";
            reply_diraction[i].innerText = "△";
        } else {
            reply_p[i].style.display = "none";
            reply_diraction[i].innerText = "▽";
        }
    })
};
