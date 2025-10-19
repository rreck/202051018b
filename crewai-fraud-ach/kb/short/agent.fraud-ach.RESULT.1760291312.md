```json
{
  "id": "adb09aa00cf5707a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291312,
  "host_pid": "9e6742732c60:1",
  "hash": "408e4500fa1a9de24831c162b944ba91d097a4d43a7e8b6cb95d58100c5134e8",
  "cid": "QmV1408e4500fa1a9de24831c162b944ba91d097a4d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291312,
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
      "evaluated_at": 1760291312
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
  "sig": "e2eeaa3c6da7d154e18ac92271798a68917872271ed18f8e7fc063c423960990"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155818462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 56383320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '4e45a5675434ecee'}}}