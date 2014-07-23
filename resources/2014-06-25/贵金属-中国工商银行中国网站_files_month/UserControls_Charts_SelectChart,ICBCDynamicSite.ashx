if(typeof UserControls_Charts_SelectChart == "undefined") UserControls_Charts_SelectChart={};
UserControls_Charts_SelectChart_class = function() {};
Object.extend(UserControls_Charts_SelectChart_class.prototype, Object.extend(new AjaxPro.AjaxClass(), {
	getBranchNameByAjax: function(DataType, DataId, PicType) {
		return this.invoke("getBranchNameByAjax", {"DataType":DataType, "DataId":DataId, "PicType":PicType}, this.getBranchNameByAjax.getArguments().slice(3));
	},
	url: '/ICBCDYNAMICSITE/ajaxpro/UserControls_Charts_SelectChart,ICBCDynamicSite.ashx'
}));
UserControls_Charts_SelectChart = new UserControls_Charts_SelectChart_class();

