```json
{
  "id": "76034a30add33479",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290521,
  "host_pid": "9e6742732c60:1",
  "hash": "f5041c3f074fc0fba3a268a3d0ed19ab260c379f614d18315c858be25819659a",
  "cid": "QmV1f5041c3f074fc0fba3a268a3d0ed19ab260c379f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290521,
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
      "evaluated_at": 1760290521
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
  "sig": "17be09a3245b6062fa7ce1905f334c8a1f0d02d62a3d14060395243c09172201"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 72345464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}