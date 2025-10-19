```json
{
  "id": "a33eeb099dbe6947",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286251,
  "host_pid": "9e6742732c60:1",
  "hash": "0fd07141d978ef62afbe33d10d7e26dd01c51329feb48af7c43d8f20c4db7b12",
  "cid": "QmV10fd07141d978ef62afbe33d10d7e26dd01c51329",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286251,
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
      "evaluated_at": 1760286251
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
  "sig": "25d12e979987b9fa3ee992a89a12ce91d332b6a53d83033be1d24800586fedbe"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100275697869
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285764, 'matching_hash': '6e45970a6bf10306'}}}