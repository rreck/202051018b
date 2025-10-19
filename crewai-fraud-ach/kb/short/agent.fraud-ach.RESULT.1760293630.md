```json
{
  "id": "81a2259120513834",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293630,
  "host_pid": "9e6742732c60:1",
  "hash": "2f33329085ae27a968e0adb7bc3b71cd8b3668b1f6d5e6110b5f2d46154aa414",
  "cid": "QmV12f33329085ae27a968e0adb7bc3b71cd8b3668b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293630,
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
      "evaluated_at": 1760293630
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
  "sig": "026cfac7f3dd0b94f03a4c5fbdfe3940fd751bc2f2e48cb6e00537bec9691f25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 89391408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}