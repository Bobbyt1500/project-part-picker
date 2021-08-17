function getCellVal(tr, i) {return $(tr.cells[i].children).val()}
function getCellText(tr, i) {return $(tr.cells[i].children).text()}

function replaceCellElement(tr, i, element) {
    $(tr.cells[i].children).remove()
    $(tr.cells[i]).append(element)
}