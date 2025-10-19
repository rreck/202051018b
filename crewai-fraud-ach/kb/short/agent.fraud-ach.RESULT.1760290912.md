```json
{
  "id": "5f7e65531584ac84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290912,
  "host_pid": "9e6742732c60:1",
  "hash": "bc3902e791cb2699db4d9ab56ff79b7bfca545dfa6df1977beec270131153b0b",
  "cid": "QmV1bc3902e791cb2699db4d9ab56ff79b7bfca545df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290912,
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
      "evaluated_at": 1760290912
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
  "sig": "0f213502aa038d15db92b87f7b2dd4692fbfa872555ab59337c397511d5c43a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151102645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 66587508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '9dd268c0fa996698'}}}