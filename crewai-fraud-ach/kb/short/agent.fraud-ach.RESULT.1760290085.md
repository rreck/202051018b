```json
{
  "id": "f37b5e5303b4cd6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290085,
  "host_pid": "9e6742732c60:1",
  "hash": "436b6cb23fd9cbb0f2c9ec8e49585c0363f338f4dca4d7123c21b33976303c71",
  "cid": "QmV1436b6cb23fd9cbb0f2c9ec8e49585c0363f338f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290085,
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
      "evaluated_at": 1760290085
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
  "sig": "2bff998aa146af6a4cb7b0d8a4f5b5e1d8310532d62906bc0dae12267ddcfd80"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 67996545, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}