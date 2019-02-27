<template>
  <div>
    <div class="top">
      <link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
      <nuxt-link :to="{path: `/`}">
        <p>Nailes online</p>
      </nuxt-link>
    </div>
    <div class="body">
      <div class="title">
        <link href="https://fonts.google.com/specimen/Crimson+Text" rel="stylesheet">
        <p>NAILIST</p>
      </div>
      <div class="pro-name">{{ user.name }}</div>
      <div class="pro">
        <div
          v-for="history in histories"
          :key="history.id"
        >{{ history.year }} | {{ history.discription }}</div>
        <div>サロンワークの他、雑誌を中心に活動中</div>
      </div>
      <div class="mag">
        <link href="https://fonts.google.com/specimen/Crimson+Text" rel="stylesheet">
        magazines
      </div>
      <div class="magname">
        <div v-for="magazine in magazines" :key="magazine.id">{{ magazine.name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  async asyncData({ app, error }) {
    try {
      const { profile } = await app.$axios.$get(`/api/users/8/profile`);
      return {
        user: profile.user,
        company: profile.company,
        histories: profile.histories,
        magazines: profile.magazines
      };
    } catch (err) {
      return {
        statusCode: err.response.status,
        message: err.response.statusText
      };
    }
  },
  methods: {
    test() {
      console.log(this.magazines);
    }
  }
};
</script>

<style lang="scss" scoped>
.top {
  font-family: "Indie Flower", sans-serif;
  margin-top: 2rem;
  font-weight: 15;
  font-size: 25px;
  text-align: -webkit-match-parent;
  letter-spacing: 0.025em;
  p {
    color: #777777;
  }
}
.body {
  text-align: center;
  border: 1px solid #aaa;
  padding: 40px 40px;
}
.title {
  font-family: "Crimson Text", sans-serif;
  font-weight: 200;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
  display: inline-block;
  margin-inline-start: 0px;
  text-align: left;
  padding-left: 17px;
  letter-spacing: 0.025em;
}
.pro-name {
  font-weight: 200;
  padding-left: 17px;
}
.pro {
  margin-top: 35px;
  font-weight: 100;
  font-size: 15px;
  text-align: left;
  display: inline-block;
}
.mag {
  margin-top: 2rem;
  font-family: "Crimson Text", sans-serif;
  font-style: italic;
  color: #777777;
}
.magname {
  margin-top: 0.2rem;
  width: 270px;
  font-weight: 100;
  font-size: 15px;
  text-align: left;
  display: inline-block;
}
</style>