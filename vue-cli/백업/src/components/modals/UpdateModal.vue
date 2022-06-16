<template>
  <div class="modal fade" id="updateModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">글수정</h4>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label for="titleUpdate" class="form-label">제목</label>
            <input type="text" class="form-control" v-model="board.title" />
          </div>
          <div class="mb-3">
            <!-- New for FileUpload, CKEditor -->
            <div id="divEditorUpdate"></div>
            <!-- New for FileUpload -->
          </div>
          <div class="mb-3">
            첨부파일 : <br />
            <span>
              <span v-for="(file, index) in board.fileList" :key="index">
                {{ file.fileName }}
              </span>
            </span>
          </div>
          <div class="mb-3">
            <div class="form-check">
              <input
                v-model="attachFile"
                class="form-check-input"
                type="checkbox"
                value=""
                id="chkFileUploadUpdate"
              />
              <label class="form-check-label" for="chkFileUploadUpdate"
                >파일 변경</label
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
              @change="changeFile"
              type="file"
              id="inputFileUploadUpdate"
              multiple
            />
            <div id="imgFileUploadUpdateThumbnail" class="thumbnail-wrapper">
              <img
                v-for="(file, index) in fileList"
                :key="index"
                v-bind:src="file"
                alt=""
              />
            </div>
          </div>
          <button
            @click="boardUpdate"
            id="btnBoardUpdate"
            class="btn btn-sm btn-primary btn-outline float-end"
            data-bs-dismiss="modal"
            type="button"
          >
            수정
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import http from "@/common/axios.js";

import Vue from "vue";
import CKEditor from "@ckeditor/ckeditor5-vue2";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import VueAlertify from "vue-alertify";

Vue.use(CKEditor).use(VueAlertify);

export default {
  props: ["board"],
  data() {
    return {
      CKEditor: "",
      tempCKEditor: "",
      attachFile: false,
      fileList: [],

      //열렸을 때 값을 업데이트 하기 위한 플러그
      isUpdated: false,
    };
  },
  async mounted() {
    try {
      this.CKEditor = await ClassicEditor.create(
        document.querySelector("#divEditorUpdate")
      );
    } catch (error) {
      console.error(error);
    }

    //열렸을 때 이벤트 등록
    let $this = this;
    this.$el.addEventListener("show.bs.modal", function () {
      $this.initUI();
    });
  }, //end mounted
  updated() {
    //CKEditor가 빈칸이고 모달이 열렸을 때 CKEditor의 값을 초기화
    if (!this.isUpdated && this.CKEditor.getData() == "") {
      this.CKEditor.setData(this.board.content);
      this.isUpdated = true;
    }
  },
  methods: {
    initUI: function () {
      this.attachFile = false;
      this.fileList = [];
      document.querySelector("#inputFileUploadUpdate").value = "";
      //isUpdated를 초기화
      this.isUpdated = false;
      //isUpdated가 초기화 되고 CKEditor를 빈칸으로 만들면서 updated호출됨
      this.CKEditor.setData("");
    },
    changeFile: function (fileEvent) {
      this.fileList = [];

      const fileArray = Array.from(fileEvent.target.files);
      fileArray.forEach((file) =>
        this.fileList.push(URL.createObjectURL(file))
      );
    },
    boardUpdate: async function () {
      let formData = new FormData();
      formData.append("title", this.board.title);
      formData.append("baordId", this.board.boardId);
      formData.append("content", this.CKEditor.getData());

      let attachFiles = document.querySelector("#inputFileUploadInsert").files;
      if (attachFiles.length > 0) {
        const fileArray = Array.from(attachFiles);
        fileArray.forEach((file) => formData.append("file", file));
      }

      let options = {
        headers: { "Content-Type": "multipart/form-data" },
      };

      try {
        let response = await http.post(
          "/boards/" + this.board.boardId,
          formData,
          options
        );
        let { data } = response;
        console.log(data);

        if (data.result == "login") {
          this.$router.push("/login");
        }

        if (data.result == 1) {
          this.$alertify.success("글이 수정되었습니다");
          this.$emit("call-parent-update");
          this.closeModal();
        } else {
          this.$alertify.error("글 수정 과정에 문제가 생겼습니다.");
        }
      } catch (error) {
        console.error(error);
        this.$alertify.error("글 수정 과정에 문제가 생겼습니다.");
      }
    }, //end boardUpdate
    closeModal: function () {
      this.$emit("call-parent-change-to-update");
    },
  },
};
</script>

<style scoped>
.modal >>> .ck-editor__editable {
  width: 100%;
  min-height: 200px !important;
  overflow-y: scroll;
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
