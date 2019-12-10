<template>
  <v-container class="pa-2" fluid>
    <v-row>
      <template v-for="n in card_col">
        <v-col :key="n">
          <v-list>
            <template v-for="(link, index) in links">
              <g-link v-if="index%card_col===n-1" :key="link.id" :to="link.url">
                <v-list-item link>
                  <v-list-item-content>
                    <v-list-item-title v-text="link.name"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </g-link>
            </template>
          </v-list>
        </v-col>
        <v-divider v-if="n % card_col != 0 && n < links.length" vertical></v-divider>
      </template>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ["links", "card_col"]
};
</script>