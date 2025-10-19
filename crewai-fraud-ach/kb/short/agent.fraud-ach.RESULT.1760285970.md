```json
{
  "id": "1ec0a5f1c81c3942",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285970,
  "host_pid": "9e6742732c60:1",
  "hash": "b3c53d93cb9047e432cc1bd824f504d3992fa668820ef8aa5229f865d4cc7d00",
  "cid": "QmV1b3c53d93cb9047e432cc1bd824f504d3992fa668",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285970,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760285970
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "a74275e06661d5cd290a444013cf476d092b0679c6f44681cee7661e1bce9d1e"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 304701772219564
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}