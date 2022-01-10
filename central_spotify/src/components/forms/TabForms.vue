<template>
  <v-container>

    <!-- CASO NÃO TENHA TABS -->

    <div v-if="!hasTabs">
      <Forms ref="forms"
      @update="update"
      @onChange="onChange"
      :inputs="inputs"
      :rowClass="rowClass1"
      v-model="valueTab">
      </Forms>
    </div>

    <!-- CASO TENHA TABS -->

    <div v-if="hasTabs">
    <v-tabs v-model="tab" background-color="transparent" color="basil" grow>
      <v-tab v-for="item in tabs" :key="item.id">
        {{ item.name }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
    <!-- REPEAT -->
      <v-tab-item v-for="item in tabs" :key="item.id" class="mt-6 mb-2">
        <!-- <v-card flat color="#FFF0"> -->
          <div v-if="!!item.text" class="mb-4" style="text-align: justify; color: darkgray;">
            <p class="ma-6" v-html="item.text" ></p>
            <v-divider></v-divider>
          </div>
          <Forms ref="forms"
          @update="update"
          @onChange="onChange"
          :inputs="inputsFilter(item.id)"
          v-model="valueTab"
          >
          </Forms>
        <!-- </v-card> -->
      </v-tab-item>
    </v-tabs-items>
  </div>
  </v-container>
</template>

<script>
import Forms from "@/components/forms/Inputs";

export default {
  name: "TabForm",
  props: ["inputs", "value", "tabs", "rowClass"],
  components: {
    Forms,
  },
  data() {
    return {
      value1: {},
      tab: null,
      items: [],
    };
  },
  computed: {
      hm(){
        return {a: "k"}
      },
      rowClass1(){
        return this.rowClass
      },
      hasTabs(){
        return !!this.tabs// && (this.tabs.length > 1)
      },
      valueTab: {
        set(value){
          this.value1 = {...this.value1, ...value}
        },
        get(){
          return this.value1
        }
      }
  },
  methods: {
    inputsFilter(id){
      return this.inputs.filter((x) => x.tab == id)
    },
    update(key) {
      this.$emit("input", this.value1);
      this.$emit("update", key);
    },
    onChange(key) {
      this.$emit("input", this.value1);
      this.$emit("onChange", key);
    },
    start() {
      this.inputs.forEach((item) => {
        this.value1[item.key] = this.value[item.key] ? this.value[item.key] : "";
        this.$refs[item.key][0].start();
      });
    },
  },
  beforeMount(){
      this.inputs.forEach(item => {
          this.value1[item.key] = this.value ? ( this.value[item.key] ? this.value[item.key] : '') : ''
      });
  },
};
</script>
        