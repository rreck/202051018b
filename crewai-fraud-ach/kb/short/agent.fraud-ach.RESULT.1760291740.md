```json
{
  "id": "47f4628fc6f489e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291740,
  "host_pid": "9e6742732c60:1",
  "hash": "3150b456da422f8ebd78c10601d4bec107f4d0ebb7cd4da3f19023d5119bd171",
  "cid": "QmV13150b456da422f8ebd78c10601d4bec107f4d0eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291740,
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
      "evaluated_at": 1760291740
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
  "sig": "1f881dab91af3538437d72c72adc22ba8f6a89e9d6a22bfbfbf19bc1025ffffb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466524554
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 69602624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': 'c9a1c21cbf3363ae'}}}