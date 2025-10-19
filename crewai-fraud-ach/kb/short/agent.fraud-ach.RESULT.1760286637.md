```json
{
  "id": "0b1952daa5504e78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286637,
  "host_pid": "9e6742732c60:1",
  "hash": "91463110ee891083fc4a83385c390d08b463eb28886ccdf1b717444cb0e8d429",
  "cid": "QmV191463110ee891083fc4a83385c390d08b463eb28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286637,
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
      "evaluated_at": 1760286637
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
  "sig": "fe8c11bfe437e353c788cf610b8ca013a8498040d1fe87ef11c32f7e3189ef7d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10413536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}