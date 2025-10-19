```json
{
  "id": "461f9ce43101ebfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286162,
  "host_pid": "9e6742732c60:1",
  "hash": "8e97f30d2ff66667d62b17b2931f72b4cbf4b09cfa1de9ddf2e51439b5bb3b46",
  "cid": "QmV18e97f30d2ff66667d62b17b2931f72b4cbf4b09c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286162,
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
      "evaluated_at": 1760286162
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
  "sig": "f0356aef7994a85000a149fe8fb29a68cfb5bb9518965f8135fc599f6f7db636"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039404283
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}