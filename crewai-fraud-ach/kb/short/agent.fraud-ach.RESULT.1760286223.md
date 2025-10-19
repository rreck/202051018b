```json
{
  "id": "627b6e12472e69c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286223,
  "host_pid": "9e6742732c60:1",
  "hash": "6c4aa84c65579545ce8dac0c3de06465253afc202d5cea3c2056dd61565f4c5d",
  "cid": "QmV16c4aa84c65579545ce8dac0c3de06465253afc20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286223,
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
      "evaluated_at": 1760286223
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
  "sig": "b5a86c713b46ea75bd0016732a7dd2c80078159977d5a1b2a09dff616f596f5b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467961793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}