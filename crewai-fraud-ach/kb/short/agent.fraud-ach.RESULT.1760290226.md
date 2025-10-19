```json
{
  "id": "c35ffa4d60e55312",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290226,
  "host_pid": "9e6742732c60:1",
  "hash": "2b6f946a0dda5da4e66b72c5fb7c80aa2d24394c54af5da780ce7cb32062cc31",
  "cid": "QmV12b6f946a0dda5da4e66b72c5fb7c80aa2d24394c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290226,
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
      "evaluated_at": 1760290226
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
  "sig": "658c3a4ae406ee3e00664f8ff1d611d56d77c532a2e1ce9b9f557961ec0414d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 23029045, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}