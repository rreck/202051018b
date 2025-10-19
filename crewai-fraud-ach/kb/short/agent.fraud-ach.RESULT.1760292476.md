```json
{
  "id": "4bd41605b2693668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292476,
  "host_pid": "9e6742732c60:1",
  "hash": "c796551803342481bdef57f316484ec2f3e37622efb94d88d7e068c61a398e51",
  "cid": "QmV1c796551803342481bdef57f316484ec2f3e37622",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292476,
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
      "evaluated_at": 1760292476
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
  "sig": "a8a03ec5bf7d85050f4f0b87f64cafbc386d150a7b9f63536f849ef1cf4fa777"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 65958750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}