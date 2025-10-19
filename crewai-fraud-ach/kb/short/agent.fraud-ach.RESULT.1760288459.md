```json
{
  "id": "9dc065962fdfdebf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288459,
  "host_pid": "9e6742732c60:1",
  "hash": "d7e15f5aaacaef4a9fcdb700c477bb92959009b4fed494d4d27c74d1c1f08de3",
  "cid": "QmV1d7e15f5aaacaef4a9fcdb700c477bb92959009b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288459,
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
      "evaluated_at": 1760288459
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
  "sig": "9bd2c5e9e035186711ddd69facf6fcef7166be44d5d500d751bbc41f35fc060c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 13333054, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}