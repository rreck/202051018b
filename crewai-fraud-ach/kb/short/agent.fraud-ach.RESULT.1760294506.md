```json
{
  "id": "947fea12a0b13004",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294506,
  "host_pid": "9e6742732c60:1",
  "hash": "eae2509911c51fefe95ce151a1d02a5de67c4f6ea022f460ab6a965faff1702c",
  "cid": "QmV1eae2509911c51fefe95ce151a1d02a5de67c4f6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294506,
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
      "evaluated_at": 1760294506
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
  "sig": "6b8002ec545b8c7f1281e4324ea11e8ee32dc3210b722397d5bf9f6ed915009e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 98471346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}