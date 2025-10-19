```json
{
  "id": "8bcdd272fe18752e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287161,
  "host_pid": "9e6742732c60:1",
  "hash": "798cb34fd20290b1dbd8e8d6e4d4fa183952b0a68c151490457776d3e7791e6c",
  "cid": "QmV1798cb34fd20290b1dbd8e8d6e4d4fa183952b0a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287161,
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
      "evaluated_at": 1760287161
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "99c39c26d6126ea7ff96140ba3bbe1d2c45e5f628ce92d6cc9f7cd508d095e4a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025832040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22419150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '02af8ad93f509b45'}}}