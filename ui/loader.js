
var wrapper = null;
template = '<tr> <td id="item-lccn">{lccn_replace}</td> <td id="item-desc">{desc_replace}</td></tr>'

function load_data(document) {

	if(wrapper == null){
		wrapper = $('#list-body');
	}

	var mydata = JSON.parse(lcco);

	console.log(mydata)
    console.log(template)
    template = template.replace("{lccn_replace}", 'AB10-20');
    template = template.replace("{desc_replace}",'Donkeys');
    wrapper.append(template);
}