<template>
  <div>
    <div>
      <p>NAILS ONLINE</p>
    </div>
    <div>
      <img v-for="image in images" :key="image.id" :src="image.image_url" class="image">
    </div>

  </div>

</template>

<script>
export default {
  async asyncData({app, error}) {
    try {
      const { data } = await app.$axios.get(`/api/images`)
      return {
        images: data.images,
      }
    } catch (err) {
      return {
        statusCode: err.response.status,
        message: err.response.statusText,
      }
    }
  },
}
</script>
<style lang="scss">
.image {
  width: 50px;
  height: 50px;
}
</style>
