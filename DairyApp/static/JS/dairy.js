//function validateId()
//{
//alert('ere');
//document.getElementById('abc').submit();
//}

function tamt1()
{
  var milkqty=document.getElementById('milkqty').value;
  var fat=document.getElementById('fat').value;
  var rate=document.getElementById('rate').value;
  var tamount = parseInt(milkqty)*parseInt(fat)*parseInt(rate);
  document.getElementById('totalamt').value=tamount;
}

function valdob()
{
	var day=document.getElementById('day').value;
	var month=document.getElementById('month').value;
	var year=document.getElementById('year').value;
	var m=parseInt(day)+parseInt(month)+parseInt(year);
	document.getElementById('dob').value= m;

}
