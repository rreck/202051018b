```json
{
  "id": "0a6d4c8909839153",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293689,
  "host_pid": "9e6742732c60:1",
  "hash": "af3247c54070bcb8677d8c7bd88c04d627b60377c4bf33aee17d690f4e5f5219",
  "cid": "QmV1af3247c54070bcb8677d8c7bd88c04d627b60377",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293689,
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
      "evaluated_at": 1760293689
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
  "sig": "272e778acc92aa4270a5abeab4b0d3042894614de96495198784483113ec4e7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 70969304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}