```json
{
  "id": "0339a11eef6fd050",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293227,
  "host_pid": "9e6742732c60:1",
  "hash": "b3f0a0e61764a1fa6b665c06c2ed00bb1fb5f3e32a4987f7a0e05d92e50e2ea0",
  "cid": "QmV1b3f0a0e61764a1fa6b665c06c2ed00bb1fb5f3e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293227,
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
      "evaluated_at": 1760293227
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
  "sig": "23f0eac8c9216a8a7d4648fa21617a7328eaa2657da0e1d01eeee98562e98ffe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028413829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 33107512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '35164be796d7e820'}}}