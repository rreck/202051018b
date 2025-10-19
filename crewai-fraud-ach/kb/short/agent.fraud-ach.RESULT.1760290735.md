```json
{
  "id": "75669a18c4916be8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290735,
  "host_pid": "9e6742732c60:1",
  "hash": "3e53bde8845f6218de3821c060779d625ea828a46925c43203e6f8a576edac5c",
  "cid": "QmV13e53bde8845f6218de3821c060779d625ea828a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290735,
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
      "evaluated_at": 1760290735
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
  "sig": "09432859fafc8d3333c6f3cdf699b57445319c4068c51ed2474a134738f078db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 63937386, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}