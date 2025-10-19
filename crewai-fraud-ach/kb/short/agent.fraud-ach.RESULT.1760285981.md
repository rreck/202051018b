```json
{
  "id": "7d42d87d6ac1a6e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285981,
  "host_pid": "9e6742732c60:1",
  "hash": "5bda78806efa9933bd78366ef1a3bc79b363931b57aed4c8d2693ccde9c3a762",
  "cid": "QmV15bda78806efa9933bd78366ef1a3bc79b363931b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285981,
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
      "evaluated_at": 1760285981
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
  "sig": "d7bd9e711e284189ab5b02407aa2645ade53b15dda1866fc1ad6fdb4b3bf63fc"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026908362
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': '7a1f70b5e24e62dd'}}}