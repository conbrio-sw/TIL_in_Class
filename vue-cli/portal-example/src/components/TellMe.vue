<template>
  <div class="container mt-3 px=0 py=3">
    <div id="CKEditor"></div>
    <button @click="sendTellMe" type="button" class="btn btn-primary mt-2">
      Send
    </button>
  </div>
</template>

<script>
import Vue from "vue";
import CKEditor from "@ckeditor/ckeditor5-vue2";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
Vue.use(CKEditor);
export default {
  data() {
    return {
      CKEditor: null,
    };
  },
  async mounted() {
    try {
      this.CKEditor = await ClassicEditor.create(
        document.querySelector("#CKEditor")
      );
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    sendTellMe: function () {
      let message = this.CKEditor.getData();
      alert(message);
    },
  },
};
</script>

<style scoped>
.container >>> .ck-editor__editable {
  width: 100%;
  height: 200px;
  overflow-y: scroll;
}
</style>
