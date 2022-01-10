<template>
  <div  >
      
     <v-dialog
        @keydown.esc="close()"
        v-model="show"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
      >
      <v-card tile>
          <v-toolbar
            flat
            dark
            dense
            color="primary"
            style="height: 50px !important;flex: none;"
          >
            <v-btn
              icon
              dark
              @click="close()"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Cortar Imagem</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items>
              <v-btn
                dark
                text
                @click="save()"
              >
              <v-icon class="mx-3">
                mdi-content-save
              </v-icon>
                Salvar
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-card-text>
              <Cropper ref="crop" :ratio="ratio1" />
          </v-card-text>
        </v-card>
     </v-dialog>
  </div>
</template>

<script>
// import AvatarCropper from "vue-avatar-cropper";
// @ is an alias to /src
import Cropper from './Cropper.vue'

export default {
  name: "CropperDialog",
  components: { Cropper },
  props: ['show', 'ratio'],
  methods: {
      close(){
          this.$refs.crop.imgSrc = ''
          this.$refs.crop.$refs.input.value = null
          this.$emit('close')
      },
      save(){
        this.$refs.crop.cropImage()
        this.$emit('crop',this.$refs.crop.cropImg)
        this.$refs.crop.$refs.input.value = null
        this.$refs.crop.reset()
        this.$refs.crop.imgSrc = ''
        this.$emit('close')
      }
  },
  data() {
    return {
    };
  },
  computed: {
    ratio1(){
      return this.ratio
    }
  }
};
</script>
