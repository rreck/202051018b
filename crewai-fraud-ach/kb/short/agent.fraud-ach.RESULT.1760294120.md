```json
{
  "id": "a9e3713f735c051c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294120,
  "host_pid": "9e6742732c60:1",
  "hash": "3edba1a361038198586a50c93528c46efd4b24d5d091ba6018a9127905086177",
  "cid": "QmV13edba1a361038198586a50c93528c46efd4b24d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294120,
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
      "evaluated_at": 1760294120
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
  "sig": "804df6b56a4afb6ecc52e71c2a8d4ab31de130ff3d26d433958fa26a124874ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025853793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 63083584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'ff3a3f7dec7a702a'}}}