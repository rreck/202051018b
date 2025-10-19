```json
{
  "id": "ab1bf84e0c671daa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286311,
  "host_pid": "9e6742732c60:1",
  "hash": "4ef5a85f418b8b3200780ebff2fe89fbb0d73d372e6251fc603b5cba960c124a",
  "cid": "QmV14ef5a85f418b8b3200780ebff2fe89fbb0d73d37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286311,
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
      "evaluated_at": 1760286311
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
  "sig": "a99670840056423a77f2c3f52b8a7f74ea09cff0c56d04fb5833be368cf269d2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025723119
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}