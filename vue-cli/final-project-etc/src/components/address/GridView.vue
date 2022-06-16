<script>
export default {
  methods: {
    async getSidoList() {
      this.$store.dispatch("getSidoList");
    },
    async getGugunList() {
      this.$store.dispatch("getGugunList");
    },
    async getDongList() {
      this.$store.dispatch("getDongList");
    },
    async getHouseDealList() {
      console.log(this.$store.state.address.dong);
    },
  },
  created() {
    this.getSidoList();
  },
  computed: {
    sidoList() {
      return this.$store.getters.getSidoList;
    },
    gugunList() {
      return this.$store.getters.getGugunList;
    },
    dongList() {
      return this.$store.getters.getDongList;
    },
    sido: {
      get() {
        return this.$store.state.address.sido;
      },
      set(sido) {
        this.$store.commit("SET_ADDRESS_SIDO", sido);
      },
    },
    gugun: {
      get() {
        return this.$store.state.address.gugun;
      },
      set(gugun) {
        this.$store.commit("SET_ADDRESS_GUGUN", gugun);
      },
    },
    dong: {
      get() {
        return this.$store.state.address.dong;
      },
      set(dong) {
        this.$store.commit("SET_ADDRESS_DONG", dong);
      },
    },
  },
  watch: {
    sido: function () {
      console.log("watch : sido()" + this.sido);
      if (this.sido == "0") {
        this.$store.commit("SET_ADDRESS_GUGUNlIST", []);
        this.$store.commit("SET_ADDRESS_DONGlIST", []);
        this.$store.commit("SET_ADDRESS_GUGUN", "0");
        this.$store.commit("SET_ADDRESS_DONG", "0");
      } else {
        this.getGugunList();
      }
    },
    gugun: function () {
      console.log("watch : gugun()" + this.gugun);
      if (this.gugun == "0") {
        this.$store.commit("SET_ADDRESS_DONGlIST", []);
        this.$store.commit("SET_ADDRESS_DONG", "0");
      } else {
        this.getDongList();
      }
    },
    dong: function () {
      console.log("watch : dong()" + this.dong);
      //if (this.dong == "0") return;
      this.getHouseDealList();
    },
  },
};
</script>

<style></style>
