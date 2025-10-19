```json
{
  "id": "afc0500c1c5c0219",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292003,
  "host_pid": "9e6742732c60:1",
  "hash": "e5a738f8c34e283a24f43f5288722d1b4a21ec7fce9676f860ae177cd692f6ba",
  "cid": "QmV1e5a738f8c34e283a24f43f5288722d1b4a21ec7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292003,
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
      "evaluated_at": 1760292003
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
  "sig": "c70df342cdc4d702fc7c2293c418888fdeb738d9762cf11953be1959b7b6a958"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593598720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 38058720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '553fe68124b88597'}}}