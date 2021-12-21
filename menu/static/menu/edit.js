let typesCount = 1
let dishesCount = 1

$(document).ready(() => {
    for (let i = 1; i < $("#menu").children().length + 1; i++) {
        let k = typesCount;
        typesCount++;
        njsAddDish(k);
        njsRmType(k);
        njsRevertType(k);

        for (let j = 1; j < ($("#dishes" + k).children().length) + 1; j++) {
            let c = dishesCount;
            dishesCount++;
            njsRmDish(k, c);
            njsRevertDish(k, c);
        }
    }

    $("#addType").click(() => {
        let k = typesCount;
        typesCount++;
        $("#menu").append(htmlType(k));
        njsAddDish(k);
        njsRmType(k);
    });
});

function njsAddDish(k) {
    $("#addDish" + k).click(() => {
        let c = dishesCount;
        dishesCount++;
        $("#dishes" + k).append(htmlDish(k, c));
        njsRmDish(k, c);
    });
}

function njsRmDish(k, c) {
    $("#" + k + "removeDish" + c).click(() => {
        $("#" + k + "newDishName" + c).val("");
        $("#" + k + "dish" + c).hide();
    });
}

function njsRevertDish(k, c) {
    $("#" + k + "revertDish" + c).click(() => {
        let name = $("#" + k + "newDishName" + c);
        let price = $("#" + k + "newDishPrice" + c);
        name.val(name.attr("placeholder"));
        price.val(price.attr("placeholder"));
    });
}

function njsRmType(k) {
    $("#removeType" + k).click(() => {
        $("#newTypeName" + k).val("");
        $("#type" + k).hide();
    });
}

function njsRevertType(k) {
    $("#revertType" + k).click(() => {
        let name = $("#newTypeName" + k);
        name.val(name.attr("placeholder"));
    });
}

function htmlType(c) {
    return "    <li id=\"type" + c + "\">" +
            "       <ul class=\"list-inline\">" +
            "           <li><label for=\"newTypeName" + c + "\">" +
            "               <input id=\"newTypeName" + c + "\" name=\"newTypeName" + c + "\" type=\"text\">" +
            "           </label></li>" +
            "           <li><button type=\"button\" id=\"removeType" + c + "\">Remove</button></li>" +
            "           <li><button type=\"button\" id=\"addDish" + c + "\" id=\"addDish" + c + "\">Add new dish</button></li>" +
            "       </ul>" +
            "       <ul id=\"dishes" + c + "\">" +
            "       </ul>" +
            "   </li>"
}

function htmlDish(k, c) {
    return "    <li id=\"" + k + "dish" + c + "\" class=\"list-group-item\">" +
            "       <a>" +
            "           <label for=\"" + k + "newDishName" + c + "\">" +
            "           <input id=\"" + k + "newDishName" + c + "\" name=\"" + k + "newDishName" + c + "\" type=\"text\">" +
            "           </label>" +
            "           <button type=\"button\" id=\"" + k + "removeDish" + c + "\">Remove</button>" +
            "       </a>" +
            "       <span class=\"badge\"><label for=\"" + k + "newDishPrice" + c + "\">" +
            "           <input id=\"" + k + "newDishPrice" + c + "\" name=\"" + k + "newDishPrice" + c + "\" type=\"number\" step=\"0.01\">" +
            "       </label></span>" +
            "   </li>"
}
