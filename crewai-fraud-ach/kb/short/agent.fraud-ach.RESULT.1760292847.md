```json
{
  "id": "d119b7d0d36d2a5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292847,
  "host_pid": "9e6742732c60:1",
  "hash": "4906c031571a7901e589275133a522bd684a5e42a4242c3d9f3825ec7bdee7e6",
  "cid": "QmV14906c031571a7901e589275133a522bd684a5e42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292847,
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
      "evaluated_at": 1760292847
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
  "sig": "a75df6636f5f5d90fe07f7bfb88c4e897f80bd959cb6db63858c89066284b769"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275531952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 282, 'threshold': 50, 'total_amount': 31555800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 281, 'first_seen': 1760284979, 'matching_hash': '283eac5c65a068f4'}}}