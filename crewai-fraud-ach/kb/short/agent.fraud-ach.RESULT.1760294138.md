```json
{
  "id": "f6bc6b1f80be8d62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294138,
  "host_pid": "9e6742732c60:1",
  "hash": "3cb1844b2a6d95aaf3e166cb0dda4a807157b2137bca8f96894fb9644f00cf3b",
  "cid": "QmV13cb1844b2a6d95aaf3e166cb0dda4a807157b213",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294138,
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
      "evaluated_at": 1760294138
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
  "sig": "9013d3ffb8caa8183dd6cfb268df96ba2d1ca7aad93055c93f352bdc34a81c27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241784115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 104388632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'd8ced4219e23835b'}}}