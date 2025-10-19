```json
{
  "id": "31a04c40e2c74dbc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286849,
  "host_pid": "9e6742732c60:1",
  "hash": "f091ac6a30c20898c5e65378bf43a69c8cfb39cc7468c1d9e97fa7a67b0c2b4a",
  "cid": "QmV1f091ac6a30c20898c5e65378bf43a69c8cfb39cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286849,
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
      "evaluated_at": 1760286849
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
  "sig": "a55b66ac77b3de218da568c73a18f3e7ef30251e55f10062ec682cde64936659"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022109746
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '2a578690bb80e431'}}}