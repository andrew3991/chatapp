
<template>
  <div class="messaging">
  <div class="inbox_msg">
	<div class="inbox_people">

		<header style="height: 49px;background:#d6ecff; ">
		<div class="dropdown dropdown_menu">
  		<button class="btn bmd-btn-icon dropdown-toggle" type="button" id="ex1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    		<i class="material-icons">more_vert</i>
  		</button>
  		<div class="dropdown-menu dropdown-menu-left" aria-labelledby="ex1">
    		<button class="dropdown-item" type="button"  @click="getAllUsers(this)">Create chat</button>
    		<!-- <button class="dropdown-item" type="button">Another action</button> -->
  	    </div>
	  </div>
		<div>
      <my-model :users="users_list" v-show="showAddChatModal" @messageFromChild="createGroupChat" @close="showAddChatModal=false" @create="createGroupChat"></my-model>
      </div>
		</header>

	  <div>
	    <section>
			<b-field>
				<b-input placeholder="Search..."
					type="search"
					icon="magnify"
					v-model="search">
				</b-input>
			
			</b-field>
			
		</section>
	  </div>
	  <div  class="inbox_chat scroll" >
		<div v-for="chat in filteredList" :key="chat.id"
		v-bind:class="{active_chat_click:chat[0] == selected}" @click="selected = chat[0]">
		<div  v-if="chat[3]=='0' && username != chat[4]" class="chat_list active_chat">
		  <div class="chat_people">
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat[0])" style="cursor: pointer;">
				<div>
					<div class="chat_title"><h5><span >{{chat[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat[6]!=''"><h5><span >{{chat[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p style="font-size: 13px;font-weight: 600;color: black;">{{ chat[2] }}</p>
					<span v-if="chat[5]>0 && username != chat[4]" class="badge badge-primary">{{chat[5]}}</span>
				</div>
				
			</div>
		  </div>
		</div>
		<div  v-else-if="chat[3]=='0' && username === chat[4]" class="chat_list active_chat">
		  <div class="chat_people">
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat[0])" style="cursor: pointer;">
			    <div>
					<div class="chat_title"><h5><span >{{chat[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat[6]!=''""><h5><span >{{chat[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p>{{ chat[2] }}</p>
					<span v-if="chat[5]>0 && username != chat[4]" class="badge badge-primary">{{chat[5]}}</span>
				</div>
			</div>
		  </div>
		</div>
		<div v-else class="chat_list active_chat">
		  <div  class="chat_people">
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat[0])" style="cursor: pointer;">
			    <div>
					<div class="chat_title"><h5><span >{{chat[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat[6]!=''""><h5><span >{{chat[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p>{{ chat[2] }}</p>
					<span v-if="chat[5]>0 && username != chat[4]" class="badge badge-primary">{{chat[5]}}</span>
				</div>
			</div>
		  </div>
		</div>
		</div>

		<div  v-for="chat_guest in filteredList_guest " :key="chat_guest.id" v-bind:class="{active_chat_click:chat_guest[0] == selected}" @click="selected = chat_guest[0]">
		<div  v-if="chat_guest[3]=='0' && username != chat_guest[4]" class="chat_list active_chat">
		  <div class="chat_people">
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat_guest[0])" style="cursor: pointer;">
			  <div>
					<div class="chat_title"><h5><span >{{chat_guest[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat_guest[6]!=''"><h5><span >{{chat_guest[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p style="font-size: 13px;font-weight: 600;color: black;">{{ chat_guest[2] }}</p>
					<span v-if="chat_guest[5]>0 && username != chat_guest[4]" class="badge badge-primary">{{chat_guest[5]}}</span>
				</div>
			</div>
		  </div>
		</div>
		<div v-else-if="chat_guest[3]=='0' && username === chat_guest[4]" class="chat_list active_chat">
		  <div  class="chat_people " >
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat_guest[0])" style="cursor: pointer;">
				<div>
					<div class="chat_title"><h5><span >{{chat_guest[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat_guest[6]!=''"><h5><span >{{chat_guest[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p>{{ chat_guest[2] }}</p>
					<span v-if="chat_guest[5]>0 && username != chat_guest[4]" class="badge badge-primary">{{chat_guest[5]}}</span>
				</div>
			</div>
		  </div>
		</div>
		<div  v-else class="chat_list active_chat">
		  <div   class="chat_people " >
			<div class="chat_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
			<div class="chat_ib" @click="changeChatGroup(chat_guest[0])" style="cursor: pointer;">
			  <div>
					<div class="chat_title"><h5><span >{{chat_guest[1]}}</span></h5></div>
				    <div class="chat_date" v-if="chat_guest[6]!=''"><h5><span >{{chat_guest[6]}}</span></h5></div>
				</div>
			    
			    <div class="chat_message">
					<p>{{ chat_guest[2] }}</p>
					<span v-if="chat_guest[5]>0 && username != chat_guest[4]" class="badge badge-primary">{{chat_guest[5]}}</span>
				</div>
			</div>
		  </div>
		</div>
		</div>

	  </div>

	
	  
	</div>
	<div class="mesgs">
	  <header class="header_bar" style="height: 50px;">
		  <div  class="chat_img_header"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"></div>
		  <div style="margin: 12px;"><span>{{username_title}}</span></div>
		  
	  </header>
	  <div id="containera" class="msg_history">
	  <div   v-for="message in messages" :key="message.id" >
		<template v-if="username === message.user.username">
		<div class="outgoing_msg">
		  <div class="sent_msg">
			<p>{{ message.message }}</p>
			<span class="time_date">{{message.create_date}} </span> </div>
		</div>
		</template>
		
		<template v-else>
		<div class="incoming_msg">
		  
		  <div class="received_msg">
			<div class="received_withd_msg">
			  <span class="time_date">{{message.user.username}}</span>
			  <p>{{ message.message }}</p>
			  <span class="time_date">{{message.create_date}}</span></div>
		  </div>
		</div>
		</template>
		</div>
	  </div>
	  
    
	  <div class="type_msg">
		<div class="input_msg_write">
			<form @submit.prevent="postMessage">
				<div class="form-group">
					<textarea v-model="message" class="form-control" id="exampleTextarea" rows="1"></textarea>
				</div>
				<button  class="msg_send_btn"><i class="fa fa-paper-plane" aria-hidden="true"></i></button>	
			</form>
		</div>
	  </div>

	</div>
	

	
  </div>

</div>

</template>

<script>
const $ = window.jQuery

export default {
  data () {
    return {
      messages: [],
	  message: '',
      chat_sessions: [],
      chat_titles: [],
      chats: [],
      chats_guest: [],
	  showAddChatModal: false,
	  users_list: [],
	  users_list_selected: [],
	  chat_group_title: '',
	  users: [],
	//   For header of messages
	  username_title : '',
	  selected: undefined,
	  search: ''
	  
    }
  },
  computed : {
            filteredList: function () {
                var sear = this.search;
                return this.chats.filter(function (elem) {
                 
                    if(sear==='') return true;
                    else return elem[1].indexOf(sear) > -1;
                })
			},
			filteredList_guest: function () {
                var sear = this.search;
                return this.chats_guest.filter(function (elem) {
                 
                    if(sear==='') return true;
                    else return elem[1].indexOf(sear) > -1;
                })
			},
			
        },
  
  created () {
    this.username = sessionStorage.getItem('username')
    $.ajaxSetup({
        headers: {
        'Authorization': `Token ${sessionStorage.getItem('authToken')}`
        }
    })
    this.getChatGroup()
	
	setInterval(this.fetchChatSessionHistory, 3000)
	setInterval(this.getChatGroup, 3000)

	
    },

	
    methods: {
    getChatGroup () {
        $.get(`http://localhost:8000/api/chats/`, (data) => {
          this.chat_sessions = data.chat_sessions
          this.chat_titles = data.chat_titles
          this.chats = data.chats
		  this.chats_guest = data.chats_guest
		  
        })
        .fail((response) => {
            alert(response.responseText)
        })
        },
    changeChatGroup (group) {
        $.get(`http://127.0.0.1:8000/api/chats/${group}/messages/`, (data) => {
		  this.messages = data.messages
		  this.username_title = data.username_title
		  this.$router.push(`/chats/${group}/`)
		  setTimeout(this.scrollToEnd, 1000)
		  this.readMessage(group)
      })
          
		},
    postMessage (event){
        const data = {message: this.message}

        $.post(`http://localhost:8000/api/chats/${this.$route.params.uri}/messages/`, data, (data) => {
            this.messages.push(data)
			this.message = '' // clear the message after sending
			setTimeout(this.scrollToEnd, 1000)

		})
        .fail((response) => {
            alert(response.responseText)
        })
    },
    joinChatSession () {
      const uri = this.$route.params.uri

      $.ajax({
        url: `http://localhost:8000/api/chats/${uri}/`,
        data: {username: this.username},
        type: 'PATCH',
        success: (data) => {
          const user = data.members.find((member) => member.username === this.username)

          if (user) {
            // The user belongs/has joined the session
			this.fetchChatSessionHistory()
			this.getChatGroup()
          }
        }
      })
    },
    fetchChatSessionHistory () {
      $.get(`http://127.0.0.1:8000/api/chats/${this.$route.params.uri}/messages/`, (data) => {
        this.messages = data.messages
		
      })
	},
	getAllUsers () {
      $.get(`http://127.0.0.1:8000/api/chats/chat/create/`, (data) => {
		this.showAddChatModal=true
        this.users_list = data.users_list
		
      })
	},
	createGroupChat (arg1, arg2) {
		
		for(var i=0; i<arg1.length; i++){
			this.users.push(arg1[i])
		}
	  const data = {users_list_selected: JSON.stringify(this.users), chat_group_title: arg2}

      $.post(`http://127.0.0.1:8000/api/chats/chat/create/`, data, (data) => {
		this.showAddChatModal = false
		this.chat_group_title = ''
		this.users_list_selected = []
		
      })
	},
	scrollToEnd() {    	
      var containera = $( "#containera" )
      containera[0].scrollTop = containera[0].scrollHeight
	},
	readMessage (group) {

      $.ajax({
        url: `http://localhost:8000/api/chats/chat/create/`,
        data: {chat_uri: group},
        type: 'PATCH',
        success: (data) => {
			this.getChatGroup()
        }
      })
	}
}
}
</script>



<style scoped>
#app{
	margin: 0 0 0 0;
}
.container{
    max-width:900px;
}
.inbox_people {
	background: #fff;
	float: left;
	overflow: hidden;
	width: 25%;
	border-right: 1px solid #ddd;
	display: flex;
    flex-direction: column;
}

.inbox_msg {
	border: 1px solid #ddd;
	clear: both;
	overflow: hidden;
	height: 733px;
}
.dropdown_menu{
	float: left;
	margin: 5px 0 0 5px;
}

.top_spac {
	margin: 20px 0 0;
}

.recent_heading {
	float: left;
	width: 40%;
}

.srch_bar {
	display: inline-block;
	text-align: right;
	/* width: 60%; */
	padding:
}

.headind_srch {
	padding: 10px 29px 10px 20px;
	overflow: hidden;
	border-bottom: 1px solid #c4c4c4;
}
.header_bar{
	display: flex;
    background: #d6ecff;
}
.recent_heading h4 {
	color: #0465ac;
    font-size: 16px;
    margin: auto;
    line-height: 29px;
}

.srch_bar input {
	outline: none;
	border: 1px solid #cdcdcd;
	border-width: 0 0 1px 0;
	/* width: 80%; */
	padding: 2px 0 4px 6px;
	background: none;
}

.srch_bar .input-group-addon button {
	background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
	border: medium none;
	padding: 0;
	color: #707070;
	font-size: 18px;
}

.srch_bar .input-group-addon {
	margin: 0 0 0 -27px;
}

.chat_ib h5 {
	/* font-size: 15px; */
	color: #464646;
	/* margin: 0 0 8px 0; */
}



.chat_ib p {
    font-size: 12px;
    color: #989898;
    margin: auto;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.chat_img {
	float: left;
	width: 12%;
	padding: 2px;
}

.chat_img_header{
	float: left;
	width: 5%;
	padding: 2px;
	width: 48px;
	height: 48px;
	margin-left: 25px;
}

.chat_img img {
	width: 100%
}

.chat_ib {
	float: left;
	padding: 0 0 0 15px;
	width: 88%;
	display: flex;
	flex-direction: column;
    flex-wrap: wrap;
}

.chat_people {
	overflow: hidden;
	clear: both;
}

.chat_list {
	border-bottom: 1px solid #ddd;
	margin: 0;
	padding: 18px 16px 10px;
}
.chat_title{
	float: left;
}
.chat_date{
	float: right;
}
.chat_date h5 span{
	font-size: 12px;
}

.chat_message{
	text-align: left;
}
.chat_title h5 span{
	text-align: left;
	font-size: 16px;
}
.inbox_chat {
	height: 660px;
	overflow-y: scroll;
}

.active_chat:hover {
	background: #f0f8ff;
}

.active_chat_click{
	background: #d6ecff;
}
.incoming_msg_img {
	/* display: inline-block; */
	width: 6%;
}

.incoming_msg_img img {
	width: 100%;
}

.received_msg {
	/* display: inline-block; */
	padding: 25px 0 0 80px;
	vertical-align: top;
	width: 80%;
}

.received_withd_msg p {
	background: #ebebeb none repeat scroll 0 0;
	border-radius: 0 15px 15px 15px;
	color: #646464;
	font-size: 14px;
	margin: 0;
	padding: 5px 10px 5px 12px;
	width: 100%;
	text-align: left;
}

.time_date {
	color: #747474;
	display: block;
	font-size: 12px;
	margin: 8px 0 0;
	text-align: left;
}

.received_withd_msg {
	width: 40%;
}

.mesgs{
	float: left;
	
	width:75%;
}

.sent_msg p {
	background:#0465ac;
	border-radius: 12px 15px 15px 0;
	font-size: 14px;
	margin: 0;
	color: #fff;
	padding: 5px 10px 5px 12px;
	width: 100%;
}

.outgoing_msg {
	overflow: hidden;
	margin: 26px 0 26px;
}

.sent_msg {
	float: right;
	width: 32%;
	text-align: left;
	padding-right: 60px;
}

.input_msg_write input {
	background: rgba(0, 0, 0, 0) none repeat scroll 0 0;
	border: medium none;
	color: #4c4c4c;
	font-size: 15px;
	min-height: 48px;
	width: 100%;
	outline:none;
}

.input_msg_write {
	margin-left: 40px;
	margin-top: 8px;
	margin-bottom: -10px;
	margin-right: 70px;
}

.type_msg {
	border-top: 1px solid #c4c4c4;
	position: relative;
	/* padding-bottom: 25px; */
    background: #d6ecff;
	border-bottom: 1px solid #c4c4c4;
}

.msg_send_btn {
	background: #05728f none repeat scroll 0 0;
	border:none;
	border-radius: 50%;
	color: #fff;
	cursor: pointer;
	font-size: 15px;
	height: 34px;
	position: absolute;
	right: 17px;
	top: 8px;
	width: 34px;
}

.messaging {
	padding: 0 0 0 0;
	margin: 0 25px 25px 25px;
}

.msg_history {
	height: 630px;
	overflow-y: auto;
	padding: 0 20px 0 5px;
}

.form-control{
	display: block;
    width: 100%;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border-top: 1px solid #ced4da;
    border-radius: 2.25rem;
    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    border-left: 1px solid #ced4da;
	border-bottom: none;
}


</style>