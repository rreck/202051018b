```json
{
  "id": "0c9a04d6dc59c363",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291420,
  "host_pid": "9e6742732c60:1",
  "hash": "65416a53fb3ac061899b46d4becc550195bce64a52266cd1d1d0791f2e88b518",
  "cid": "QmV165416a53fb3ac061899b46d4becc550195bce64a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291420,
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
      "evaluated_at": 1760291420
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
  "sig": "43676c1606c13cd11d1ef638c93a645170d53914f0e99dc09fca4abc15e2937d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 55375152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}