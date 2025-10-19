```json
{
  "id": "099a573fe3055dc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289835,
  "host_pid": "9e6742732c60:1",
  "hash": "c8271221c9061d0557df7291d77e42b289839b2eb630e98ef3fb8c1093013504",
  "cid": "QmV1c8271221c9061d0557df7291d77e42b289839b2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289835,
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
      "evaluated_at": 1760289835
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
  "sig": "69419379fa12aac12085bf74e66f2d67ed7e5a33b1c4f0835954b59cfc6e823d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 60045266, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}