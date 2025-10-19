```json
{
  "id": "67f15fd380f379ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293402,
  "host_pid": "9e6742732c60:1",
  "hash": "88f38e3c923688f6dc510f9c1207bb3e69c997fe68934f358f2b582475513b4c",
  "cid": "QmV188f38e3c923688f6dc510f9c1207bb3e69c997fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293402,
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
      "evaluated_at": 1760293402
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
  "sig": "0e6081d732d7f3ad1735a57a1e25a5cdf9446d8d35d2b1476f05b9f8fac41bbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 51485714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}