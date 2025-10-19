```json
{
  "id": "4af8e96d13b0f55b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294440,
  "host_pid": "9e6742732c60:1",
  "hash": "90b97bcbad4a00568ff1a0b1c93aff5874adcf63fbd955bf811699fc30b79be3",
  "cid": "QmV190b97bcbad4a00568ff1a0b1c93aff5874adcf63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294440,
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
      "evaluated_at": 1760294440
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
  "sig": "f3d3f42b2b166cb7ab3b00fdc0cb1c56098c54c8b4d9553660059ca81a5fcaf2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158691889
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 66668560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '7f09a9884a1a1f0e'}}}