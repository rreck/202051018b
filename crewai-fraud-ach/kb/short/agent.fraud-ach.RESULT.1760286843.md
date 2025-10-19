```json
{
  "id": "dad8d2276557c50a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286843,
  "host_pid": "9e6742732c60:1",
  "hash": "10828877335f593b7b0c4f6ced672d39acd4dc3dd1696e3981fe96df1bad1da1",
  "cid": "QmV110828877335f593b7b0c4f6ced672d39acd4dc3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286843,
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
      "evaluated_at": 1760286843
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
  "sig": "16f82703596d86133c0c3c71d73a16d85f83286db94f4b36e4b1e51d832c36b8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000249127775
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '35c1bd481e0f1f5f'}}}