```json
{
  "id": "a770119d38a52bbc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292727,
  "host_pid": "9e6742732c60:1",
  "hash": "6d8ee1e5b87648c035bbfaa43fff62f7879655419eeef578ca63ee07145931a3",
  "cid": "QmV16d8ee1e5b87648c035bbfaa43fff62f787965541",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292727,
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
      "evaluated_at": 1760292727
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "0af82209259e6abfdcd2326b6d67821df8a481a0d92ea2b3d9d1b6ddf5f13c13"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000020453252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 102000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '94693ae2b8a79c3a'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}