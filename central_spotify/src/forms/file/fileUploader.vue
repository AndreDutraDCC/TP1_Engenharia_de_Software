<template>
    <v-card elevation-1>
      <input
        style="display: none;"
        ref="input"
        type="file"
        @change="setFile"
      />
      <v-card-title>
        {{label}}
      </v-card-title>
      <v-card-text>
        <v-progress-linear v-if="loading" indeterminate></v-progress-linear>
        <p><i>*Para arquivos comprimidos utilize <strong>apenas</strong> .zip (não utilizar .rar)</i></p>
        <v-btn v-if="url && (!loading)" @click="openFile()" block color="primary" text>
          <v-icon class="mx-3">mdi-open-in-new</v-icon>
          Abrir aquivo
        </v-btn>
        <v-btn v-if="!disabled" :disabled="loading" block @click="showFileChooser()" color="primary" text>
          <v-icon class="mx-3">mdi-file</v-icon>
          {{url ? 'Trocar Arquivo' : 'Selecionar Arquivo'}}
        </v-btn>
      </v-card-text>
    </v-card>
</template>
<script>

// import AvatarCropper from "vue-avatar-cropper";
// @ is an alias to /src
import Upload from '@/service/upload'
const upload = new Upload()

export default {
  name: "ImageSelector",
  components: { 
    
   },
  props: ['filename','bucket', 'subfolder','disabled','label'],
  data() {
    return {
      dialog: false,
      loading: false,
      base64: '',
      url: ''
    };
  },
  methods: {
    async uploadFile(file, fileBase64, bucket, subfolder){
      try {
        this.loading = true
        let fileUploaded = await upload.file(file, fileBase64, bucket, subfolder)
        this.url = this.getUrlFile(fileUploaded.fileURLKey, this.bucket) 
        this.$emit('uploaded', fileUploaded.fileURLKey)
      } catch (error) {
        console.log(error)  
      }
      this.loading = false
    },
    setFile(e){
      const file = e.target.files[0];

      // if (file.type.indexOf('image/') === -1) {
      //   alert('Por favor, selecione uma imagem');
      //   return;
      // }

      if (typeof FileReader === 'function') {
        const reader = new FileReader();

        reader.onload = (event) => {
          this.base64 = event.target.result;
          this.uploadFile(file, this.base64, this.bucket, this.subfolder)
        };

        reader.readAsDataURL(file);
      } else {
        alert('Sorry, FileReader API not supported');
      }
    },
    showFileChooser() {
      this.$refs.input.click();
    },
    getUrlFile(filename, bucket){
        return `https://s3.amazonaws.com/${bucket}/${filename}`
    },
    openFile(){
      window.open(this.url, '_blank')
    }

  },
  mounted(){
    if(this.filename) this.url = this.getUrlFile(this.filename, this.bucket)
  },
  computed: {
  }
};
</script>
<style lang="scss" scoped>
</style>
