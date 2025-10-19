```json
{
  "id": "3826193c3c21e8e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293129,
  "host_pid": "9e6742732c60:1",
  "hash": "33f2179b6c312b7794a1005288af4d5b69d69b23f3f154699e2c5aca978a594e",
  "cid": "QmV133f2179b6c312b7794a1005288af4d5b69d69b23",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293129,
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
      "evaluated_at": 1760293129
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
  "sig": "74fe3436afaf1c05b550ea935712d7b8ec2fae6b726c821bb6995eda3e6366ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156085799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 50092632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'a879e580def76590'}}}