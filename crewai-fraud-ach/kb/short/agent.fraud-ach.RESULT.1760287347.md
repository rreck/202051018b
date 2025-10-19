```json
{
  "id": "97028eed754743d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287347,
  "host_pid": "9e6742732c60:1",
  "hash": "825f83f010add1197e69e78aba4d434856813799414dc5932a1cfcc483f5e88c",
  "cid": "QmV1825f83f010add1197e69e78aba4d434856813799",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287347,
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
      "evaluated_at": 1760287347
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
  "sig": "4edb4aa32fa9a56a2167e5e7cf50288ca53b1868b81beebbe3b3039023ee45bd"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000027960877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 18572196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285763, 'matching_hash': '750facc395053d7c'}}}