```json
{
  "id": "cc95fa6736feef33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287252,
  "host_pid": "9e6742732c60:1",
  "hash": "3f936ee5c5acb4c350934c71eb2cfaa8f754d05f3b684e4f5633557aa015b2b8",
  "cid": "QmV13f936ee5c5acb4c350934c71eb2cfaa8f754d05f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287252,
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
      "evaluated_at": 1760287252
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2013f5acff438beecdd9dd69d52f136eed07ca56b4e576c7f07f786a5dd73e3b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 16867144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}