```json
{
  "id": "013e999269730a4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288441,
  "host_pid": "9e6742732c60:1",
  "hash": "c0109eb27944dae99dbea5bf525357fd8a660ea200c2b6ea03fd5b863ce88bcf",
  "cid": "QmV1c0109eb27944dae99dbea5bf525357fd8a660ea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288441,
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
      "evaluated_at": 1760288441
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
  "sig": "2b667e6549461908d0f2d7e6a9e07be6e13135d5f3ff036392d49e8a05fca09a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 36056565, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}