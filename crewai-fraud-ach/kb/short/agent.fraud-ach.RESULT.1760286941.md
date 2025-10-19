```json
{
  "id": "cae320bbd57febf9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286941,
  "host_pid": "9e6742732c60:1",
  "hash": "4fd31854bab4f1ceba1c100cd07c90651940365e87477caefde81aeb4c3a2947",
  "cid": "QmV14fd31854bab4f1ceba1c100cd07c90651940365e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286941,
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
      "evaluated_at": 1760286941
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d064900f419d3a87616a0d6b4479207977db05ad9ae30068339ae19e9588ecf3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13366416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}