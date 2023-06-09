function popup_info(info_content) {
  // 创建一个 div 元素
  var div = document.createElement("div");
  div.innerText = info_content;

  // 设置 div 元素的样式
  div.style.position = "fixed";
  div.style.top = "0px";
  div.style.right = "20px";
  div.style.padding = "10px";
  div.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
  div.style.color = "#fff";
  div.style.zIndex = "9999";
  div.style.opacity = "0"; // 初始时设置透明度为0

  // 将 div 元素添加到页面的 body 中
  document.body.appendChild(div);

  // 通过 setTimeout 函数在下一次事件循环中触发渐变显示效果
  setTimeout(function () {
    div.style.transition = "opacity 1s"; // 添加渐变效果
    div.style.opacity = "1"; // 将透明度设置为1，触发渐变显示
  }, 0);

  // 通过 setTimeout 函数在六秒钟后触发渐变消失效果
  setTimeout(function () {
    div.style.opacity = "0"; // 将透明度设置为0，触发渐变消失
  }, 21000);

  // 七秒钟后移除 div 元素
  setTimeout(function () {
    document.body.removeChild(div);
  }, 22000);

}

function report_new_submit() {
  console.log("事件已捕获，开始发送请求...")
  fetch('https://chatgpt-4-counter-backend-production.up.railway.app//usage_audit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'action_type': 'report_new_submit'
    }),
  })
    .then(response => response.text())
    .then(data => {
      console.log(data);
      popup_info(data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

function inject_btn_func() {
  var button = document.querySelector('button.absolute');
  button.addEventListener('click', report_new_submit);
  console.log('add click listener success')
}

function inject_enter_func() {
  var textarea = document.querySelector('#prompt-textarea');
  textarea.addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
      report_new_submit();
    }
  });
  console.log('add enter listener success')
}

function inject_style_adjustment(){
    console.log("开始调整格式");
    const nodeList = document.querySelectorAll('div.group');
    for (let i = 1; i < nodeList.length; i++) {
      const element = nodeList[i];
      const first_div = element.firstElementChild;
      first_div.style.transition = "1s";
      first_div.style.maxWidth = '480rem';
    }
    document.querySelector("div.rounded-lg:nth-child(2)").style.maxHeight= "40rem";
}

setInterval(() => {
  inject_btn_func();
  inject_enter_func();
  inject_style_adjustment();
}, 2000);
