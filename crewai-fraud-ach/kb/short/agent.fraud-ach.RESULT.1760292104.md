```json
{
  "id": "9e9e318bbbfd3f2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292104,
  "host_pid": "9e6742732c60:1",
  "hash": "0d7336af10feff3da48b054e7d7f214de58d924dfd413624d29057bddce2f5f6",
  "cid": "QmV10d7336af10feff3da48b054e7d7f214de58d924d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292104,
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
      "evaluated_at": 1760292104
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
  "sig": "622470d5cac3f7142418fcdb0a9759891ef5e2fe0c83ab4518790a791d0b8d25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596690593
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 266, 'threshold': 50, 'total_amount': 37494030, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 265, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}