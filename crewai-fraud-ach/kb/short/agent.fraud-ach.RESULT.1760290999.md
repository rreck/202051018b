```json
{
  "id": "d18af0b22bdac89e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290999,
  "host_pid": "9e6742732c60:1",
  "hash": "b759efc5fd7d4700fd62e84c08f70176bf881adce64eb33ca37d509f59fd6dfe",
  "cid": "QmV1b759efc5fd7d4700fd62e84c08f70176bf881adc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290999,
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
      "evaluated_at": 1760290999
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
  "sig": "856404279284d4c4b2a7b23b56f8d1f30278ea5dd04ec509a96c6813eb38c3c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 74841564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}