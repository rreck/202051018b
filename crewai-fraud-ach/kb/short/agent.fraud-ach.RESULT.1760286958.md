```json
{
  "id": "fd463c2c0ef0c483",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286958,
  "host_pid": "9e6742732c60:1",
  "hash": "a5a4c4be20d6ad1f3daa2c9908b236973d00ce9b85a0f9e15e1938961e0feef1",
  "cid": "QmV1a5a4c4be20d6ad1f3daa2c9908b236973d00ce9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286958,
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
      "evaluated_at": 1760286958
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
  "sig": "cfcce5d8aaa0183a97fb373a994775fdaa18af94c65a4ab285659fdfd8c78e86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 28341635, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}