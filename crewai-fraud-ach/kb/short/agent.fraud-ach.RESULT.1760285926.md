```json
{
  "id": "110cdfa423efbe51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285926,
  "host_pid": "9e6742732c60:1",
  "hash": "ecf8da4ff4ee7416be6cf58364a248522323e90a8245d441e6d87f396adbabfa",
  "cid": "QmV1ecf8da4ff4ee7416be6cf58364a248522323e90a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285926,
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
      "evaluated_at": 1760285926
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
  "sig": "17c35f897ee6130a483127f8cab13d3deefe7f409e06d362f6aba3e894a5435e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038480332
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}