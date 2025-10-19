```json
{
  "id": "aa646fc6f7169c7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285808,
  "host_pid": "9e6742732c60:1",
  "hash": "f41db04fe2243c6db57767fe83e79e0c4dd15e419b3e03a9cc8c996a71e031e6",
  "cid": "QmV1f41db04fe2243c6db57767fe83e79e0c4dd15e41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285808,
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
      "evaluated_at": 1760285808
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
  "sig": "396fd1e1525e912b32b332afe7e7d7ddb5c15a95d338411e580765ff795d3d40"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}