```json
{
  "id": "4107083bcea4c9a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294020,
  "host_pid": "9e6742732c60:1",
  "hash": "28ff4a161b2d6f00167f68c30836d8e70d4ff40aa3b5c9af86e2d716cfe0a43c",
  "cid": "QmV128ff4a161b2d6f00167f68c30836d8e70d4ff40a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294020,
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
      "evaluated_at": 1760294020
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
  "sig": "fd61557f3bbe6aac102766d806a2c205438f83708af7841d29aef6f242d80bac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248879476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 43757270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '88da1f364f410d45'}}}