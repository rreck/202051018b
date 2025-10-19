```json
{
  "id": "6bb5dd12488a97fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287157,
  "host_pid": "9e6742732c60:1",
  "hash": "b5ca41967b1f68c3d757fa66a85154d00ea691162485639f155bd35e587f705e",
  "cid": "QmV1b5ca41967b1f68c3d757fa66a85154d00ea69116",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287157,
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
      "evaluated_at": 1760287157
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
  "sig": "1a329fb4beeec3ea77b4e968e5508f4b27bf499302750e2d578de264e4a53f21"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467395210
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'b5e2565aea18e07c'}}}