function editRow() {

    let tableRow = $(this).parents("tr")[0]
    let button = $(tableRow.cells[0].children)

    console.log(getCellText(tableRow, 1))

    replaceCellElement(tableRow, 1, $(`<input class="w-100" value="${getCellText(tableRow, 1)}">`))
    replaceCellElement(tableRow, 2, $(`<input class="w-100" value="${getCellText(tableRow, 2)}">`))
    replaceCellElement(tableRow, 3, $(`<input class="w-100" type="number" min=0 value=${getCellText(tableRow, 3).substring(1)}>`))
    
    button.removeClass("editbtn").addClass("savebtn")
    button.children().removeClass("fa-edit").addClass("fa-check")
    button.off('click').on('click', saveRow)
}

function saveRow() {
    
    let tableRow = $(this).parents("tr")[0]
    let button = $(tableRow.cells[0].children)

    // Get inputted row data
    let data = {
        "name" : getCellVal(tableRow, 1),
        "link" : getCellVal(tableRow, 2),
        "price" : getCellVal(tableRow, 3)
    }

    // If no number was provided, default to 0
    if (data["price"] == "") data["price"] = 0

    replaceCellElement(tableRow, 1, $(`<p>${data["name"]}</p>`))
    replaceCellElement(tableRow, 2, $(`<a href=${data["link"]}>${data["link"]}</a>`))
    replaceCellElement(tableRow, 3, $(`<p>$${data["price"].toString()}</p>`))

    button.removeClass("savebtn").addClass("editbtn")
    button.children().removeClass("fa-check").addClass("fa-edit")
    button.off('click').on('click', editRow)

    // Send data to server
    $.ajax({
        type : "PUT",
        url : `${window.location.pathname}/part/${$(tableRow).data("id")}`,
        data : data,
        success : function() {window.location.reload()}
    })

}

function deleteRow() {
    let tableRow = $(this).parents("tr")[0]

    $.ajax({
        type: "DELETE",
        url : `${window.location.pathname}/part/${$(tableRow).data("id")}`,
        success: function() {window.location.reload()}
    })
}

$(document).ready(function() {
    $(".editbtn").on('click', editRow)
    $(".delbtn").on('click', deleteRow)
})