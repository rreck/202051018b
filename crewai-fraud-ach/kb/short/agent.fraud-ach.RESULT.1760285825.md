```json
{
  "id": "2682499142c5efed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285825,
  "host_pid": "9e6742732c60:1",
  "hash": "f1ac7ac253a9e4ab5480a8ccc46f93232c95ec166db931d0683072a44973d9b7",
  "cid": "QmV1f1ac7ac253a9e4ab5480a8ccc46f93232c95ec16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285825,
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
      "evaluated_at": 1760285825
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "cb15c80ea6ce7550545fca2d23882b8caa26ab0ca5537358d1be359846545eb2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000035025346
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760284979, 'matching_hash': '4e18e54a79e9d8ab'}}}