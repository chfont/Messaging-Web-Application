var canvas, cntxt, flag = false,
prevX = 0,
prevY = 0,
currX = 0,
currY = 0;

function init()
{
  canvas = document.getElementById('canvas');
  cntxt = canvas.getContext("2d");
  cntxt.scale(2,2);
  h = canvas.height;
  w = canvas.width;

  canvas.addEventListener("mouseup",function(e){renderUpdate('up',e)},false);
  canvas.addEventListener("mousemove",function(e){renderUpdate('move',e)},false);
  canvas.addEventListener("mousedown",function(e){renderUpdate('down',e)},false);
}
function renderUpdate(cmd, e)
{

  if (cmd == 'down')
  {
    flag = true;
    prevX = currX;
    prevY = currY;
    currX = e.clientX - canvas.offsetLeft + window.scrollX;
    currY = e.clientY - canvas.offsetTop + window.scrollY;

    currX = currX / 2;
    currY = currY / 2;
      cntxt.beginPath();
      cntxt.fillStyle = "black";
      cntxt.fillRect(currX,currY,1,1);
      cntxt.closePath();
  }
  else if(cmd == 'up')
  {
    flag = false;
  }
  else if(cmd == 'move')
  {
    if(flag)
    {
      prevX = currX;
      prevY = currY;
      currX = e.clientX - canvas.offsetLeft + window.scrollX;
      currY = e.clientY - canvas.offsetTop + window.scrollY;
      currX = currX / 2;
      currY = currY / 2;
      cntxt.beginPath();
      cntxt.moveTo(currX,currY);
      cntxt.lineTo(prevX, prevY);
      cntxt.strokeStyle = "black";
      cntxt.lineWidth=1;
      cntxt.stroke();
      cntxt.closePath();

    }
  }
}

function clearCanv()
{
  cntxt.clearRect(0,0, canvas.width, canvas.height);
}

function b64(digit)
{
  var charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-";
  var s="";
  do
  {
    s+= charset[digit % 64];
    digit = Math.floor(digit/64);
  }while(digit !=0);
  if (s == "")
  {
    s = "0";
  }
  return s.split("").reverse().join("");

}

/*Not working*/
function submitCanvas()
{
  var rD = cntxt.getImageData(0,0, canvas.width, canvas.height);
  var binS = "";
  var hexS = "";
  var count = 0;
  var digit;
  for(var i = 3; i < rD.data.length; i+=4)
  {
    count += 1;
    var d = rD.data[i];
    if(d > 0)
    {
      binS += "1";
    }
    else
    {
      binS += "0";
    }

    if(count % 6 == 0)
    {
      digit = parseInt(binS, 2);
      hexS += b64(digit);
      binS = "";
    }
  }
  return hexS;
}
