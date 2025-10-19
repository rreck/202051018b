```json
{
  "id": "632eec41575113db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293855,
  "host_pid": "9e6742732c60:1",
  "hash": "ddc8d1752bd61d62171c074925d4735c4ddd2e25bd20c189847347313d4a526b",
  "cid": "QmV1ddc8d1752bd61d62171c074925d4735c4ddd2e25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293855,
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
      "evaluated_at": 1760293855
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
  "sig": "954830f1d8a5ce34fa7596a4243b9371232299921c0b01bbc32ef666ea316afb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022025451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 106337015, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}