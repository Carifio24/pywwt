import { App } from "@wwtelescope/research-app";

export function createRender(app) {
  return ({ model, el }) => {
    let _appUrl = location.toString();
    const _appOrigin = _appUrl.origin;
    
    const iframe = document.createElement('iframe');
    // Pass our origin so that the iframe can validate the provenance of the
    // messages that are posted to it. This isn't acceptable for real XSS
    // prevention, but so long as the research app can't do anything on behalf
    // of the user (which it can't right now because we don't even have
    // "users"), that's OK.
    iframe.src = _appUrl + '?origin=' + encodeURIComponent(location.origin);
    iframe.style.setProperty('height', '400px', '');
    iframe.style.setProperty('width', '100%', '');
    iframe.style.setProperty('border', 'none', '');

    const div = document.createElement("div");
    div.setAttribute("id", "wwt-anywidget-wrapper");
    div.appendChild(iframe);
    div.style.setProperty("height", "400px", "");
    div.style.setProperty("width", "100%", "");
    div.style.setProperty("border", "none", "");

    const mounted = model.get("mounted");
    el.appendChild(div);
    const vm = app.mount(div);

    model.on("msg:custom", (msg) => {
      iframe.contentWindow.postMessage(msg);
    });

    window.addEventListener(
      "message",
      (event) => {
        if (event.data.ready === "research_app_ready") {
          model.set("mounted", True);
          model.save_changes();
          return;
        }
        model.send(event.data);
      }, false);

    return () => app.unmount();

  };
}

export default createRender(App);
