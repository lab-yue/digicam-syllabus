<template>
  <div class="syllabus-search">
    <input
      @focus="open"
      class="syllabus-search-input"
      type="text"
      v-model="searchText"
      placeholder="search..."
    />
    <ul v-if="isOpen && resultList.length" class="syllabus-search-result">
      <li v-for="(result,id) in resultList" :key="id" @click="close">
        <router-link :to="result.url">
          <p class="syllabus-search-result-item">
            <span class="syllabus-search-result-title">{{result.title}}</span>
            <span v-html="result.text"></span>
          </p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
const { data } = require("../../../data/search.json");

export default {
  data() {
    return {
      searchText: "",
      isOpen: false
    };
  },
  methods: {
    open() {
      this.isOpen = true;
    },
    close() {
      this.isOpen = false;
    }
  },
  computed: {
    resultList() {
      if (!this.searchText) {
        return [];
      }

      const searchText = this.searchText.toLowerCase();
      const result = data
        .filter(item => {
          item.index = item.text.toLowerCase().indexOf(searchText);

          return item.index !== -1;
        })
        .splice(0, 15)
        .map(item => {
          const text = item.text
            .substring(item.index - 15, item.index + 15)
            .replace(
              new RegExp(`(${searchText})`, "i"),
              `<span class="syllabus-search-highlight">$1</span>`
            );
          return { text, title: item.title, url: `/${item.type}/${item.id}` };
        });
      return result;
    }
  }
};
</script>


<style lang="scss">
.syllabus-search {
  width: 60%;
  text-align: right;
  position: relative;
  &-input {
    width: 30%;
    transition: 0.3s all ease-in-out;
    border: 0;
    border-bottom: 1px solid #c8dad3;
    &:focus {
      width: 100%;
      outline: none;
      border-bottom: 1px solid slategrey;
    }
  }
  &-highlight {
    background-color: yellow;
  }
  &-result {
    background-color: #fff;
    width: 100%;
    padding: 10px;
    z-index: 100;
    position: absolute;
    top: 100%;
    left: 0;
    box-shadow: 0 0 5px #aaa;
    border-radius: 5px;
    text-align: left;
    &-item {
      transition: 0.3s all ease-in-out;
      border-collapse: collapse;
      //display: flex;
      margin: 0;
      padding: 0 5px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      &:hover {
        background-color: #f2f6f5;
      }
    }
    &-title {
      width: 6rem;
      overflow: hidden;
      display: inline-block;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin-right: 5px;
      padding-right: 5px;
      border-right: 1px solid slategrey;
    }
  }
}
@media screen and (max-width: 640px) {
  .syllabus-search {
    &-result {
      position: fixed;
      left: 0;
      top: 3rem;
    }
  }
}
</style>
