setTimeout(function() {
    const callInterface = document.getElementById("tab_callInterface");
    const callInterface_div = document.createElement("div");
    callInterface_div.style = "witdth: 100%;height:100%";
    callInterface_div.innerHTML = '<iframe id="callInterfaceIframe" name="Frame" src="/callInterface/easy_ui.html" style="width: 100%; height: 100%;"></iframe>';
    callInterface.appendChild(callInterface_div);
},1000*25);
