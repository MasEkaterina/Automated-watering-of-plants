$(document).ready(function() {
$(".polivBtn").on("click", function() {
$(this).addClass('disabled');
$(this).text("Polivaetsa...");
const id = $(this).data('id');
console.log(id);
poliv(id, (data) => {
console.log('response', data);
$(this).removeClass('disabled');
$(this).text("Poliv");
$(".plant-history[data-id='" + id + "']").each(updateHistory);
});
});

$(".plant-history").each(updateHistory);
});

function updateHistory() {
const id = $(this).data('id');
getHistory(id, (data) => {
$(this).html(data.replace(/^(\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2})(.*?)$/mg, '<b>$1</b>$2'));
});
}

function poliv(id, callback) {
$.post("poliv/" + id, function(data) {
callback(data);
});
}

function getHistory(id, callback) {
$.post("history/" + id, function(data) {
callback(data);
});
}
