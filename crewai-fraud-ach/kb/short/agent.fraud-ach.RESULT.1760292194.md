```json
{
  "id": "a1003cf12d9ec0ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292194,
  "host_pid": "9e6742732c60:1",
  "hash": "fbaad4e883ecd9a737e651aa1720ad0b21d0cfffd9ba04d3ef4aff29a77a52cf",
  "cid": "QmV1fbaad4e883ecd9a737e651aa1720ad0b21d0cfff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292194,
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
      "evaluated_at": 1760292194
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
  "sig": "0a141654edb8c444285cdfb238754be4048265840c337d36f79a6dff37eb1862"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023745358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 29461824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '29c890c1b3276ef0'}}}