```json
{
  "id": "69d1811e5fb8e6b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293934,
  "host_pid": "9e6742732c60:1",
  "hash": "ba4cfee2c257943ebbe101df228aa0e8dbd22a2f49d3ffd668a39d080a56bf94",
  "cid": "QmV1ba4cfee2c257943ebbe101df228aa0e8dbd22a2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293934,
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
      "evaluated_at": 1760293934
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
  "sig": "d06145f3da487e714366f8c51a183caf0a2acfe48788497f72395dd5ef1fdf7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246932907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 103050528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'b5767c7cd6e7c742'}}}