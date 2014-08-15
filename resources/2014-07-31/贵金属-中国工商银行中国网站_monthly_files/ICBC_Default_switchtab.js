function GetObj(objName) {
    if (document.getElementById) {
        return eval('document.getElementById("' + objName + '")');
    } else if (document.layers) {
        return eval("document.layers['" + objName + "']");
    } else {
        return eval('document.all.' + objName);
    }
}
function ICBC_Default_SwitchTabMenu(index, flag, TotalNum) {
    for (var i = 1; i <= TotalNum; i++) {

        var contentDivId = "AD" + flag + "con" + i;
        var MenuTDId = "AD" + flag + "m" + i;

        if (GetObj(contentDivId) && GetObj(MenuTDId)) {
            if (i == index) {
                GetObj(contentDivId).style.display = 'block';
                GetObj(MenuTDId).className = "AD20MenuOn";
            }
            else {
                GetObj(contentDivId).style.display = 'none';
                GetObj(MenuTDId).className = "AD20MenuOff";
            }
        }
    }
}
function ICBC_Default_SwitchTabMenuStyle(index, flag, TotalNum) {
    for (var i = 1; i <= TotalNum; i++) {
        var MenuTDId = "AD" + flag + "m" + i;
        if (GetObj(MenuTDId)) {
            if (i == index) {
                GetObj(MenuTDId).className = "AD20MenuOn";
            }
            else {
                GetObj(MenuTDId).className = "AD20MenuOff";
            }
        }
    }
}