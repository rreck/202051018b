```json
{
  "id": "0a7d435d39f69e58",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290462,
  "host_pid": "9e6742732c60:1",
  "hash": "cc1c36e0899eec73e7ec0b2e0b89abf848b2e14c93f7a5db36ce94459fcfeb56",
  "cid": "QmV1cc1c36e0899eec73e7ec0b2e0b89abf848b2e14c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290462,
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
      "evaluated_at": 1760290462
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
  "sig": "9e645bb71bb4a0815c4754c697360fcbc45bb64f2cfd1e5d27f8c0e9d09767cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026087105
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 44280901, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '109bc77652f62494'}}}