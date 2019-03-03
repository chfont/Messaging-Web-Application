class jsCanvas
{

constructor()
{
  flag = false;
  currX = null;
  currY = null;
  prevX = null;
  prevY = null;
  this.canvas = document.getElementById('canvas');
  this.contxt = canvas.getContext("2d");
  this.h = canvas.height;
  this.w = canvas.width;

  canvas.addEventListener("mouseup",function(e){renderUpdate('up',e)},false);
  canvas.addEventListener("mousemove",function(e){renderUpdate('move',e)},false);
  canvas.addEventListener("mousedown",function(e){renderUpdate('down',e)},false);
}


renderUpdate(cmd, e)
{
  if (cmd == 'down')
  {
    flag = true;
    if(currX == null)
    {
      currX = e.clientX - canvas.offsetLeft;
      currY = e.clientY - canvas.offsetTop;
    }
    else
    {
      prevX = currX;
      prevY = currY;
      currX = e.clientX - canvas.offsetLeft;
      currY = e.clientY - canvas.offsetTop;

      contxt.beginPath();
      contxt.fillStyle = "black";
      contxt.fillRect(currX,currY,1,1);
      contxt.closePath();
    }
  }
  else if(cmd == 'up')
  {
    flag = false;
    currX = null;
    currY = null;
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

}
