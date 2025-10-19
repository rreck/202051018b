```json
{
  "id": "a8b87ebb0ce096ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291473,
  "host_pid": "9e6742732c60:1",
  "hash": "d636c9cc1cccb1b0e27f648ea91154888e4d687179da067701a81e5df81bb2d3",
  "cid": "QmV1d636c9cc1cccb1b0e27f648ea91154888e4d6871",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291473,
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
      "evaluated_at": 1760291473
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
  "sig": "f05004d9b79908676e38549a45f58f611c321acc0c8f44c9387d9d23602b2508"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 41566448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}