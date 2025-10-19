```json
{
  "id": "50bda35c2957ddd5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292329,
  "host_pid": "9e6742732c60:1",
  "hash": "dc7f32eacb2cbb3e642f2c0ad8a147f778cfe7409732c4914515df54a4db7cc5",
  "cid": "QmV1dc7f32eacb2cbb3e642f2c0ad8a147f778cfe740",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292329,
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
      "evaluated_at": 1760292329
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
  "sig": "c6720f2e7b9793c280053256a92e069d76c9a1690ec606f7d58a8879dd3ed845"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 59254845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}