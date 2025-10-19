```json
{
  "id": "9f660eefc79894e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288536,
  "host_pid": "9e6742732c60:1",
  "hash": "5d8aaa9c3e259ebe47bb4fdf8f298024a8a7765d039947ff0b7585bff0b0a54e",
  "cid": "QmV15d8aaa9c3e259ebe47bb4fdf8f298024a8a7765d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288536,
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
      "evaluated_at": 1760288536
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
  "sig": "6ea636e2fcb1d9624a182b34f70a5465da7fa6c9790c63d21f917f061f9282a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 31980000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}