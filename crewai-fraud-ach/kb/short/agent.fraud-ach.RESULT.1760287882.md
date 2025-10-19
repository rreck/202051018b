```json
{
  "id": "a570d8bcc82f819f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287882,
  "host_pid": "9e6742732c60:1",
  "hash": "02928fa6eb66ccedea081650622b8a074eafd8b57cda3064724c5aed7ddbd188",
  "cid": "QmV102928fa6eb66ccedea081650622b8a074eafd8b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287882,
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
      "evaluated_at": 1760287882
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
  "sig": "30d14efb8e212aa363ab2f706ecfcc7f8d38a9281fc4359cf817f144e188673f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033294426
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 10845750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': '591497f4da3dc787'}}}