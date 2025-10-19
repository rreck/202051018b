```json
{
  "id": "09e043bef26d941b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291716,
  "host_pid": "9e6742732c60:1",
  "hash": "bf6a01cc617107f3e41b2f8731ed044a03c5689087bf8ceeee13cf3bd4edede2",
  "cid": "QmV1bf6a01cc617107f3e41b2f8731ed044a03c56890",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291716,
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
      "evaluated_at": 1760291716
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
  "sig": "96cb751fcbb633ffd0e92cad3b75f65e4e98b016de0e7ed07e7e4c72845c2538"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 34604847, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}