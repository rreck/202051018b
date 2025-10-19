```json
{
  "id": "b3a0b21715107332",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286993,
  "host_pid": "9e6742732c60:1",
  "hash": "a947845089d7f6e4f6b43aefce200cf2eec3e2e6369d3f8d473c55b9915c980f",
  "cid": "QmV1a947845089d7f6e4f6b43aefce200cf2eec3e2e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286993,
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
      "evaluated_at": 1760286993
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
  "sig": "b55f88c059e942d5dc773e7a3235a1b094a4436200df237dbcae4cad5cc02aa8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467961793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}