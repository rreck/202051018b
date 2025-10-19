```json
{
  "id": "5bab448a78abe431",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292564,
  "host_pid": "9e6742732c60:1",
  "hash": "898dab88a47f2883359415f5bd65955459037cd8c506d62c7e535a954206e2d8",
  "cid": "QmV1898dab88a47f2883359415f5bd65955459037cd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292564,
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
      "evaluated_at": 1760292564
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
  "sig": "d0751b986b790d44019e9bf11043a9ef03fc3cb653c1566baab932ae7614fc86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 57508600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}