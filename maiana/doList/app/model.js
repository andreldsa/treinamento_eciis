function User(data){
    this.email = data.email || "";
    this.lists = data.lists || [];
    this.lists_name = data.lists_name || [];
}

User.prototype.addList = function(list) {
	console.log(list)
    this.lists.push(list.id);
    this.lists_name.push(list.name);
}

User.prototype.removeList = function(idList) {
    _.remove(this.lists, function(list) {
        return list == idList;
   });
}