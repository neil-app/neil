
<template>

  <div>
    <div class="title">
        <link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
        Nails online contact
    </div>

    <div class="base">
      <link href="https://fonts.google.com/specimen/Amatic+SC" rel="stylesheet">
      <div>
          <label for="name">Name:</label>
          <input type="text" id="name" name="user_name" v-model="name">
      </div>

      <div>
          <label for="mail">E-mail:</label>
          <input type="text" id="mail" name="user_mail" v-model="email">
      </div>

      <div>
          <label for="telephone">Telephone:</label>
          <input type="text" id="telephone" name="user_phone" v-model="phone">
      </div>

      <div>
          <label for="msg">Message:</label>
          <textarea id="msg" name="user_message" v-model="msg"></textarea>
      </div>

      <div class="msg">
          <button @click="submit">Send your message</button>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      phone: "",
      msg: "",
    }
  },
  head() {
    return {
      title: "contact",
    }
  },
  methods: {
    async submit() {
      try {
        await this.$axios.post(`/api/contact`, {
          name: this.name,
          email: this.email,
          phone: this.phone,
          msg: this.msg,
        })
      } catch (error) {
        let message = "エラーが発生しました。しばらくたってからお試しください"
        if (error.response.data.message) {
            message = error.response.data.message
        }
        this.$toast.open({
          message: message,
          type: "is-danger",
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.title{
  font-family: "Indie Flower", cursive;
  text-align: center;
  margin-top: 2rem;
  font-weight: 15;
  font-size:25px;
}
.base{
  margin: 0 auto;
  width: 500px;
  padding: 2em;
  border: 1px solid;
  border-radius: 2em;
}
.base div + div {
  margin-top: 1em;
}
label {
  display: inline-block;
  width: 90px;
  text-align: right;
  font-family: "Amatic SC", cursive;
}
input, textarea {
  font: 1em sans-serif;
  width: 300px;
  box-sizing: border-box;
  border: 1px solid #999;
}
input:focus, textarea:focus {
  border-color: #000;
}
textarea {
  vertical-align: top;
  height: 5em;
}
.msg {
  padding-left: 20px;
}
.msg {
  margin-left: .5em;
}
.msg{
    text-align: center;
}
</style>