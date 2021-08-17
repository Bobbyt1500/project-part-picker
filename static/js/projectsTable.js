function editRow() {
    let tableRow = $(this).parents("tr")[0]
    let button = $(tableRow.cells[0].children)

    replaceCellElement(tableRow, 1, $(`<input class="w-100" value="${getCellText(tableRow, 1)}">`))
    
    button.removeClass("editbtn").addClass("savebtn")
    button.children().removeClass("fa-edit").addClass("fa-check")
    button.off('click').on('click', saveRow)
}

function saveRow() {
  
    let tableRow = $(this).parents("tr")[0]
    let button = $(tableRow.cells[0].children)
    let updated_name = getCellVal(tableRow, 1)

    replaceCellElement(tableRow, 2, $(`<a href="/project/${$(tableRow).data("id")}">updated_name</a>`))

    button.removeClass("savebtn").addClass("editbtn")
    button.children().removeClass("fa-check").addClass("fa-edit")
    button.off('click').on('click', editRow)

    // Send data to server
    $.ajax({
        type : "PUT",
        url : `/project/${$(tableRow).data("id")}`,
        data : {"name" : updated_name},
        success : function() {window.location.reload()}
    })
}

function deleteRow() {
    let tableRow = $(this).parents("tr")[0]

    $.ajax({
        type: "DELETE",
        url : `/project/${$(tableRow).data("id")}`,
        success: function() {window.location.reload()}
    })
}

$(document).ready(function() {
    $(".editbtn").on('click', editRow)
    $(".delbtn").on('click', deleteRow)
})