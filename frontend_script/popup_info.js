// 创建一个 div 元素
var div = document.createElement("div");
div.textContent = "Hello World";

// 设置 div 元素的样式
div.style.position = "fixed";
div.style.bottom = "20px";
div.style.right = "20px";
div.style.padding = "10px";
div.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
div.style.color = "#fff";
div.style.zIndex = "9999";
div.style.opacity = "0"; // 初始时设置透明度为0

// 将 div 元素添加到页面的 body 中
document.body.appendChild(div);

// 通过 setTimeout 函数在下一次事件循环中触发渐变显示效果
setTimeout(function() {
  div.style.transition = "opacity 1s"; // 添加渐变效果
  div.style.opacity = "1"; // 将透明度设置为1，触发渐变显示
}, 0);

// 通过 setTimeout 函数在六秒钟后触发渐变消失效果
setTimeout(function() {
  div.style.opacity = "0"; // 将透明度设置为0，触发渐变消失
}, 6000);

// 七秒钟后移除 div 元素
setTimeout(function() {
  document.body.removeChild(div);
}, 7000);
