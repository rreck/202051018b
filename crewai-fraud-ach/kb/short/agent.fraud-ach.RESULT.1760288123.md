```json
{
  "id": "2fa378ff4a08cb92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288123,
  "host_pid": "9e6742732c60:1",
  "hash": "d20018aa3ba64e6ba110fc1542d21c2ec3e9f1360f24f8d193dfc2ef591a0afb",
  "cid": "QmV1d20018aa3ba64e6ba110fc1542d21c2ec3e9f136",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288123,
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
      "evaluated_at": 1760288123
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
  "sig": "6c557a58af04cb97f8b563ae59630cf19d8238a31afd4ee583d48fc5b69a984b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}