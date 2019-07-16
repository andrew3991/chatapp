<template>
  <div class="container">
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true">Sign Up</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div class="tab-pane fade show active" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signUp"><!--access form elements-->
              <div class="form-group">
                
              <b-field 
            message="This email is invalid">
            <b-input placeholder="Email" v-model="email" type="email"
                value="john@"
                maxlength="30">
            </b-input>
        </b-field>
              </div>
              <div class="form-row">
                <b-field >
                <b-input placeholder="Username" v-model="username" value="johnsilver" maxlength="30"></b-input>
                <b-input placeholder="Password" v-model="password" type="password"
                        value="iwantmytreasure"
                        password-reveal>
                </b-input>
                </b-field>
                
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="toc" required>
                  <label class="form-check-label" for="gridCheck">
                    Accept terms and Conditions
                  </label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign up</button>
            </form>
          </div>

          <div class="tab-pane fade" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <b-field>
                <b-input  placeholder="Username" v-model="username" value="johnsilver" maxlength="30"></b-input>
                </b-field>
                <b-field>
                    <b-input  placeholder="Password" v-model="password" type="password"
                        value="iwantmytreasure"
                        password-reveal>
                    </b-input>
                </b-field>
                
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign in</button>
            </form>
          </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  const $ = window.jQuery // JQuery
  export default {
    data () {
      return {
        email: '', username: '', password: ''
      }
    },
    methods: {
      signUp () {
        $.post('http://localhost:8000/auth/users/create/', this.$data, (data) => {
          alert('Your account has been created. You will be signed in automatically' + this.$data)
          this.signIn()
        })
        .fail((response) => {
          alert(response.responseText)
        })
      },
      signIn () {
        const credentials = {username: this.username, password: this.password}
        $.post('http://localhost:8000/auth/token/create/', credentials, (data) => {
          sessionStorage.setItem('authToken', data.auth_token)
          sessionStorage.setItem('username', this.username)
          this.$router.push('/chats')
        })
        .fail((response) => {
          alert(response.responseText)
        })
      }
    }
  }
</script>

<style scoped>
  #auth-container {
    margin-top: 50px;
  }

  .tab-content {
    padding-top: 20px;
  }
</style>