```json
{
  "id": "aaf947cd681d1fe3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286581,
  "host_pid": "9e6742732c60:1",
  "hash": "6bc064e80257f1e92e6b5b3bcf87e733840b9f368d61e9e327e9fc708d6fe690",
  "cid": "QmV16bc064e80257f1e92e6b5b3bcf87e733840b9f36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286581,
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
      "evaluated_at": 1760286581
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
  "sig": "3ce92984427b1a42aaa6712a29c145f46754e3fc996e905b519c255ed7058597"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156493582
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': '0d7de9a99f2e5847'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}