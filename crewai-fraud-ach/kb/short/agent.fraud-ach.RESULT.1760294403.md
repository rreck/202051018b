```json
{
  "id": "ad2ca32a382f3dc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294403,
  "host_pid": "9e6742732c60:1",
  "hash": "833153dd02f2ddb8bfa0ab32be28d8a9f556155ee123d2b58248b397f25deb74",
  "cid": "QmV1833153dd02f2ddb8bfa0ab32be28d8a9f556155e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294403,
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
      "evaluated_at": 1760294403
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
  "sig": "110e6dbfb9a428a09b805f688c1ac097278349554ab3b4cfbfcbf344ed227274"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 69561396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}