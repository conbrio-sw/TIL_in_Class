import router from "../routers.js"
export default {
  template:
  `
  <div class="container px=0 py=3">
  <div class="card">
<img src="./img/02.png" style="width:200px" class="card-img-top" alt="...">
<div class="card-body row">
<div class="col-6 col-md">
  <h5 class="card-title">보낼 메시지</h5>
  <input type="text" v-model="sendingMsg"/>
  <button @click="sendMsg" class="btn btn-primary">Send Msg</button>
  </div>
  <div class="col-6 col-md">
          <h5>받은 메시지</h5>
          <p>{{receivingMsg}} <button @click="checkMsg" class="btn btn-primary">Check Msg</button></p>
  </div>
</div>
</div>
  </div>
  `,
data() {
  return {
    from: this.$route.query.from,
    sendingMsg: "",
    receivingMsg:"받은 메시지가 없습니다.",
  }
},
methods: {
  sendMsg: function () {
    let data = {
      from: "핑크머리",
      receivingMsg:this.sendingMsg
    };
    router.push({
      name: "Half",
      query: data,
    });
  },
  checkMsg: function () {
    if (this.from != undefined) {
      this.receivingMsg = this.$route.query.receivingMsg;
      alert(this.from + " / " + this.receivingMsg);
    } else {
      alert("메일이 없습니다.")
    }
  }
},
}