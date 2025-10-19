```json
{
  "id": "8e410d11adb4a129",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292707,
  "host_pid": "9e6742732c60:1",
  "hash": "3d5df8ad5d6cc565574b4b217117db6bb11a48c7dbea1405158bb933c361ed7b",
  "cid": "QmV13d5df8ad5d6cc565574b4b217117db6bb11a48c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292707,
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
      "evaluated_at": 1760292707
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
  "sig": "7f27405cf58b7ef5e4baea05bb1e815600b1214b70a069a0be97993c0566c198"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 69234774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}