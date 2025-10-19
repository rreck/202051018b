```json
{
  "id": "01c98a6a47b5c32e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287634,
  "host_pid": "9e6742732c60:1",
  "hash": "de5cab58fdd94eeae1cd727b40a2c7133342617a5025a1a792f8c19217df5a69",
  "cid": "QmV1de5cab58fdd94eeae1cd727b40a2c7133342617a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287634,
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
      "evaluated_at": 1760287634
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
  "sig": "3885a10fdfe1f394b1ffd1a58514d4b6d214e6c597de633534abf5d291d833bd"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 122105156493582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}een': 1760285763, 'matching_hash': 'c92648ab22001236'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}