<template>
  <div class="container px=0 py=3">
    <div class="card">
      <img :src="imgSrcUrl" class="card-img-top" alt="..." />
      <div class="card-body">
        <h5 class="card-title">Blog</h5>
        <p class="card-text">
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imgSrcUrl: require("@/assets/logo.png"),
    };
  },
};
</script>

<style></style>
