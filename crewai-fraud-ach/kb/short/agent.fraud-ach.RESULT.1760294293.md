```json
{
  "id": "4e5a39baaeabaadd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294293,
  "host_pid": "9e6742732c60:1",
  "hash": "3143c693777703d1b4cfc0977424ec6fadeff83c8f1d5296427fb4b19960615b",
  "cid": "QmV13143c693777703d1b4cfc0977424ec6fadeff83c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294293,
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
      "evaluated_at": 1760294293
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
  "sig": "8d2b9e5ae7f45d5a227afee87e7d97d45d9babe89343bc904225f46e83d9977c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 311, 'threshold': 50, 'total_amount': 99315984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 310, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}