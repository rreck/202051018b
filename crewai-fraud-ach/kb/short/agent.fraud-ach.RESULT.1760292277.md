```json
{
  "id": "ae8d645aeaaa3458",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292277,
  "host_pid": "9e6742732c60:1",
  "hash": "8d382ddaa8ae7e43d0c135b07ebf198501cc6bbcb56bd1d49298b888347e4258",
  "cid": "QmV18d382ddaa8ae7e43d0c135b07ebf198501cc6bbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292277,
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
      "evaluated_at": 1760292277
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
  "sig": "ed0665728509953a7a468a9594aa48f174e5f53ae5454abbb8e935e104020c60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022711139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 83452592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '282a945486899803'}}}