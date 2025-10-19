```json
{
  "id": "8156b09dafc7be38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294503,
  "host_pid": "9e6742732c60:1",
  "hash": "7ebae7306e494d23be8c0fd9a84fefe10ad400e4d152bd2813e49746f02ea195",
  "cid": "QmV17ebae7306e494d23be8c0fd9a84fefe10ad400e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294503,
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
      "evaluated_at": 1760294503
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
  "sig": "669ac93564d381ce39a66ffc8ef3233ae482ae217ac08282ec3d8b8996652da7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591685004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 78598018, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'e63d914157ffc7ed'}}}