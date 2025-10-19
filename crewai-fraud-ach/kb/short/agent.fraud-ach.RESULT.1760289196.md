```json
{
  "id": "95eda702da7273e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289196,
  "host_pid": "9e6742732c60:1",
  "hash": "43c58505adf149134ebd1e7b798b6e5b9fdd40a1019484b88487a2ae362df258",
  "cid": "QmV143c58505adf149134ebd1e7b798b6e5b9fdd40a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289196,
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
      "evaluated_at": 1760289196
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
  "sig": "4191bc57508a51bb040ac70bb4f8b4b3670660fcf8f4281d80650608cd1e56a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240849779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 22404820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}