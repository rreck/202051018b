```json
{
  "id": "25415e62798d7e0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286873,
  "host_pid": "9e6742732c60:1",
  "hash": "f1b26ac2077655844c53ad0bd67430f43e63f76c4ad81e64ea6862f04e1a6020",
  "cid": "QmV1f1b26ac2077655844c53ad0bd67430f43e63f76c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286873,
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
      "evaluated_at": 1760286873
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
  "sig": "a1ce1009adfb160db6704652cd2fc000be73db6cdb19d694523e223e93bab78a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11871400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}