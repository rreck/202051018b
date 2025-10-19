```json
{
  "id": "02542f97c9614bb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285972,
  "host_pid": "9e6742732c60:1",
  "hash": "a7fb0a5275542a9168bb22e4352defae4506db9c9081ce12b5aac94c303719fa",
  "cid": "QmV1a7fb0a5275542a9168bb22e4352defae4506db9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285972,
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
      "evaluated_at": 1760285972
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
  "sig": "82db42ce671d5335480ed56fad08c8d885c7fbd3b0bbbf455033338f7510cd71"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591886558
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': '37bcf4c9c4817870'}}}