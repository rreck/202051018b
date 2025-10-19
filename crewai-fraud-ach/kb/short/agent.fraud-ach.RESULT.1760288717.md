```json
{
  "id": "da3ea0b7bfbe9b0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288717,
  "host_pid": "9e6742732c60:1",
  "hash": "fc12d93bd125a7f512010beeb296dcbdbdad7d391876fd0378eec0564fd641a1",
  "cid": "QmV1fc12d93bd125a7f512010beeb296dcbdbdad7d39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288717,
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
      "evaluated_at": 1760288717
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
  "sig": "d62e388e240d381ef3ca30db129a128b0f7185785ad1013a1dfd69a6a2aef3a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021760547
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 26460738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': 'fad63ed6e9f4a51a'}}}