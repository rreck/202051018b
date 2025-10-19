```json
{
  "id": "eea16d77be7c35ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286796,
  "host_pid": "9e6742732c60:1",
  "hash": "8c85c17c03c41a6e39c2db6a11933b2aa5fb8eecf1851225ff8e5e6c358ed2fc",
  "cid": "QmV18c85c17c03c41a6e39c2db6a11933b2aa5fb8eec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286796,
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
      "evaluated_at": 1760286796
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
  "sig": "b92cf61be6d20524a18f2e1d4c113fc52fecec33fb09e9c1f79483c23ef203d0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025375881
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': '7f563b0766db4821'}}}