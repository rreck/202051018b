```json
{
  "id": "439c5e1371ad740d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292840,
  "host_pid": "9e6742732c60:1",
  "hash": "59d5426c67e4378bd7d66acda63649b27cb2b687ff455fa150b70a5676a3214b",
  "cid": "QmV159d5426c67e4378bd7d66acda63649b27cb2b687",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292840,
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
      "evaluated_at": 1760292840
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
  "sig": "74dc7aeae09c3804cadd1ee49ef69ecc2d499dd82c1dd5d80bb7095de8afc609"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 93176890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}