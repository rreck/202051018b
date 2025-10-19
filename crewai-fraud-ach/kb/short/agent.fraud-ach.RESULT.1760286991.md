```json
{
  "id": "e109a026eb1282e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286991,
  "host_pid": "9e6742732c60:1",
  "hash": "daf57db33fe0aef45b9e355fbfcbb2062295b018dc0aaff34162c39a16bc82d5",
  "cid": "QmV1daf57db33fe0aef45b9e355fbfcbb2062295b018",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286991,
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
      "evaluated_at": 1760286991
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
  "sig": "af6094dd9f1904b3e02ad22a8f08c3bf2b3c02ca7ca3d5dacf0e10c09cd9a907"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039663431
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}