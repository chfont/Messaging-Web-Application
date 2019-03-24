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

/*Not working*/
function submitCanvas()
{
  var rawData = cntxt.getImageData(0,0,canvas.width, canvas.height);
  var dec = "";
  var count = 0;
  var hexString = "";
  for(var i = 3; i < rawData.data.length; i+=4)
  {
    if(rawData.data[i] != 0)
    {dec+= "1";}
    else{dec+="0";}
    if(count % 3 == 0 && count != 0)
    {
      count = 0;
      dec = parseInt(dec,2);
      dec = dec.toString(16);
      hexString += dec;
    }
    count++;
  }
  return hexString;
}
