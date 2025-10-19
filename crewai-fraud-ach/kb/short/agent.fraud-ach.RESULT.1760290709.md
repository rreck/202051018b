```json
{
  "id": "4850b8913050fd88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290709,
  "host_pid": "9e6742732c60:1",
  "hash": "f82027b00eb3eaed57a7a418f8f97ca92d389b518a1f8d292992f5e1b815625f",
  "cid": "QmV1f82027b00eb3eaed57a7a418f8f97ca92d389b51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290709,
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
      "evaluated_at": 1760290709
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
  "sig": "9a8236f9075fa346d8f6985b78a89e4c20660568a8aa716a5d895542657035d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245742893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 57415057, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '17d6d8b38d025182'}}}