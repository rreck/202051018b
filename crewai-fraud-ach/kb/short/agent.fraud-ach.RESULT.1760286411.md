```json
{
  "id": "6a96411f2ec3c893",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286411,
  "host_pid": "9e6742732c60:1",
  "hash": "0de441db0d3a2f1d58fd984c0d6c0bc7b2a5023c9d947a48dcdab2047006711d",
  "cid": "QmV10de441db0d3a2f1d58fd984c0d6c0bc7b2a5023c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286411,
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
      "evaluated_at": 1760286411
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
  "sig": "b61beafca620c549a0db28b0141faf6557a81ca20eeb35d3a99f90e93e3b52b3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463448865
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}