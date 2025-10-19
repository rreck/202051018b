```json
{
  "id": "8765fdc656d76e15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292094,
  "host_pid": "9e6742732c60:1",
  "hash": "d57072fb9bb5be75f738ccb7199e38b7ebec27669470bc6b0dc44ad2d98f48e1",
  "cid": "QmV1d57072fb9bb5be75f738ccb7199e38b7ebec2766",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292094,
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
      "evaluated_at": 1760292094
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
  "sig": "62e80f8d63df7b9c593548d11f0f33975503da7fb13ac413e098f5377391ffc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278925206
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 47392080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'f9778a1b3fb70950'}}}