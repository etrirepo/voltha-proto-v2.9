// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: voltha_protos/onu_inter_adapter_service.proto

package org.opencord.voltha.onu_inter_adapter_service;

public final class VolthaOnuInterAdapterService {
  private VolthaOnuInterAdapterService() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n-voltha_protos/onu_inter_adapter_servic" +
      "e.proto\022\031onu_inter_adapter_service\032\032volt" +
      "ha_protos/common.proto\032\033google/protobuf/" +
      "empty.proto\032!voltha_protos/inter_adapter" +
      ".proto\032\032voltha_protos/health.proto2\333\003\n\026O" +
      "nuInterAdapterService\022;\n\017GetHealthStatus" +
      "\022\022.common.Connection\032\024.health.HealthStat" +
      "us\022L\n\rOnuIndication\022#.inter_adapter.OnuI" +
      "ndicationMessage\032\026.google.protobuf.Empty" +
      "\022D\n\016OmciIndication\022\032.inter_adapter.OmciM" +
      "essage\032\026.google.protobuf.Empty\022X\n\023Downlo" +
      "adTechProfile\022).inter_adapter.TechProfil" +
      "eDownloadMessage\032\026.google.protobuf.Empty" +
      "\022L\n\rDeleteGemPort\022#.inter_adapter.Delete" +
      "GemPortMessage\032\026.google.protobuf.Empty\022H" +
      "\n\013DeleteTCont\022!.inter_adapter.DeleteTcon" +
      "tMessage\032\026.google.protobuf.EmptyB\220\001\n-org" +
      ".opencord.voltha.onu_inter_adapter_servi" +
      "ceB\034VolthaOnuInterAdapterServiceZAgithub" +
      ".com/opencord/voltha-protos/v5/go/onu_in" +
      "ter_adapter_serviceb\006proto3"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
        new com.google.protobuf.Descriptors.FileDescriptor.    InternalDescriptorAssigner() {
          public com.google.protobuf.ExtensionRegistry assignDescriptors(
              com.google.protobuf.Descriptors.FileDescriptor root) {
            descriptor = root;
            return null;
          }
        };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
          org.opencord.voltha.Common.getDescriptor(),
          com.google.protobuf.EmptyProto.getDescriptor(),
          org.opencord.voltha.inter_adapter.InterAdapter.getDescriptor(),
          org.opencord.voltha.health.Health.getDescriptor(),
        }, assigner);
    org.opencord.voltha.Common.getDescriptor();
    com.google.protobuf.EmptyProto.getDescriptor();
    org.opencord.voltha.inter_adapter.InterAdapter.getDescriptor();
    org.opencord.voltha.health.Health.getDescriptor();
  }

  // @@protoc_insertion_point(outer_class_scope)
}
