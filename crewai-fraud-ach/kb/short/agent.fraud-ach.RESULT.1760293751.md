```json
{
  "id": "d9b2828b00156e08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293751,
  "host_pid": "9e6742732c60:1",
  "hash": "c3c5b20d32fb5b3e4597c2ac6900191e6495c3b199064e881c650e3e4a8745f6",
  "cid": "QmV1c3c5b20d32fb5b3e4597c2ac6900191e6495c3b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293751,
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
      "evaluated_at": 1760293751
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
  "sig": "88e43ac981bb095bab55079174d0a730e4264aaa23958004dab52e9d65087c30"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158436711
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 103708125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '839de208acaae015'}}}