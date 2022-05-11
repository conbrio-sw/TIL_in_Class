export default {
    
    template: 
    `
    <div class="mt-3 container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <!--<a class="nav-link active" aria-current="page" href="#">Home</a>-->
          <router-link to="/half" class="nav-link">반반머리</router-link>
          </li>
        <li class="nav-item">
          <router-link to="/pink" class="nav-link">핑크머리</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/tellMe" class="nav-link">TellMe</router-link>
        </li>
      </ul>
      <form class="d-flex">
        <input v-model="searchWord" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button @click="search" class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
    </div>
    `,
  data: function () {
    return {
      searchWord: "",
    }
  },
  methods: {
    search() {
      alert(this.searchWord)
    }
  }
}