```json
{
  "id": "28754f191d36bdaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294602,
  "host_pid": "9e6742732c60:1",
  "hash": "85bbda40e2b6173e1361d55d8f02f9dc841fd7045be56029e2318514c4b3198f",
  "cid": "QmV185bbda40e2b6173e1361d55d8f02f9dc841fd704",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294602,
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
      "evaluated_at": 1760294602
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
  "sig": "a8a27e2e27da7e795bdc94187adb66c76289b8cbdf0ee557794fc93d215d5bdc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 105965290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}