```json
{
  "id": "ff37e175459c6fe2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290420,
  "host_pid": "9e6742732c60:1",
  "hash": "7bcf8c0050ee53347fd1d9ff4d0f5a4d36717a65eceee75fb16f31c7a510c3ed",
  "cid": "QmV17bcf8c0050ee53347fd1d9ff4d0f5a4d36717a65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290420,
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
      "evaluated_at": 1760290420
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
  "sig": "b40c37671392d37068620d956954831ed7c8f555682abe46304318b1838ed912"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279650502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 37418850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'f07ec2819f69af8b'}}}