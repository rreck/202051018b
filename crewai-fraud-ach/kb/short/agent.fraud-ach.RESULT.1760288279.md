```json
{
  "id": "0f911e92c27a4c50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288279,
  "host_pid": "9e6742732c60:1",
  "hash": "9dda5d9ce7cd2eb57556cbf39c22769376f74cf8c21bd31f4bbba458a9b7d226",
  "cid": "QmV19dda5d9ce7cd2eb57556cbf39c22769376f74cf8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288279,
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
      "evaluated_at": 1760288279
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
  "sig": "907b2ff08bcaaff399cfe8dad6a9107e9f5e6b70dd1b76a7bbb21451e4071178"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 28063288, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}