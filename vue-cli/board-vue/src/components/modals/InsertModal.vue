<template>
  <!-- Modal insert-->
  <div class="modal" id="insertModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">글쓰기</h4>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="titleInsert" class="form-label">제목</label>
            <input
              v-model="title"
              type="text"
              class="form-control"
              id="titleInsert"
            />
          </div>
          <div class="mb-3">
            <label for="contentInsert" class="form-label">내용</label>

            <!-- New for FileUpload, CKEditor -->
            <div id="divEditorInsert"></div>
            <!-- / New for FileUpload, CKEditor -->
          </div>
          <div class="mb-3">
            <div class="form-check">
              <input
                v-model="attachFile"
                class="form-check-input"
                type="checkbox"
                value=""
                id="chkFileUploadInsert"
              />
              <label class="form-check-label" for="chkFileUploadInsert"
                >파일 추가</label
              >
            </div>
          </div>
          <div
            v-show="attachFile"
            class="mb-3"
            style="display: none"
            id="imgFileUploadInsertWrapper"
          >
            <input
              @change="changFile"
              type="file"
              id="inputFileUploadInsert"
              multiple
            />
            <div id="imgFileUploadInsertThumbnail" class="thumbnail-wrapper">
              <img
                v-for="(file, index) in fileList"
                :key="index"
                :src="file"
                alt=""
              />
            </div>
          </div>
          <button
            @click="boardInsert"
            class="btn btn-sm btn-primary btn-outline float-end"
            data-bs-dismiss="modal"
            type="button"
          >
            등록
          </button>
        </div>
      </div>
    </div>
  </div>
  <!-- End Modal -->
</template>

<script>
import Vue from "vue";
import VueAlertify from "vue-alertify";
import CKEditor from "@ckeditor/ckeditor5-vue2";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import http from "@/common/axios.js";

Vue.use(VueAlertify);
Vue.use(CKEditor);

export default {
  data() {
    return {
      title: "",
      CKEditor: "",
      attachFile: false,
      fileList: [],
    };
  },
  methods: {
    initUI() {
      this.title = "";
      this.CKEditor.setData("");
      this.attachFile = false;
      this.fileList = [];
      document.querySelector("#inputFileUploadInsert").value = "";
    },
    changFile(fileEvent) {
      this.fileList = [];

      const fileArray = Array.from(fileEvent.target.files);
      fileArray.forEach((file) =>
        this.fileList.push(URL.createObjectURL(file))
      );

      // const fileArray = fileEvent.target.files;
      // let cnt = fileArray.length;
      // for (let i = 0; i < cnt; i++) {
      //   this.fileList.push(URL.createObjectURL(fileArray[i]));
      // }
    },
    async boardInsert() {
      let formData = new FormData();
      formData.append("title", this.title);
      formData.append("content", this.CKEditor.getData());
      // let attachFiles = document.querySelector("#inputFileUploadInsert");
      // let cnt = attachFiles.files.length;
      // for (let i = 0; i < cnt; i++) {
      //   formData.append("file", attachFiles.files[i]);
      // }
      let attachFiles = document.querySelector("#inputFileUploadInsert").files;
      if (attachFiles.length > 0) {
        const fileArray = Array.from(attachFiles);
        fileArray.forEach((file) => formData.append("file", file));
      }

      let options = {
        headers: {
          "Content-Type": "mmultipart/form-data",
        },
      };
      try {
        let response = await http.post("/boards", formData, options);
        let { data } = response;
        console.log(data);
        if (data.result == "login") {
          this.$router.push("/login");
        } else {
          this.$alertify.success("글이 등록되었습니다.");
          this.closeModal();
        }
      } catch (error) {
        console.error(error);
      }
    },
    closeModal() {
      this.$emit("call-parent-insert");
    },
  },
  async mounted() {
    try {
      this.CKEditor = await ClassicEditor.create(
        document.querySelector("#divEditorInsert")
      );
    } catch (error) {
      console.error(error);
    }
    let $this = this;
    this.$el.addEventListener("show.bs.modal", function () {
      $this.initUI();
    });
  },
};
</script>

<style scoped>
.modal >>> .ck-editor__editable {
  min-height: 300px !important;
}

.modal >>> .thumbnail-wrapper {
  margin-top: 5px;
}

.modal >>> .thumbnail-wrapper img {
  width: 100px !important;
  margin-right: 5px;
  max-width: 100%;
}
</style>
