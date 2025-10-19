```json
{
  "id": "3372f92e7487a17a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286154,
  "host_pid": "9e6742732c60:1",
  "hash": "7b49c39dffda14c3595171270f88721f633cac6ea5d4676ae90a990f894118a3",
  "cid": "QmV17b49c39dffda14c3595171270f88721f633cac6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286154,
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
      "evaluated_at": 1760286154
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
  "sig": "23b66a3e74c097f524c44ae60081189eae7c65fa05214245c504bc215e27c42d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246878582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 25093920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760284979, 'matching_hash': '3e968f91ba41b0b5'}}}