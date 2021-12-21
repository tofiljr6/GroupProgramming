let canvas;
let gl;

let curX;
let curY;
let count = 0;
let pressed = null;
let selected = null;

let size;
let tableSize;

window.onload = () => {
    canvas = document.querySelector("#layout");
    gl = canvas.getContext("2d");

    if (gl === null) {
        alert("Your browser or machine may not support WebGL.");
        return;
    }

    canvas.onpointermove = (e) => {
        const rect = canvas.getBoundingClientRect();
        curX = e.clientX - rect.left;
        curY = e.clientY - rect.top;
    };

    canvas.onpointerdown = () => {
        selected = null;
        for (let i = 0; i < count; i++) {
            const xData =  $("#x" + (i + 1)).val();
            const yData =  $("#y" + (i + 1)).val();
            const x = size * parseFloat(xData) / 1000;
            const y = size * parseFloat(yData) / 1000;
            if (curX >= x - (tableSize / 2) && curX <= x + (tableSize / 2) &&
                curY >= y - (tableSize / 2) && curY <= y + (tableSize / 2)) {
                pressed = i + 1;
                selected = i + 1;
                break;
            }
        }
    };

    canvas.onpointerup = () => {
        pressed = null;
    };

    function move() {
        if (pressed != null) {
            $("#x" + pressed).val(parseInt(1000 * curX / size));
            $("#y" + pressed).val(parseInt(1000 * curY / size));
        }
        draw();
        requestAnimationFrame(move);
    }

    redraw();
    move();

    $("#add").click(() => {
        count++;
        $("#tableList").append("<li id=\"" + count + "\">\n" +
            "                    <label for=\"x" + count + "\"><input id=\"x" + count + "\" name=\"x" + count + "\" value=\"500\"></label>\n" +
            "                    <label for=\"y" + count + "\"><input id=\"y" + count + "\" name=\"y" + count + "\" value=\"500\"></label>\n" +
            "                    <label for=\"state" + count + "\"><input id=\"state" + count + "\" name=\"state" + count + "\" value=\"FREE\"></label>\n" +
            "                   </li>");
    });
    $("#remove").click(() => {
        if (selected != null) {
            $("#x" + selected).val("");
            selected = null;
        }
    });
    $("#tableList").hide();
};

window.onresize = redraw;

function redraw() {
    size = Math.min(window.innerWidth, window.innerHeight) * 0.8
    tableSize = size * 0.05;
    canvas.width = size;
    canvas.height = size;
    count = parseInt($("#tableList").attr("count"));
    draw();
}

function draw() {
    gl.fillStyle = "#797979";
    gl.fillRect(0, 0, size, size);
    for (let i = 0; i < count; i++) {
        const xData =  $("#x" + (i + 1)).val();
        const yData =  $("#y" + (i + 1)).val();
        const x = size * parseFloat(xData) / 1000;
        const y = size * parseFloat(yData) / 1000;
        if (selected === i + 1) {
            gl.fillStyle = "#000000";
            gl.fillRect(x - (tableSize / 2) * 1.2, y - (tableSize / 2) * 1.2, tableSize * 1.2, tableSize * 1.2);
        }
        const state = $("#state" + (i + 1)).val();
        if (state === "BUSY") gl.fillStyle = "#9f3232";
        else if (state === "RESERVED") gl.fillStyle = "#b0983a";
        else if (state === "FREE") gl.fillStyle = "#85b22e";
        else gl.fillStyle = "#ffffff";
        gl.fillRect(x - (tableSize / 2), y - (tableSize / 2), tableSize, tableSize);
    }
}
