```json
{
  "id": "90c197523f8ac27f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290780,
  "host_pid": "9e6742732c60:1",
  "hash": "d71461d95d70ae150728d96be6150b0c6148e9be1ca68e459b74556e779aec47",
  "cid": "QmV1d71461d95d70ae150728d96be6150b0c6148e9be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290780,
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
      "evaluated_at": 1760290780
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
  "sig": "ae8e5460ed92e7387360d19cd02a165983e4cb0e6b6c925a24891ad3de3d3426"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150592686
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 10020021, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '43d52159a9989a8b'}}}