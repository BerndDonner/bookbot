{
  description = "BookBot development environment";

  inputs = {
    nixos-config.url = "github:BerndDonner/NixOS-Config";
    nixpkgs.follows = "nixos-config/nixpkgs";
  };

  outputs = { nixpkgs, nixos-config, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = nixos-config.lib.mkPythonDevShell {
        inherit pkgs;

        inputs = { inherit nixos-config nixpkgs; };
        checkInputs = [ "nixos-config" ];
        flakeLockPath = ./flake.lock;

        extraPackages = [
          nixos-config.packages.${system}.bootdev-cli
        ];

        message = "🐍 BookBot development shell ready";
      };
    };
}
