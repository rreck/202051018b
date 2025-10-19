```json
{
  "id": "760aeb3c81465d21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291605,
  "host_pid": "9e6742732c60:1",
  "hash": "6ad7be29457933add43a66607a1e3d1aeab0959cb948d9a732a3196b7d76741b",
  "cid": "QmV16ad7be29457933add43a66607a1e3d1aeab0959c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291605,
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
      "evaluated_at": 1760291605
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
  "sig": "56965bb86594d8d677d9f42fc036c6ba25c92a14a6e9973363b1d5c2906640f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028831887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 49970177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': '597950b73179eb3f'}}}