function doPost(e) { 
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[0];
  var Unique_id = e.parameter.Unique_id ; 
  var url = e.parameter.url ; 
  sheet.appendRow([Unique_id,url]);
  return "done"
}
