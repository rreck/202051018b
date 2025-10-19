```json
{
  "id": "de26098bbe2b49ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290812,
  "host_pid": "9e6742732c60:1",
  "hash": "f57bea1efb9af738f2d46a001d4e788cf3c850f4b489e9e3f2e41310926d2ef0",
  "cid": "QmV1f57bea1efb9af738f2d46a001d4e788cf3c850f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290812,
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
      "evaluated_at": 1760290812
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
  "sig": "a7b971e71435f340e0b5da4ef05165addc6185821f3aa02dc4fd58ce80340814"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020127754
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 30099520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '0e6816faa7d68d85'}}}