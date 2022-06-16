<template>
  <!-- Modal detail-->
  <div class="modal fade" id="detailModal">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">글 상세</h4>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <div class="modal-body">
          <div class="example table-responsive">
            <table class="table">
              <tbody>
                <tr>
                  <td>글번호</td>
                  <td>{{ board.boardId }}</td>
                </tr>
                <tr>
                  <td>제목</td>
                  <td>{{ board.title }}</td>
                </tr>
                <tr>
                  <td>내용</td>
                  <td v-html="board.content"></td>
                </tr>
                <tr>
                  <td>작성자</td>
                  <td>{{ board.userName }}</td>
                </tr>
                <tr>
                  <td>작성일시</td>
                  <td>{{ board.regDate }} {{ board.regTime }}</td>
                </tr>
                <tr>
                  <td>조회수</td>
                  <td>{{ board.readCount }}</td>
                </tr>
                <!-- New for FileUpload -->
                <tr>
                  <td colspan="2">첨부파일</td>
                </tr>
                <tr v-if="board.fileList.length > 0">
                  <td colspan="2">
                    <div v-for="(file, index) in board.fileList" :key="index">
                      <span class="fileName">{{ file.fileName }}</span>
                      &nbsp;&nbsp;
                      <a
                        type="button"
                        class="btn btn-outline btn-default btn-xs"
                        :href="file.fileUrl"
                        :download="file.fileName"
                        >내려받기</a
                      >
                    </div>
                  </td>
                </tr>
                <!-- / New for FileUpload -->
              </tbody>
            </table>
          </div>
          <button
            v-show="board.sameUser"
            @click="changeToUpdate"
            id="btnBoardUpdateForm"
            class="btn btn-sm btn-primary btn-outline"
            data-bs-dismiss="modal"
            type="button"
          >
            글 수정하기
          </button>
          <button
            v-show="board.sameUser"
            @click="changeToDelete"
            id="btnBoardDeleteConfirm"
            class="btn btn-sm btn-warning btn-outline"
            data-bs-dismiss="modal"
            type="button"
          >
            글 삭제하기
          </button>
        </div>
      </div>
    </div>
  </div>
  <!-- End Modal -->
</template>

<script>
import http from "@/common/axios.js";
import Vue from "vue";
import VueAlertify from "vue-alertify";
Vue.use(VueAlertify);
export default {
  props: ["board"],
  methods: {
    changeToUpdate() {
      this.$emit("call-parent-change-to-update");
    },
    async changeToDelete() {
      console.log(this.board.boardId);
      try {
        let response = await http.delete("/boards/" + this.board.boardId); // params: params : shorthand property
        let { data } = response;
        console.log(data);
        if (data.result == "login") {
          this.$router.push("/login");
        } else {
          this.$alertify.success("글이 삭제되었습니다.");
        }
      } catch (error) {
        console.error(error);
      }
      this.$emit("call-parent-change-to-delete");
    },
  },
};
</script>

<style></style>
