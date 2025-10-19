```json
{
  "id": "9a2a022ea7c6eac2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288800,
  "host_pid": "9e6742732c60:1",
  "hash": "eb5efa22c694f5c01a4af64626089ef5857125de1aff4c6cd453576d3bdcf52c",
  "cid": "QmV1eb5efa22c694f5c01a4af64626089ef5857125de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288800,
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
      "evaluated_at": 1760288800
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
  "sig": "509ea7419bdc39056019f35bd8d19ec5e8afb85e11db4d74fb0b9c5cd30204d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029236644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 23690680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}