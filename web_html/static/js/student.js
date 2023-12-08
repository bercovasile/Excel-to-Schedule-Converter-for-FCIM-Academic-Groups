function updateSecondComboBox() {
  const selectOptions = document.getElementById("selectOptions");
  const selectedOption = selectOptions.value;

  const selectOptionsGrups = document.getElementById("selectOptionsGrups");

  fetch("/get_options_grups", {
    method: "POST", 
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ selectedOption }),
  })
    .then(response => response.json())
    .then(data => {
      selectOptionsGrups.innerHTML = "";
      data.options.forEach(option => {
        const optionElement = document.createElement("option");
        optionElement.textContent = option;
        optionElement.value = option;
        selectOptionsGrups.appendChild(optionElement);
      });
    })
    .catch(error => {
      console.error("Error updating second combobox:", error);
    });
}

function sendSelectedOptionGrups(test) {
  const selectOptionsGrups = document.getElementById("selectOptionsGrups");
  const selectedOptionGrups = selectOptionsGrups.value;
  fetch("/handle_selected_option_grups", {
    method: "POST", 
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ selectedOptionGrups }),
  })
    .then(response => response.blob())
    .then(blob => {

      if (test)
        excel_to_html_table_pc(blob);
      else
        excel_to_html_table_mobile(blob);

    })
    .catch(error => {
      console.error("Error sending selected option:", error);
    });
}


function excel_to_html_table_pc(excel_blob) {
  var reader = new FileReader();
  reader.onload = function (event) {
    var data = new Uint8Array(event.target.result);
    var workbook = XLSX.read(data, { type: "array" });
    var sheet_name = workbook.SheetNames[0];
    var sheet_data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name], { header: 1 });


    if (sheet_data.length > 0) {
      var table_output = '<table class="listViewTable table-sortable" id="listViewTable" >';
      for (var row = 0; row < sheet_data.length; row = row + 2) {
        var merge_data = '';
        table_output += '<tr class="ce1 colorYellow">';

        for (var cell = 0; cell < sheet_data[row].length; cell++) {
          // Verificăm dacă valoarea este undefined și o înlocuim cu un spațiu gol
          var cellValue = sheet_data[row][cell] === undefined ? " " : sheet_data[row][cell];

          if (row == 0) {
            table_output += '<th class="name1 hsText "><div class="table_first_row">' + cellValue + '</div></th>';
          } else {

            if (sheet_data[row + 1][cell] !== undefined) {

              var undefinedCellValue = cellValue === '#' ? "📖" : cellValue;
              table_output += '<td class="entry1 hsText"><div class="table_cell_content_merge_1"> ' + undefinedCellValue + '</div></td>';

              var mergeCell = sheet_data[row + 1][cell] === '#' ? "📖" : sheet_data[row + 1][cell];
              merge_data += '<td class="entry1 hsText"><div class="table_cell_content_merge_2">' + mergeCell + '</div></td>';

            } else {
              if ((cell == 0) && (row != 0)) {
                var undefinedCellValue = cellValue === '#' ? "📖  <font siz</font>" : cellValue;
                table_output += '<td class="entry1 hsText" rowspan="2"><div class="table_first_column">' + undefinedCellValue + '</div></td>';
              }
              else {
                var undefinedCellValue = cellValue === '#' ? "📖" : cellValue;
                table_output += '<td class="entry1 hsText" rowspan="2"><div class="table_cell_content">' + undefinedCellValue + '</div></td>';
              }
            }
          }
        }
        table_output += '</tr>';
        if (merge_data === '')
          table_output += '<tr></tr>';
        else
          table_output += '<tr>' + merge_data + '</tr>';
      }
      table_output += '</table>';
      document.getElementById('excel_data').innerHTML = table_output;
    }
  };

  reader.readAsArrayBuffer(excel_blob);
}


function excel_to_html_table_mobile(excel_blob) {
  var reader = new FileReader();
  reader.onload = function (event) {
    var data = new Uint8Array(event.target.result);
    var workbook = XLSX.read(data, { type: "array" });
    var sheet_name = workbook.SheetNames[0];
    var sheet_data = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name], { header: 1 });

    if (sheet_data.length > 0) {
      var table_output = '<table class="listViewTable table-sortable" id="listViewTable">';
      for (var coll = 1; coll < sheet_data.length; coll++)
        for (var row = 0; row < sheet_data.length; row = row + 2) {
          var cellValue = sheet_data[row][coll];
          var undefinedCellValue = cellValue === '#' ? "📖" : cellValue;

          if (sheet_data[row][coll] !== undefined)
            if (sheet_data[row + 1][coll] !== undefined) {

              table_output += '<tr class="ce1 colorYellow"> <td class="entry1 hsText"><div class="table_cell_content_merge_1">' + undefinedCellValue + '</div></td> </tr>';

              var cellValue = sheet_data[row + 1][coll];
              var undefinedCellValue = cellValue === '#' ? "📖" : cellValue;
              table_output += '<tr class="ce1 colorYellow"> <td class="entry1 hsText"><div class="table_cell_content_merge_2">' + undefinedCellValue + '</div></td> </tr>';
            }
            else
              if (row == 0)
                table_output += '<tr class="ce1 colorYellow"> <td class="entry1 hsText"><div class="table_first_row">' + undefinedCellValue + '</div></td> </tr>';
              else
                table_output += '<tr class="ce1 colorYellow"> <td class="entry1 hsText"><div class="table_cell_content">' + undefinedCellValue + '</div></td> </tr>';
        }


      table_output += '</table>';
      document.getElementById('excel_data').innerHTML = table_output;
    }
  };
  reader.readAsArrayBuffer(excel_blob);
}

function checkScreenWidth() {
  const width = window.innerWidth;

  if (width > 600) {
    sendSelectedOptionGrups(1);
  } else {
    sendSelectedOptionGrups(0);
  }
}

// Apelăm funcția inițial pentru a seta valoarea corectă la încărcarea paginii
checkScreenWidth();

// Adăugăm un ascultător pentru evenimentul resize al ferestrei pentru a verifica și apela funcția corespunzătoare
window.addEventListener('resize', checkScreenWidth);




