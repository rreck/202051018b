```json
{
  "id": "d6bfb48a4d374062",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294834,
  "host_pid": "9e6742732c60:1",
  "hash": "a21df627cf6a7da7f0bcc4a1e183430877ed2dc707a99c1c21c1e51c8623aace",
  "cid": "QmV1a21df627cf6a7da7f0bcc4a1e183430877ed2dc7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294834,
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
      "evaluated_at": 1760294835
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
  "sig": "f2d6e973c112aa500b801f6ebd043695e6af2a2b613c88c38b48a385f4ceace4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598076965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 38418940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '05e01649c2d43b8b'}}}