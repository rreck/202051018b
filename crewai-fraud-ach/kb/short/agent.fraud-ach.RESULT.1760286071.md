```json
{
  "id": "845fbc9167a06801",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286071,
  "host_pid": "9e6742732c60:1",
  "hash": "95ca10458fcf4498e43c7091f5ac9e1cb829da1638aed3059b13dd79cfef1853",
  "cid": "QmV195ca10458fcf4498e43c7091f5ac9e1cb829da16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286071,
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
      "evaluated_at": 1760286071
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
  "sig": "1c141ef81c5044aaaa51576c5b74d34050f52fee6529dc2add136ae8512828ae"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100273461392
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': 'ee78248c8d3d65fe'}}}