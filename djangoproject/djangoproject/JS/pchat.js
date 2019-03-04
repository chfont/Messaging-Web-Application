var canvas, cntxt, flag = false,
prevX = 0,
prevY = 0,
currX = 0,
currY = 0,
h,w;

function init()
{
  canvas = document.getElementById('canvas');
  cntxt = canvas.getContext("2d");
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
    currX = e.clientX - canvas.offsetLeft;
    currY = e.clientY - canvas.offsetTop;

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
      currX = e.clientX - canvas.offsetTop;
      currY = e.clientY - canvas.offsetLeft;
      cntxt.beginPath();
      cntxt.moveTo(prevX,prevY);
      cntxt.lineTo(currX, currY);
      cntxt.strokeStyle = "black";
      cntxt.lineWidth=1;
      cntxt.stroke();
      cntxt.closePath();

    }
  }
}
