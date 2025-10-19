```json
{
  "id": "d6ca1e41ae6ef588",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293861,
  "host_pid": "9e6742732c60:1",
  "hash": "86bfd91ae045b61bbdea644bf908576bfbe1027746c32875cf2bf6b4c2d08c3f",
  "cid": "QmV186bfd91ae045b61bbdea644bf908576bfbe10277",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293861,
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
      "evaluated_at": 1760293861
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
  "sig": "f707943990eeaf215c40c870b126be53a09d7f4e30863e877adb51669347e804"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465236749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 54901539, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '3442ebeb280b968f'}}}