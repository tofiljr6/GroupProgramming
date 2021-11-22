let typesCount = 1
let dishesCount = 0

$(document).ready(function(){
    $("#numberOfTypes").val(typesCount);
    $("#addType").click(function() {
        let c = typesCount;
        typesCount++;
        $("#numberOfTypes").val(typesCount);
        $("#menu").append(" <li id=\"typeToAdd" + c + "\">" +
            "                   <ul class=\"list-inline\">" +
            "                       <li><label for=\"addedNewTypeName" + c + "\">" +
            "                           <input id=\"addedNewTypeName" + c + "\" name=\"addedNewTypeName" + c + "\" type=\"text\">" +
            "                       </label></li>" +
            "                       <li><button type=\"button\" id=\"dontAdd" + c + "\">Remove</button></li>" +
            "                       <li><button type=\"button\" id=\"addDishToNew" + c + "\" id=\"addDishToNew" + c + "\">Add new dish</button></li>" +
            "                   </ul>" +
            "                   <ul id=\"addedTypeDishes" + c + "\">" +
            "                   </ul>" +
            "               </li>");

        $(document).on("click", "#dontAdd" + c, function() {
            $("#typeToAdd" + c).remove();
            typesCount--;
            $("#numberOfTypes").val(typesCount);
        });

        $(document).on("click", "#addDishToNew" + c, function() {
            $("#addedTypeDishes" + c).append("<li class=\"list-group-item\">" +
                "                                   <a>" +
                "                                       <label for=\"newDishName\">" +
                "                                       <input id=\"newDishName\" name=\"newDishName\" type=\"text\">" +
                "                                       </label>" +
                "                                       <button type=\"button\" id=\"removeDish\" name=\"removeDish\">Remove</button>" +
                "                                   </a>" +
                "                                   <span class=\"badge\"><label for=\"newDishPrice\">" +
                "                                       <input id=\"newDishPrice\" name=\"newDishPrice\" type=\"number\" step=\"0.01\">" +
                "                                   </label></span>" +
                "                               </li>");
        });
    });
    for (let i = 1; i < $("#menu").children().length + 1; i++) {
        typesCount++;
        $("#numberOfTypes").val(typesCount);
        $("#addDish" + i).click(function() {
            $("#dishes" + i).append("   <li class=\"list-group-item\">" +
                "                           <a>" +
                "                               <label for=\"newDishName\">" +
                "                               <input id=\"newDishName\" type=\"text\">" +
                "                               </label>" +
                "                               <button type=\"button\" id=\"removeDish\">Remove</button>" +
                "                           </a>" +
                "                           <span class=\"badge\"><label for=\"newDishPrice\">" +
                "                               <input id=\"newDishPrice\" type=\"number\" step=\"0.01\">" +
                "                           </label></span>" +
                "                       </li>");
        });
        $("#removeType" + i).click(function() {

        });
    }
});