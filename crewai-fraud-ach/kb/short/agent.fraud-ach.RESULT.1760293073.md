```json
{
  "id": "bc34c0974089d89f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293073,
  "host_pid": "9e6742732c60:1",
  "hash": "c07102568fae400f52def284aa06dd0f68ddf757be3a70109683aa42cf1580ae",
  "cid": "QmV1c07102568fae400f52def284aa06dd0f68ddf757",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293073,
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
      "evaluated_at": 1760293073
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
  "sig": "0ba161333942373671d1904c7c676291478fa3b9a7c66a7ae56e29a7e9e7453e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 54690778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}