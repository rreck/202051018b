```json
{
  "id": "19bd8c804f02e969",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287502,
  "host_pid": "9e6742732c60:1",
  "hash": "75746498bae2f070bc58410f06547e378f9cd676759355c4a15d31bf4b045d3e",
  "cid": "QmV175746498bae2f070bc58410f06547e378f9cd676",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287502,
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
      "evaluated_at": 1760287502
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
  "sig": "f7d3ba1e350517c498668f6c2b332302e07dd979c11639cbc0da4b206f749db7"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 122105158642736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 11354680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}