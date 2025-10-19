```json
{
  "id": "94f49f1a591252f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286043,
  "host_pid": "9e6742732c60:1",
  "hash": "8dda871c8d7d83dfa9a622d16df998a4a2d5c43fc606a8f79f661c15459c1061",
  "cid": "QmV18dda871c8d7d83dfa9a622d16df998a4a2d5c43f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286043,
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
      "evaluated_at": 1760286043
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
  "sig": "8ee3301908ca31b34add39b128e166026445214a9cbf5542aba199d01c18fb61"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591834365
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}