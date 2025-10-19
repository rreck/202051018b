```json
{
  "id": "c68230101a62a7a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287927,
  "host_pid": "9e6742732c60:1",
  "hash": "2f2d436f12c1f1e65a62fd87950c5393bf3c48fa754c366aaf3a9516e9541f6e",
  "cid": "QmV12f2d436f12c1f1e65a62fd87950c5393bf3c48fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287927,
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
      "evaluated_at": 1760287927
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
  "sig": "963a6b4e2c479bf16d32fc39e0c053a88fb1a6cead73c721915d72d87e4ada72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154917617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 32395517, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': 'bb8a68e9925b6436'}}}