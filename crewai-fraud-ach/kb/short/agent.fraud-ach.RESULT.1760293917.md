```json
{
  "id": "4a7ebce2ee5dca4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293917,
  "host_pid": "9e6742732c60:1",
  "hash": "3876acf4685dcd6b3b2b5ee72b6fee4587e755b56cb635e02efd71008db6da50",
  "cid": "QmV13876acf4685dcd6b3b2b5ee72b6fee4587e755b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293917,
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
      "evaluated_at": 1760293917
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
  "sig": "2ea2675594ea1d734993cffe7e438d2b5075a825bc620f3b5d413cd297d6a12c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591602283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 33181068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '995d19d96715feaf'}}}