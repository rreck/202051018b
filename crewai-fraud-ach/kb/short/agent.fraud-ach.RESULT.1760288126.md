```json
{
  "id": "d48146855b95bea1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288126,
  "host_pid": "9e6742732c60:1",
  "hash": "f36fc00739648f7628f852ccc8ee50c6051e8adef686a82a0f55a23f5935ea3b",
  "cid": "QmV1f36fc00739648f7628f852ccc8ee50c6051e8ade",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288126,
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
      "evaluated_at": 1760288126
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
  "sig": "4b6d6eb600cf2a56250f7c247e2c9ecd375b2df262fdecedb1244e88ecb5fe9f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158642736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 15200620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}