```json
{
  "id": "35476c5d14d6e75c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293067,
  "host_pid": "9e6742732c60:1",
  "hash": "e8980dafba268f38770fffa8b9723a58c60391e19756d1dc5fb3c4771db34542",
  "cid": "QmV1e8980dafba268f38770fffa8b9723a58c60391e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293067,
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
      "evaluated_at": 1760293067
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
  "sig": "9359e0342a1cbd932eb140269d7d27b08abb1a85e89da4717e2f0b8a283d2bb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150128981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 40355860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}