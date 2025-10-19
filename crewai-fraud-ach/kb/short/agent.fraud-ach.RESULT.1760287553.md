```json
{
  "id": "92ee5bb0d6a667d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287553,
  "host_pid": "9e6742732c60:1",
  "hash": "c0abfe6faedbacfebcf9588ffb4f973d5e688b3338853fb74d42462d0bb6b0aa",
  "cid": "QmV1c0abfe6faedbacfebcf9588ffb4f973d5e688b33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287553,
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
      "evaluated_at": 1760287553
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
  "sig": "3626874fe5a1cb748b9a1025e494fd63ae994133e0ae8f126ab379d06c18ff79"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 14847936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}