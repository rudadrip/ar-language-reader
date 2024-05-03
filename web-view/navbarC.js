class navbarC extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback(){
    this.render()
  }
  render () { this.innerHTML=`
    <div class="navbar bg-base-100">
      <div class="flex-1">
        <a class="btn btn-ghost text-xl">Auto Read</a>
      </div>
      <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
          <li><a href="index.html">Converter</a></li>
          <li>
            <details>
              <summary>
                Other
              </summary>
              <ul class="p-2 bg-base-100 rounded-t-none">
                <li><a href="info.html">Info</a></li>
                <li><a href="about-me.html">About Me</a></li>
              </ul>
            </details>
          </li>
        </ul>
      </div>
    </div>`
  }
}

customElements.define("navbar-c",navbarC)