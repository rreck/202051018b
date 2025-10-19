```json
{
  "id": "d06691e1ff9e8122",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290202,
  "host_pid": "9e6742732c60:1",
  "hash": "8e11035d800a0abe863747fc774b3adc4db68156269db9693679bfaacd0855fc",
  "cid": "QmV18e11035d800a0abe863747fc774b3adc4db68156",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290202,
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
      "evaluated_at": 1760290202
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
  "sig": "ab33de8fe26d5696aba47eb7c8419f21c2954c99e89da969962b3d167bd79584"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277495051
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 70118352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': 'b54d2b84a0558fd6'}}}