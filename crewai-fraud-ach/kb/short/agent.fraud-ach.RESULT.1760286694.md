```json
{
  "id": "bd87ac7eb90a899d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286694,
  "host_pid": "9e6742732c60:1",
  "hash": "e3655d983ec1297dc1855e6741edf56e44394b66d7870059445d8d72f61c3dc1",
  "cid": "QmV1e3655d983ec1297dc1855e6741edf56e44394b66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286694,
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
      "evaluated_at": 1760286694
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
  "sig": "1df86258637aa2dc5268ac7f7b27d49d22662f9327e6984bbb093c2a23f59596"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 824845893834283
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285764, 'matching_hash': '751a36f41382ae06'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}