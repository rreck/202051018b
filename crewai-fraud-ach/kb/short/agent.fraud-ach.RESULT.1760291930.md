```json
{
  "id": "84c92cef74a44c3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291930,
  "host_pid": "9e6742732c60:1",
  "hash": "3d1534ec8a4765dad8800274edf1a15a129fee7cf0fa585a065b47695cd3f89a",
  "cid": "QmV13d1534ec8a4765dad8800274edf1a15a129fee7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291930,
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
      "evaluated_at": 1760291930
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
  "sig": "996c87d23a28ee643f34ef6f984fecd029f9588a935db72afb74e3e486d998ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 37144386, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}