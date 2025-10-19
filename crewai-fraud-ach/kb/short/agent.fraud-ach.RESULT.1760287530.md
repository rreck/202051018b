```json
{
  "id": "b78a17d478c3ad0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287530,
  "host_pid": "9e6742732c60:1",
  "hash": "991c5560bc6010859318d62812803044ce38099daf2c8be69f37f7fd2f6f51b1",
  "cid": "QmV1991c5560bc6010859318d62812803044ce38099d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287530,
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
      "evaluated_at": 1760287530
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
  "sig": "b3728c864dcc6d5875ac8e0f67ede207c71edfc85a4f42be9052ff9ba19254dc"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 044000038099532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 25289586, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': 'ac68ba9e81a65c72'}}}