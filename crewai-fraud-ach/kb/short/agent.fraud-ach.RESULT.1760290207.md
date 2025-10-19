```json
{
  "id": "04a466f3fed17990",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290207,
  "host_pid": "9e6742732c60:1",
  "hash": "d6c449410323c253e6ff9a38ff5723f4c595848f3da68dbaa4180e786459f710",
  "cid": "QmV1d6c449410323c253e6ff9a38ff5723f4c595848f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290207,
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
      "evaluated_at": 1760290207
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
  "sig": "f1c642c711f6ca5333e150cbaaa3bffe04e40a2a5c58eefa13293ce9d04edeb4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597908242
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 16483248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': 'd5ac49343fc3272b'}}}