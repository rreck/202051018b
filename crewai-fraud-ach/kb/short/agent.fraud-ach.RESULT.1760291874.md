```json
{
  "id": "da3f4718a5873620",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291874,
  "host_pid": "9e6742732c60:1",
  "hash": "971c27304a28fe9caaba16bc4206585443ac2ec540cd8e1d5dc8f4e7c931301b",
  "cid": "QmV1971c27304a28fe9caaba16bc4206585443ac2ec5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291874,
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
      "evaluated_at": 1760291874
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
  "sig": "e26a25a0a5bccbf5a135ad3002c28f73308e85e4bfbfce2b6cdd008509d943f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248536916
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 27265115, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': '45170da297af1bde'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}