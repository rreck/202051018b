```json
{
  "id": "4a98807a0bd5a56b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285853,
  "host_pid": "9e6742732c60:1",
  "hash": "58acd322b3db76fb66057afc543908ff1a3b165af9fccad0ea372cdc002c3af8",
  "cid": "QmV158acd322b3db76fb66057afc543908ff1a3b165a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285853,
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
      "evaluated_at": 1760285853
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
  "sig": "428f8c715ca1c05070be473b248b168717d9c8c384c96b4228ab9d7a947b3c2b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}