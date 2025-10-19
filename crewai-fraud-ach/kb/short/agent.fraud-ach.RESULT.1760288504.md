```json
{
  "id": "a563b842d6db2c37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288504,
  "host_pid": "9e6742732c60:1",
  "hash": "914bcf669e774dd4a28e7bada4458de05d0051d9479e4d74765a3ea96281e1f2",
  "cid": "QmV1914bcf669e774dd4a28e7bada4458de05d0051d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288504,
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
      "evaluated_at": 1760288504
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
  "sig": "02598111f60a066314944e29f974441dd557a96a74a171a5eec5631f206d8e06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}