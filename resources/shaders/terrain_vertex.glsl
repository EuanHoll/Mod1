#version 400 core

in vec3 position;

out vec3 colour;

uniform mat4 transformMatrix;
uniform mat4 projectMatrix;

void main(void)
{
    gl_Position = projectMatrix * transformMatrix * vec4(position, 1.0);
    colour = vec3(0 , 1, position.y + 0.5);
}