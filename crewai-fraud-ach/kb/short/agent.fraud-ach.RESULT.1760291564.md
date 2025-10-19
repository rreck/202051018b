```json
{
  "id": "4d20360e32e0de25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291564,
  "host_pid": "9e6742732c60:1",
  "hash": "862ecd85565292997da081b07399c16f33ab824b6520208bec92cb8b2e761f54",
  "cid": "QmV1862ecd85565292997da081b07399c16f33ab824b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291564,
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
      "evaluated_at": 1760291564
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
  "sig": "e429b8f11ee09be6c8fe6618400f27801dbd9e5e596ccec1929198efa1a92785"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591167362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 55548816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '24df3db171a5add1'}}}