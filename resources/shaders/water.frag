#version 120

varying vec3 gradient;

void main()
{
    gl_FragColor = vec4(gradient, 0.5f);
}