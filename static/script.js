document.getElementById('upload-form').onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const res = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    document.getElementById('result').innerHTML = `<img src="${data.url}" width="300"/>`;
};
