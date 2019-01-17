<template>
  <section class="section">
    <div class="container is-centered">
      <div class="card">
        <div class="card-content">
          <div class="content">
            <form @submit.prevent="submit">
              <div class="field">
                <div class="label">名前</div>
                <div class="control">
                  <input class="input" type="text" placeholder="名前を入力" v-model="name" required>
                </div>
              </div>
              <div class="field">
                <div class="label">メールアドレス</div>
                <div class="control">
                  <input class="input is-medium" type="email" placeholder="メールアドレス" v-model="email" required>
                </div>
              </div>
              <div class="field">
                <div class="label">パスワード</div>
                <div class="control has-icons-right">
                  <input class="input" :type="showPassword ? 'text' : 'password'" placeholder="パスワード" v-model="password" required>
                  <span class="icon is-small is-right toggle-password" :class="{'is-show': showPassword}" @click="togglePassword">
                    <b-icon icon="eye" size="is-small"></b-icon>
                  </span>
                </div>
              </div>
              <div class="field is-grouped is-grouped-right field-submit">
                <div class="control">
                  <button class="button is-primary" type="submit">
                    登録
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      showPassword: false,
    }
  },
  async asyncData({ app, error }) {},
  head() {
    return {
      title: "会社登録",
    }
  },
  methods: {
    togglePassword: function() {
      this.showPassword = !this.showPassword
    },
    async submit() {
      try {
        await this.$axios.post(`/api/users`, {
          name: this.name,
          email: this.email,
          password: this.password,
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
.section {
  padding-top: 1.5rem;
}

.card {
  margin-left: auto;
  margin-right: auto;
  max-width: 400px;
}

.card-image {
  padding: 3rem 3rem 1.5rem;
}

.select {
  width: 100%;
  select {
    width: 100%;
  }
}
</style>
