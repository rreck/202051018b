```json
{
  "id": "c21942d1402e8320",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285850,
  "host_pid": "9e6742732c60:1",
  "hash": "dc30792a09e6196028feb33bb3f8c155301f99f3224e60603de25f5428d6edbe",
  "cid": "QmV1dc30792a09e6196028feb33bb3f8c155301f99f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285850,
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
      "evaluated_at": 1760285850
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
  "sig": "ad3ddbe524584c87c1b991d1f7ce17a9dcc97444bdb131259ea188cf9cceac83"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000242075877
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}