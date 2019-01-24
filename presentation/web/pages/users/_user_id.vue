<template>
  <div>
    <div>
      <a href="#" class="button is-large">NAILS ONLINE</a>
    </div>


    <div class="column">
      <div class="is-pulled-right">
        <div align="center">
          <p>ヘルプ</p>
        </div>
      </div>
    </div>

    <div class="hero is-light is-bold">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">マイアカウント</h1>
        </div>
      </div>
    </div>

    <div>
      <p>&nbsp;&nbsp;詳細</p>
    </div>


  <div class="columns is-center">
    <div class="column is-half">
      <table class="table is-fullwidth">
        <tbody>
          <th>名前</th>
          <input v-if="isEdit" class="input" type="text" v-model="user.name" required>
          <td v-else>{{ user.name }}</td>
        </tbody>
        <tbody>
          <th>Eメールアドレス</th>
          <input v-if="isEdit" class="input" type="text" v-model="user.email" required>
          <td v-else>{{ user.email }}</td>
        </tbody>
        <tbody>
          <th>電話番号</th>
          <input v-if="isEdit" class="input" type="text" v-model="phoneNumber" required>
          <td v-else>09012345</td>
        </tbody>
        <tbody>
          <th>パスワード</th>
          <input v-if="isEdit" class="input" type="text" v-model="password" required>
          <td v-else>010101</td>
        </tbody>
      </table>
    </div>
  </div>

  <div class="field is-grouped">
    <button v-if="isEdit" class="control button" @click="update">
      更新する
    </button>
    <button class="control button" @click="edit" v-else>
      内容を編集する
    </button>
  </div>

    <div align="center">
    　   トップページへ戻る
    </div>


  </div>
</template>


<script>
export default {
  data() {
    return {
      isEdit: false,
      phoneNumber: "12345",
      password: "",
    }
  },
  async asyncData({app, params, error}) {
    try {
      let userId = parseInt(params.user_id)
      const { data } = await app.$axios.get(`/api/users/${userId}`)
      return {
        userId: userId,
        user: data.user,
      }
    } catch (err) {
      return {
        user: 0,
        statusCode: err.response.status,
        message: err.response.statusText,
      }
    }
  },
  computed: {
    name: function() {
      return this.user.name
    }
  },
  methods: {
    edit() {
      this.isEdit = true
    },
    update() {
      console.log(111111111)
      this.$axios.put(`/api/users/${this.userId}`, {
         name: this.user.name,
         email: this.user.email,
    })
      this.isEdit = false
    },
  }
}
</script>

<style lang="scss" scoped>
  p {
    color :blue
  }
</style>

