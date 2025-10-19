```json
{
  "id": "958ae1292d65556f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290475,
  "host_pid": "9e6742732c60:1",
  "hash": "2e75e7fea1bb4f5573ca335e6b1e301f4e32e679c38502488cd95c6dd7402518",
  "cid": "QmV12e75e7fea1bb4f5573ca335e6b1e301f4e32e679",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290475,
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
      "evaluated_at": 1760290475
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
  "sig": "18122550cae1a59b35f3485309ab65a3b80cdbff23a37102c7601c89edec6304"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248710981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 38749771, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}