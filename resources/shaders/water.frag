#version 120

varying vec3 colour;

void main()
{
    gl_FragColor = vec4(1.0f, 1.0f, 1.0f, 1.0f) - vec4(colour, 0.0f);
}