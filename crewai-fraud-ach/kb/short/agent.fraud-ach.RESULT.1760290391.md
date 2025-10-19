```json
{
  "id": "845409f8663a78d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290391,
  "host_pid": "9e6742732c60:1",
  "hash": "2a8587f2b641c35297d9d038ae2ede84640c3099e53b40522be5c2219acad5df",
  "cid": "QmV12a8587f2b641c35297d9d038ae2ede84640c3099",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290391,
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
      "evaluated_at": 1760290391
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
  "sig": "4f09832acf6099309dca1d67b6e8fd19ba221b82816cfd133f032d1958f7f7cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153425339
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 65843398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'd6fcd27194bc1174'}}}