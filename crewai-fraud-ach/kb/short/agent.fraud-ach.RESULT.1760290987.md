```json
{
  "id": "6988cdcfa411d00f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290987,
  "host_pid": "9e6742732c60:1",
  "hash": "0a75ecc54e0b351df924cfe0f2489b739ca2405d8b579c80f54e2bf94ae736a3",
  "cid": "QmV10a75ecc54e0b351df924cfe0f2489b739ca2405d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290987,
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
      "evaluated_at": 1760290987
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
  "sig": "d7f8cffea8f94db6cd6cfabf1346d03be4b9b86661a5a47c46f3f4850deab8f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465603072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}een': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}