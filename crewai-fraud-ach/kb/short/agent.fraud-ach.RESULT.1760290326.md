```json
{
  "id": "2811b5e15c318323",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290326,
  "host_pid": "9e6742732c60:1",
  "hash": "20165959cdf84dd3c544dd73ed774c3cf29da0cde9b2beb9a34defa2c4c7d401",
  "cid": "QmV120165959cdf84dd3c544dd73ed774c3cf29da0cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290326,
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
      "evaluated_at": 1760290326
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
  "sig": "dfcc4fb8d7681ac45eb07ac10e975881a838a2d008d1e081ec3747f5b21c13ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247533282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 22049706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': '15ae64209d1fefcb'}}}