```json
{
  "id": "b77abb1aa6110ebf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286894,
  "host_pid": "9e6742732c60:1",
  "hash": "db9e77408175455ad1e791b02c9f6d11595353cfc30869c6faf1e470906fbe66",
  "cid": "QmV1db9e77408175455ad1e791b02c9f6d11595353cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286894,
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
      "evaluated_at": 1760286894
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
  "sig": "8bf2a1b4395b134caac9fbb07b5b0b2091e3c1f26eaee670b7de70c65398690d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000039326834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10499936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': '4e66e6716d66a614'}}}