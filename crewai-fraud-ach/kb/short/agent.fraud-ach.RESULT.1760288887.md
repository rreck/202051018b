```json
{
  "id": "91c51c2823bc73f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288887,
  "host_pid": "9e6742732c60:1",
  "hash": "2f4b2bd891e69a58522379722f9f7a3dcffe59c52470e532f0cc79ff8e30cad7",
  "cid": "QmV12f4b2bd891e69a58522379722f9f7a3dcffe59c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288887,
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
      "evaluated_at": 1760288887
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
  "sig": "c8794291a589b4c117c4df35e32bb1eda29a911a72a69f733ddc40f03f291ea1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245035140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 43338745, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'af29b59576821758'}}}