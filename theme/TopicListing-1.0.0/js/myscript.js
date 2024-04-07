function set_checkbox(){
    var e = document.getElementById("download-form");
    var value = document.getElementById("main-box").checked;
    console.log(value);
    if (value) {
        set_boxes(true);
    } else {
        set_boxes(false);
    }

}

function set_boxes(val) {
    var els = document.getElementsByClassName("select-box");
    if (val) {
        console.log("set on");
        for (let i = 0; i < els.length; i++) {
            const element = els[i];
            element.checked = true;
        }
    } else {
        console.log("set off");
        for (let i = 0; i < els.length; i++) {
            const element = els[i];
            element.checked = false;
        }
    }
}